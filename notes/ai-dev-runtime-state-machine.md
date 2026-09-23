---
version: 1
id: ai-dev-runtime-state-machine
title: 运行核心：状态机、SQLite、事务与原子提交
tags:
  - SQLite
  - Rust
  - 架构
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 状态图以声明式配置编译进二进制，所有变更在单个事务里落库并追加事件，产物先落文件再登记。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# 运行核心：状态机、SQLite、事务与原子提交

> 状态图以声明式配置编译进二进制，所有变更在单个事务里落库并追加事件，产物先落文件再登记。

## 声明式状态机

Run 侧的状态链是 `created → (scanning) → index_running → index_waiting_approval → architecture_* → technology_selection_* → parallel_running / parallel_blocked → quality_gate_3 → unit_test_running → quality_gate_4 → e2e_test_running → quality_gate_5 → final_waiting_approval → completed`，终止态为 `cancelled`、`manual_intervention`、`failed`；Stage 侧八个状态是 `pending / running / gate_pending / waiting_approval / retry_scheduled / succeeded / manual_intervention / failed`。这张图物理上就是 `config/phase-1-foundation.json`，靠 `include_str!` 编译进二进制，也是文档反复强调的唯一事实源的落点：校验器、CLI 帮助、文档表格与测试都从这一份快照派生。启动时 `validate_source()` 交叉校验每条边的 from/to 均已声明、guard 落在 13 个 `KNOWN_GUARDS` 之内。`apply_transition(source, event, context)` 先匹配边再跑 `guard_passes`，guard 实质是对 `HashMap<&str,String>` 做字符串等值比较，例如 `attempts_below_limit` 比较 `attempt` 与 `max_attempts`，`approval_is_valid_for_index` 要求 `approval_stage=="index"`、`approval_gate_status=="passed"`、`approval_manifest_exists=="true"`、`approval_role_allowed=="true"` 同时成立。Phase 1 只声明了 14 条 transition，主链连通到 `architecture_running` 为止。

## 表结构与设计落差

核心表有 `runs`、`stages`（含 `checkpoint_json`）、`attempts`、`gates`、`artifacts`（`UNIQUE(run_id,relative_path,attempt)`）、`approvals`、`manifests`、`outbound_logs`、`events`（`UNIQUE(run_id,sequence_no)`）与 `schema_meta`；大段正文不入库，只存 URI、摘要和 hash。`StateStore::open` 固定打开 `PRAGMA foreign_keys = ON` 与 `journal_mode = WAL`。三处落差值得记：`runs.status` 的 CHECK 约束只放行到 `architecture_running`，后段状态在数据库层面根本写不进去；`schema_meta` 仅有单版本 1 且用 `INSERT OR IGNORE`，设计里“逐版本迁移、失败 rollback 并返回 STATE_CORRUPTED”的引擎尚未落地；实现侧个别约束反比文档更硬，`manifests` 带 `CHECK(committed_count<=required_count)`，`attempts.status` 限定在 running、succeeded、abandoned、failed。

## 事务、事件与并发锁

一次提交的步骤顺序是：校验状态转换 → 校验 artifact 路径 → 验 manifest hash → upsert 相关记录 → 恰好追加一条事件 → 更新 run status → COMMIT，中途任何一步失败整体回滚。`sequence_no` 由 `SELECT COALESCE(MAX(sequence_no),0)+1` 单调生成。`resume_interrupted` 把旧 attempt 标成 `PROCESS_INTERRUPTED` 的 abandoned 并写 `stage.abandoned` 与 `stage.resumed` 两条事件；`cancel_run` 以 `RUN_CANCELLED` 收尾运行中的 attempt。同一目标项目只允许一个活跃 run：业务查询 `active_run_for_repo()` 负责给出友好错误，partial unique index `one_active_run_per_repo`（`ON runs(repo_root) WHERE status NOT IN ('completed','cancelled','failed')`）负责最终互斥。发现有效锁立刻返回冲突，不杀已有进程，过期锁也不自动接管。

## Checkpoint 与产物提交

checkpoint 记 `run_id`、`stage_id`、`attempt`、`input_hash`、`config_hash`、`stack_profile_hash`、`approved_artifact_ids` 与 `next_action`。恢复前逐项校验仓库根一致、config hash 未变、frozen decisions 与 StackProfile hash 未变或已有批准变更、manifest 文件仍在且 hash 对得上、没有第二把有效锁，任一项不成立就明确报错而不是猜。提交粒度是 stage attempt manifest，重试必须新建 attempt，旧 manifest 只能标 `abandoned`。`ArtifactStore::commit` 的实际顺序是：读临时目录产物算 sha256 组 `ArtifactEntry` → 对未签名的 manifest JSON 算 `manifest_sha256` → `fs::rename` 原子移动到最终目录，目标已存在直接报 `attempt already committed` → 写 pretty manifest JSON → 单个事务插入 `manifests`(committed) 与 `artifacts`。路径安全由 `validate_component` 与 `checked_path` 逐段拒绝 `..`，证据文件上限 `MAX_EVIDENCE_BYTES` 为 8 MiB，`verify_detailed` 重算 hash 支撑 `artifacts --verify`。
