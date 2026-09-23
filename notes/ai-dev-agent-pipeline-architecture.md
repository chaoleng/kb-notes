---
version: 1
id: ai-dev-agent-pipeline-architecture
title: AI 开发 Agent Pipeline — 架构知识摘要
tags:
  - Agent
  - 架构
  - AI应用
  - Pipeline
  - Rust
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现（crates/pi-pipeline）
summary: CLI 形态、可断点续跑、可审计的多智能体开发流水线；SQLite 为流程状态唯一真相源，LLM 只做生成，质量门由确定性 Skill 判定，人工承認不可被替代。
created: 2026-09-12T02:45:51.000Z
updated: 2026-09-12T02:45:51.000Z
favorite: false
related:
---

# AI 开发 Agent Pipeline — 架构知识摘要

从 `ai-dev-agent-pipeline` 项目的设计分片（`docs/product-brief.md`、`architecture-design.md`、`runtime-core.md`、`cli-contract.md`、`brownfield-adapters.md`、`security-review.md`、`phase-1-foundation.md`）抽取的主要架构知识。原项目是设计文档 + Rust 实现（`crates/pi-pipeline`），面向日本客户交付场景，强调保密、过程留痕和可审计。本文只保留架构层面的核心决策与契约，不复制全部规范细节。

## 1. 定位与目标

一套 **CLI 形态、可断点续跑、可审计的多智能体软件开发流水线**。把需求分析、架构设计、技术选型、Infra、前端、后端、单元测试、E2E 测试组织为带质量门（Quality Gate）和人工承認（レビュー门）的阶段图，由 AI Agent 承担各阶段生成工作。

四条硬目标：生成质量可审计不低于人工；能用确定性代码解决的不调 LLM 以控成本；满足保密 + 过程文档/レビュー留痕；支持企业级项目的外部系统对接（Salesforce、多云等）。

支持两种模式：**Greenfield**（从零开发）与 **Brownfield**（在客户已有代码库上迭代）。

## 2. 五条核心原则（最重要的架构知识）

1. **SQLite 是流程状态唯一真相源**。文件成果物是可审计输出，必须由 manifest 登记后才算提交；绝不用文件名/目录扫描推断流程状态。
2. **LLM 只做生成型/主观判断型工作**；凡可验证、可重复、有明确规则的工作全部下沉为确定性 **Skill**（不调 LLM）。质量门只消费成果物和结构化诊断，不依赖 LLM 自评。
3. **人工承認不可被 AI 替代**。AI 可生成レビュー草稿，但承認栏必须真人签字，通过 CLI `approve` 写入文档正式章节；未承認不能进入下一阶段。
4. **状态转换由 Orchestrator 统一在事务中提交**。Stage Agent 不得直接写 SQLite，Skill 不得直接改阶段状态。
5. **不确定或损坏时停止并给人工恢复路径**，不猜测、不自动删除、不用旧 checkpoint 猜测恢复。Brownfield 未知技术事实进 `unknowns`，不支持的质量门不得伪造通过。

## 3. 技术基座

采用 **Rust 原生编排核心**（workspace + `rusqlite` + `serde` + `clap`），**明确弃用 LangGraph/CrewAI/AutoGen**（ADR-001）。理由：编译型 CLI 低依赖、跨平台分发、稳定退出码、严格边界控制；状态机由声明式配置驱动，运行时校验器从同一数据源读取，不需要第二套图编排框架。LLM、MCP、Project Adapter 作为阶段插件接入，不改 Core 状态机。

执行形态：**CLI，无常驻服务**。状态持久化在项目目录 `.pipeline/state.db`（SQLite）+ 产物文件。默认顺序执行，`--parallel` 显式开启并发。

## 4. 流水线阶段图

```
需求输入 (+brownfield: 现状扫描 Skill)
  → [Index 生成 Agent(PM人格)] → 人工レビュー承認，冻结 Document Index
  → [架构设计 Agent] → 质量门①(结构完整性) → レビュー门①
  → [技术选型 Agent] → 质量门②(必选项覆盖) → レビュー门②  # 冻结云厂商/存储/Git私仓白名单
  → 并行: [Infra] [Frontend(UI专家)] [Backend(安全/性能专家)]
  → 质量门③(build/lint/typecheck 通过)
  → [Unit Test Agent] → 质量门④(覆盖率阈值)
  → [E2E Test Agent] → 质量门⑤(通过率/证据完整性)
  → レビュー门③(最终交付承認)
  → 最终报告 + 全部成果物
```

阶段-质量门映射（`stage_id` → 主要质量门）：`brownfield-scan`(只读/证据/敏感检查)、`index`(章节完整性→人工冻结)、`architecture`(结构/引用/图文一致→承認①)、`technology-selection`(必选项/许可证/EOL/供应商白名单→承認②)、`infra`(fmt/validate/secret scan)、`frontend`(build/lint/typecheck/accessibility)、`backend`(build/lint/typecheck/security scan)、`unit-test`(覆盖率阈值)、`e2e-test`(通过率/证据→承認③)。

失败处理：任一质量门默认最多重试 **3 次**，超过转 `manual_intervention`（`resume --manual-fix`）。参数错误、权限拒绝、脱敏失败、schema 错误**不得盲目重试**。

## 5. Agent 人格与模型路由

每个 LLM 节点绑定一个"专家人格"负责生成方向，是否达标由 Skill 校验，不靠 LLM 自评：

| 人格 | 阶段 | 关注点 | Skill 校验 |
|---|---|---|---|
| 高级产品经理 | Index/需求 | 边界、验收标准、非功能需求、"不做什么" | Index 章节完整性 |
| 高级开发技术专家 | 架构/选型/Infra/Backend | OWASP、越权/注入、性能(N+1/缓存/限流) | Semgrep/Bandit、性能基准 |
| 前端 UI 设计专家 | Frontend | 视觉层级、WCAG 无障碍、响应式 | axe-core、视觉回归 |
| QA 专家 | Unit/E2E | 用例完整性、边界覆盖 | 覆盖率、Playwright 报告 |

**模型路由**（借鉴 Agyn 论文）：推理型任务（需求/架构）用综合能力强的模型，实现型任务（Backend/Infra）用代码专用模型，失败重试的修复建议走对应角色模型，而非一个模型贯穿全程。

## 6. Skill 层与质量门

```
Agent 生成(LLM) → Skill 校验(确定性,不调LLM) → 通过则进下一阶段 / 不通过则带诊断打回重试
```

Skill 分两类：现成开源工具（eslint/ruff/mypy、pytest/jest、playwright、terraform validate、trivy/npm audit、markdownlint）+ 自定义 Skill（Index 章节完整性、架构与 mock 一致性、接口与后端字段对齐、覆盖率阈值）。

5 个质量门中 4 个以上为纯 Skill 自动判定；仅"技术选型是否真正适合业务"这类主观判断需 LLM 复核，且只喂结构化诊断结果、不重读原始文档，以控调用量。质量门统一契约：每个检查器输出 `check_id`、命令/版本、起止时间、退出码、摘要、证据路径、严重级别；默认 `error` 阻断、`warning` 记录不阻断；配置可提高阈值但**不得降低安全拦截项**。安全扫描/权限校验/secret scan 不允许用 `unsupported` 代替，不成立即转人工。

## 7. Document Index 驱动的文档体系

需求 → Index 生成 Agent 产出《Document Index》草稿 → 人工承認冻结为"文档模板契约" → 后续所有阶段文档由 Skill 对照 Index 校验章节完整性/顺序。**一旦冻结不可中途变更**（变更须走正式流程并留痕）。

每份交付文档固定四部分：**改訂履歴 / 正文(按 Index 章节) / レビュー記録 / 承認**。承認栏必须真人签字。

## 8. 保密与数据安全（面向日本客户的关键设计）

**脱敏层（Confidentiality Layer）**：夹在"Agent 生成内容"与"发送远程 LLM"之间的确定性 Skill，自身不调 LLM：

| 检测对象 | 工具 | 处理 |
|---|---|---|
| 通用 PII（邮箱/手机/证件/信用卡/IP） | Microsoft Presidio（本地开源） | 替换占位符 |
| 密钥/密码/服务器地址/连接串 | gitleaks / detect-secrets | 命中即硬拦截，本地占位，不允许半脱敏 |
| 客户名/项目代号 | 自定义 glossary（本地） | 用户登记映射表 |

**可逆令牌化**：真实内容 → 本地脱敏 → 占位符 → 发 LLM → 返回后本地映射表回填 → 写本地文件。映射表只存本地（可加密），不随 prompt 外发。

调用路径固定：`内容 → 本地扫描 → 令牌化 → policy decision → LLM Gateway → 本地回填 → artifact`，任一环失败都不发送。敏感度分级：`public` 用配置供应商；`confidential` 需批准的零数据保留(ZDR)供应商；`restricted` 默认只允许本地模型（Ollama/llama.cpp 逃生舱）。

**外部送信ログ**：LLM Gateway 每次调用生成 `call_id`，记录 provider/model、阶段、令牌数、耗时、脱敏摘要 hash、策略版本；**不记录**原始 prompt/response/令牌映射/客户秘密。汇总为审计成果物。

## 9. 外部系统对接（MCP 优先级）

优先级统一为：**官方 MCP Server > 社区 MCP（需额外安全审查）> 自建轻量 wrapper**。适用于测试平台（Salesforce Hosted MCP、Playwright MCP）和多云（AWS `awslabs/mcp`、Azure MCP、GCP MCP preview、Cloudflare Workers MCP；阿里云仅社区版需自建）。

- **IaC 统一层**用 Terraform/OpenTofu（HashiCorp 官方 MCP 生成/校验 HCL），云专属操作再叠加对应云官方 MCP。
- **文件存储**统一走 S3 兼容协议为公约数（S3/OSS/R2/GCS/MinIO 兼容，Azure Blob 例外需单独适配），代码用存储抽象接口（`fsspec`/`unstorage`）而非锁定厂商 SDK。

## 10. 仓库角色隔离（易错点）

两类仓库必须隔离凭证、工作目录、Git remote、审计和提交策略：

| 角色 | 含义 | 提交策略 |
|---|---|---|
| CLI Agent 源码仓库 | `pi-pipeline` 自身代码 | 按维护者授权和分支保护 |
| Pipeline 目标仓库 | `--repo` 指定的客户项目 | 按项目 Index 冻结的 host 白名单 |

**客户目标仓库禁止用 GitHub.com 或任何公网 SaaS Git 作 remote**——Skill 层在 `git push` 前校验 remote host 是否在冻结白名单内，不能靠 `--force`/环境变量绕过。白名单写入客户 Index 并冻结。人工"承認" = review 并 merge 对应 PR，PR comments 构成レビュー記録。CLI Agent 源码仓库不受此限。

## 11. Brownfield 三层适配架构

采用 **Core + Project Adapter + Tool Adapter**，不假设所有客户同栈：

| 层 | 固定内容 | 可替换 |
|---|---|---|
| Core | 状态机、checkpoint、manifest、审批、审计、脱敏 | 不可替换 |
| Project Adapter | 项目识别、目录规则、命令发现、构建/测试入口、文档模板 | 每客户独立 |
| Tool Adapter | Git、包管理器、编译器、lint、扫描器、浏览器、MCP | 按技术栈注册 |

适配器接口：`detect(repo_root)→StackProfile`、`plan(profile,stage)→CommandPlan`、`run(command_plan,sandbox)→ToolResult`、`collect(profile,result)→Evidence[]`。

**现状扫描 Skill** 只读客户代码，输出 `brownfield-inventory.json`（languages/frameworks/build_commands/datastores/interfaces/constraints/unknowns，每项带证据路径 + 置信度）。`StackProfile` 含语言、框架、包管理器、运行时版本、构建/测试命令、源码/生成目录、锁文件、部署方式、`allowed_tools`、`forbidden_operations`、`unknowns`。适配器声明能力矩阵，不支持的门返回 `unsupported` 并转人工，**不伪造通过**。栈适配矩阵覆盖 Python/Node/Java/Go/.NET/Ruby/PHP/Rust/Terraform/Salesforce，各自"识别证据 + 默认工具链 + 适配要点"。

变更边界：默认只在项目根内读写；先出适配计划和变更清单再生成代码；不借"修复环境"名义全量升级依赖；破坏性 DB 迁移/公共 API 变更/运行时升级/基础设施变更必须单独人工承認。

## 12. 模块边界（12 个模块）

CLI Adapter（解析/校验/打印/退出码）、Pipeline Orchestrator（按状态图调度）、Stage Agent（读输入调人格生成成果物）、Skill Runner（确定性检查产 GateResult）、State Store（SQLite 事务/checkpoint/锁）、Artifact Store（原子写 + manifest）、Confidentiality Layer（脱敏/出站判定）、LLM Gateway（模型路由/超时/调用摘要）、Review Manager（承認项/レビュー記録/冻结）、Project Adapter、Integration Adapter（Git/MCP/云白名单连接）。模块间只通过结构化契约通信；所有状态变更由 Orchestrator 事务提交。

## 13. Stage/Gate 契约

统一接口：`Stage.run(context: StageContext) -> StageResult`、`Gate.evaluate(result, context: GateContext) -> GateResult`。

- **StageContext**：`run_id, stage_id, attempt, mode, repository_root, stack_profile, document_index, frozen_decisions, approved_artifacts, config_snapshot, sensitivity_level, allowed_tools`。
- **StageResult**：`status(succeeded|failed|blocked)`、`artifact_ids[]`、`diagnostic_ids[]`、`next_action(continue|retry|await_approval|manual_intervention)`、`summary`。
- **GateResult**：`gate_id`、`status(passed|failed|skipped|unsupported)`、`checks[{check_id,status,severity,message,evidence_uri}]`、`attempt`、`evaluated_at`、`tool_versions`。

成果物写入后生成不可变 `artifact-manifest.json`（相对路径、SHA-256、大小、阶段、attempt、schema 版本）；相同 `artifact_id` 不覆盖，重试生成新 attempt。

## 14. 运行核心：状态机 / SQLite / Checkpoint

**Run 状态链**：`created → (scanning) → index_running → index_waiting_approval → architecture_* → technology_selection_* → parallel_running/parallel_blocked → quality_gate_3 → unit_test_running → quality_gate_4 → e2e_test_running → quality_gate_5 → final_waiting_approval → completed`；终止态 `cancelled / manual_intervention / failed`。**Stage 状态**：`pending → running → gate_pending → waiting_approval → succeeded`（旁路 `retry_scheduled` / `manual_intervention`）。合法边由状态图校验器拒绝非法转换；每次转换含 actor、reason、from、to、attempt、时间、event id。**状态转换和退出码的唯一事实源是 `phase-1-foundation.md`**，校验器、CLI `--help`、文档表格、测试从同一快照生成。

**SQLite 核心表**：`runs`、`stages`（含 `checkpoint_json`）、`attempts`、`gates`（`status ∈ passed/failed/skipped/unsupported`）、`artifacts`（UNIQUE(run_id,relative_path,attempt)）、`approvals`、`manifests`（`status ∈ prepared/committed/abandoned`）、`outbound_logs`、`events`（UNIQUE(run_id,sequence_no)）+ `schema_meta`。大段正文不进 SQLite，只存 URI/摘要/hash。启动顺序：取文件锁 → 事务读 `schema_meta` → 逐版本向前迁移记录 id+hash → 失败 rollback 保留原库返回 `STATE_CORRUPTED`，不自动降级或删未知表。

**事务边界**（一次 Stage 提交按序）：校验状态转换 → 校验 artifact 路径 → 验 manifest hash → upsert stage/attempt/gate/manifests/artifacts/approvals → append 恰好一条 event → 更新 run status → COMMIT。任一步失败整体 rollback；文件先写 attempt 临时目录，manifest 校验成功后同一事务登记为 committed。`.pipeline/events.jsonl` 若存在只能由 SQLite events 生成。

**并发锁**：`.pipeline/locks/run.lock`（run_id/pid/host/heartbeat）。同一目标项目只允许一个 active run，靠 `runs` 查询 + 数据库 `one_active_run_per_repo` partial unique index 双重保证（业务查询给友好错误，约束负责最终互斥）。发现有效锁立即冲突返回，不杀已有进程；过期锁不自动接管，只允许 `resume --manual-fix`。

**Checkpoint 与恢复**：checkpoint 记 `run_id/stage_id/attempt/input_hash/config_hash/stack_profile_hash/approved_artifact_ids/next_action`。恢复前校验：repo root 一致、config hash 未变、frozen decisions 与 StackProfile hash 未变（或有批准变更）、manifest 文件仍存在且 hash 一致、无另一有效锁。校验失败明确报错，不从旧 checkpoint 猜测。提交粒度是 stage attempt manifest；重试必须新建 attempt，旧 manifest 只能标 abandoned 不覆盖。

## 15. CLI 契约与退出码

```
pi-pipeline init [--mode greenfield|brownfield] [--repo PATH]
pi-pipeline run --requirement TEXT [--mode ...] [--repo PATH] [--parallel]
pi-pipeline resume [--run RUN_ID] [--manual-fix]
pi-pipeline status [--run RUN_ID] [--json]
pi-pipeline approve/reject STAGE --role ROLE --reviewer NAME --comment TEXT
pi-pipeline skip-gate GATE --reviewer NAME --reason TEXT
pi-pipeline artifacts [--run RUN_ID] [--stage STAGE]
pi-pipeline scan [--repo PATH] [--output RELATIVE_PATH]
```

**退出码（固定）**：`0` 成功、`2` 参数/配置错误、`3` 质量门失败、`4` 等待人工承認、`5` 安全策略拦截(`SECURITY_BLOCKED`)、`6` 外部依赖不可用(`DEPENDENCY_UNAVAILABLE`)、`7` 状态/成果物损坏(`STATE_CORRUPTED`)、`8` 内部错误。`status --json` 只从 SQLite 返回机器可读结果，stdout 不混入模型/工具日志。配置优先级：命令行参数 > 项目配置 > 安全默认值；加载后算 `config_hash` 随 run 冻结，API key 不进项目配置。

## 16. 安全默认值与权限控制

- CLI 只读项目外路径；写入必须在项目根或 `--repo` 根内。拒绝 `../` 逃逸、未授权命令、未批准远程 URL、危险 shell 参数。
- 工具执行用 argv 数组 + 固定 cwd + 环境变量 allowlist + timeout；禁止动态拼命令，禁止未批准的 `curl|sh`/安装脚本/真实 Terraform apply/破坏性 DB 操作。
- 需求文本只是数据，不得解释为 shell 命令/路径/权限。
- 外部命令 stdout/stderr 先写受控日志再 secret redact 再生成 evidence；错误消息/manifest/外部日志/提交包不得出现 API key/Cookie/Authorization/脱敏映射值/客户秘密。审计事件 append-only。

## 17. 测试策略

- **单元**：状态转换、重试预算、配置优先级、路径校验、脱敏规则、退出码。
- **集成**：SQLite checkpoint、断点续跑、artifact manifest、Project/Tool adapter fixture。
- **安全**：越权路径、remote 白名单、secret hard-block、日志脱敏、恶意输入与工具参数注入。
- **端到端**：`run → approve → resume → 最终报告`，含 gate 失败重试和人工跳过；noop stage 跑通 `init→run→status→kill -9→resume→approve→artifacts --verify`。

夹具不得含真实客户数据/凭证/公网 push 地址。每个质量门必须有一个可复现的通过样例和一个能阻断流程的失败样例。

## 18. 关键决策与验收要点速记

- ADR-001：LangGraph+SQLite checkpointer → **Rust 原生 Orchestrator + SQLite StateStore**；文档实现不得再以 LangGraph 为前提。
- 唯一事实源纪律：状态转换/退出码只有 `phase-1-foundation.md` 一处声明；Kill-9 后锁不自动接管、临时目录标 abandoned、旧 attempt 保留、manifest 无半条 committed。
- MVP 明确不做：全量语言/框架适配、多人共享远程状态、云生产自动部署、自动替代真人审批/绕过质量门、Web 管理后台。

---

> 以上 §1–§18 是**设计层**知识（来自 docs 分片）。以下 §19–§24 是**实现层**知识，从 `crates/pi-pipeline` 真实源码抽取，记录 Phase 1 实际落地的具体架构；设计与实现存在差距处已标注。

## 19. Crate 结构与依赖（实现事实）

单 crate `pi-pipeline` v0.1.0（edition 2021），单二进制 `src/main.rs`。依赖精简：`clap 4.5`(derive)、`rusqlite 0.32`(bundled，自带 SQLite)、`serde`/`serde_json`、`sha2`、`chrono`、`uuid`(v4)；dev 依赖 `libc`、`tempfile`。**无 async 运行时、无 LLM SDK、无网络库**——Phase 1 完全确定性、离线。

模块划分（`src/*.rs`）：

| 模块 | 职责 | 关键类型 |
|---|---|---|
| `main.rs` | clap CLI、命令分派、退出码映射 | `Cli`/`Command`/各 `*Args`、`CliError` |
| `foundation.rs` | 声明式状态机加载/校验/转换、退出码枚举 | `Foundation`、`TransitionSpec`、`ExitCode`、`apply_transition`、`guard_passes` |
| `store.rs` | SQLite StateStore、schema、全部事务 | `StateStore`、`GateRecord`、`ApprovalRecord`、`StageCompletion` |
| `artifact.rs` | manifest 生成、原子提交、校验、路径安全 | `Manifest`、`ArtifactEntry`、`ArtifactStore` |
| `orchestrator.rs` | Stage/Gate trait 抽象 + noop 实现 | `Stage`/`Gate` trait、`NoopStage`、`ManifestGate`、`StageContext`/`StageResult`/`GateResult` |
| `stack.rs` | Brownfield 只读扫描 | `StackProfile`、`Fact`、`CommandSpec`、`Unknown`、`BrownfieldInventory`、`scan_repo` |
| `lock.rs` | run 锁文件 | `RunLock`（`Drop` 自动 release） |

## 20. 声明式状态机（实现事实）

状态机是 `config/phase-1-foundation.json`，通过 `include_str!` **编译进二进制**（`FOUNDATION_JSON`）。这就是 docs 反复强调的"唯一事实源"的物理落点。

- `run` 状态 20 个、`stage` 状态 8 个（`pending/running/gate_pending/waiting_approval/retry_scheduled/succeeded/manual_intervention/failed`）。
- 实际只声明了 **14 条 transition**，且真正连通的主链只到 `architecture_running`；`parallel_running`/`final_waiting_approval` 等只有零星占位边，quality_gate/unit_test/e2e 阶段**没有任何 transition**。
- 退出码 enum `#[repr(i32)]`：`0 OK`/`2 INVALID_ARGUMENT`/`3 QUALITY_GATE_FAILED`/`4 WAITING_APPROVAL`/`5 SECURITY_BLOCKED`/`6 DEPENDENCY_UNAVAILABLE`(唯一 retryable)/`7 STATE_CORRUPTED`/`8 INTERNAL_ERROR`。
- `validate_source()` 启动时交叉校验：每条 transition 的 from/to 必须是已声明状态，guard 必须在 `KNOWN_GUARDS`(13 个) 内，否则拒绝。
- 转换求值 `apply_transition(source, event, context)`：查匹配边 → 跑 `guard_passes` → 返回目标状态。**guard 是对一个 `HashMap<&str,String>` 上下文做字符串等值判断**（如 `mode_is_greenfield`、`gate_1_passed=="true"`、`attempts_below_limit` 比较 `attempt`<`max_attempts`）。较复杂的 `approval_is_valid_for_index` 需同时满足 4 个键：`approval_stage=="index"` ∧ `approval_gate_status=="passed"` ∧ `approval_manifest_exists=="true"` ∧ `approval_role_allowed=="true"`；`manual_fix_recorded_and_lock_owned` 需 `manual_fix_recorded ∧ lock_owned`。

## 21. SQLite 实现细节（实现事实）

`StateStore::open` 固定 `PRAGMA foreign_keys = ON; PRAGMA journal_mode = WAL;`。`initialize()` 用 `CREATE TABLE IF NOT EXISTS` 建全部表 + `INSERT OR IGNORE INTO schema_meta VALUES(1,...)`。

**关键差距（设计 vs 实现）**：

- `runs.status` 的 CHECK 约束**只允许** `created/scanning/index_running/index_waiting_approval/architecture_running/completed/cancelled/manual_intervention/failed` —— 即数据库层面**根本无法写入** `parallel_running`/`quality_gate_*`/`unit_test_running`/`e2e_test_running`/`final_waiting_approval`。**Phase 1 只实现到 architecture_running**，后段流水线是设计而非代码。
- `schema_meta` 只有单版本 1、`INSERT OR IGNORE`；**没有真正的逐版本迁移引擎**（runtime-core.md §3.1 描述的迁移链尚未实现）。
- 表约束比 docs 更硬：`manifests` 有 `CHECK(committed_count<=required_count)`，`attempts.status ∈ running/succeeded/abandoned/failed`（与 stage 状态不同），`events.sequence_no>0` 且 `UNIQUE(run_id,sequence_no)`。
- `one_active_run_per_repo` partial unique index **已真实建立**：`ON runs(repo_root) WHERE status NOT IN ('completed','cancelled','failed')`，配合 `active_run_for_repo()` 业务查询双保险。

## 22. 事务与事件日志（实现事实）

所有状态变更都在 `store.rs` 的一个 `conn.transaction()` 内完成，并**追加事件**，`sequence_no` 通过 `SELECT COALESCE(MAX(sequence_no),0)+1` 单调生成：

| 方法 | 作用 | 写入的表/事件 |
|---|---|---|
| `create_run_with_stage` | 建 run + 首个 stage(pending) | runs, stages, `run.created`(seq 1) |
| `start_attempt` | attempt=MAX+1，stage→running | stages, attempts, `stage.started` |
| `complete_stage` | gate 落库 + attempt→succeeded + stage→waiting_approval + run→next_state | gates, attempts, stages, runs, `stage.waiting_approval` |
| `resume_interrupted` | 旧 attempt→abandoned(`PROCESS_INTERRUPTED`)、stage→pending | attempts, stages, runs, `stage.abandoned`+`stage.resumed`(两条事件) |
| `cancel_run` | running attempt→abandoned(`RUN_CANCELLED`)、未终态 stage→failed、run→cancelled | attempts, stages, runs, `run.cancelled` |
| `advance_run` | 仅推进 run 状态 + 事件 | runs, 自定义 event_type |

体现了 docs 的核心不变量：**重试不覆盖**（旧 attempt 标 abandoned，attempt 号 +1 新建）、**每次转换恰好一条以上事件、actor 显式**（`cli`/`noop`/`resume`/传入 actor）。

## 23. 成果物原子提交（实现事实）

`ArtifactStore::commit`（Phase 1 只处理 `noop.txt`）的实际提交顺序：

1. 读 attempt 临时目录里的产物，算 `sha256`，组 `ArtifactEntry`。
2. 对**未签名 manifest JSON** 算 `manifest_sha256`（内容指纹）。
3. `fs::rename(临时目录 → 最终 artifacts 目录)` **原子移动**；若最终目录已存在直接报错 `"attempt already committed"`（防重复提交）。
4. 写 pretty manifest JSON 到 `manifests/.../attempt-<n>.json`。
5. **单个 DB 事务**插入 `manifests`(status='committed', required=1, committed=1) + `artifacts`。

即"**先落文件、再登记数据库**"，文件写入不依赖 DB 事务，与 runtime-core.md §3.3 一致。路径安全由 `validate_component`（校验 run_id/stage/attempt 段）+ `checked_path`（用 `Path::Component` 逐段检查，拒绝 `..` 逃逸）保证；证据文件上限 `MAX_EVIDENCE_BYTES = 8 MiB`。`verify_detailed` 逐文件重算 hash 比对 manifest，支撑 `artifacts --verify`。

## 24. Orchestrator 抽象、锁、CLI（实现事实）

**trait 抽象**（`orchestrator.rs`）：`Stage{ id(); execute(ctx, artifacts)->StageResult }`、`Gate{ evaluate(&Manifest)->GateResult }`。Phase 1 只有 `NoopStage`（sleep 后写 `noop.txt`）和 `ManifestGate`（`REQUIRED_ROLE="product-owner"`）。这是未来接 LLM Stage/真实质量门的插件点——Core 不变，Stage/Gate 可替换。

**锁**（`lock.rs`）：`RunLock` 用 `OpenOptions::create_new(true)` 独占创建 `.pipeline/locks/run.lock`（内含 run_id/pid/lock_id）；存在有效锁且非 `--manual-fix` 直接报错，不杀进程；`Drop` 自动 `release`（kill-9 时进程被杀、文件残留，故 `resume --manual-fix` 才能接管，与 kill-9 恢复语义吻合）。

**CLI**（`main.rs`）：全局参数 `--repo`(默认`.`)/`--run`/`--json`。子命令**实际实现 8 个**：`init`/`run`/`resume`/`status`/`approve`/`scan`/`artifacts`/`cancel`。

- 差距：docs CLI 契约里的 `reject`、`skip-gate` **尚未实现**。
- `run` Phase 1 是 noop 驱动：`--stage` 默认 `noop`、`--sleep-seconds`（`parse_sleep_seconds` 限定有限值 0..=3600）、`--mode`。
- `CliError{code: ExitCode, ...}` 统一把错误映射到 §20 的退出码。

**Brownfield 扫描实现**：`scan_repo` 是纯确定性的**根目录文件证据探测**（`matching_root_files` 按扩展名/文件名匹配 `Cargo.toml`/`package.json`/`pyproject.toml` 等），产出 `StackProfile{ languages/frameworks/package_managers: Vec<Fact>, commands: BTreeMap<String,CommandSpec>, forbidden_operations, unknowns, evidence_hash }`。`Fact{name,version,confidence,evidence}`、`CommandSpec{value,evidence,network}`、`Unknown{path,reason,impact}` —— 每条事实带证据路径与置信度，无法确认的进 `unknowns`，与设计的"事实边界"一致。
