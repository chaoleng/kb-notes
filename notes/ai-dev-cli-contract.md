---
version: 1
id: ai-dev-cli-contract
title: CLI 契约、退出码与 Crate 结构
tags:
  - CLI
  - Rust
  - 架构
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 子命令与固定退出码构成对外契约，单 crate 的模块划分和 trait 抽象决定后续能替换什么。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# CLI 契约、退出码与 Crate 结构

> 子命令与固定退出码构成对外契约，单 crate 的模块划分和 trait 抽象决定后续能替换什么。

## 子命令

设计中的命令面是 `init [--mode greenfield|brownfield] [--repo PATH]`、`run --requirement TEXT [--parallel]`、`resume [--run RUN_ID] [--manual-fix]`、`status [--run RUN_ID] [--json]`、`approve/reject STAGE --role ROLE --reviewer NAME --comment TEXT`、`skip-gate GATE --reviewer NAME --reason TEXT`、`artifacts [--stage STAGE]`、`scan [--repo PATH] [--output RELATIVE_PATH]`。实际落地八个：init、run、resume、status、approve、scan、artifacts、cancel，`reject` 与 `skip-gate` 还没实现。全局参数是 `--repo`（默认 `.`）、`--run`、`--json`。Phase 1 的 `run` 由 noop 驱动，`--stage` 默认 `noop`，`--sleep-seconds` 经 `parse_sleep_seconds` 限定在 0..=3600。`status --json` 只从数据库读机器可读结果，stdout 不混入模型或工具日志。配置优先级是命令行参数高于项目配置、项目配置高于安全默认值，加载后算出 `config_hash` 随 run 冻结，API key 不进项目配置。

## 退出码

`#[repr(i32)]` 的枚举把错误收敛成固定数值：`0 OK`、`2 INVALID_ARGUMENT`（参数或配置错误）、`3 QUALITY_GATE_FAILED`、`4 WAITING_APPROVAL`、`5 SECURITY_BLOCKED`、`6 DEPENDENCY_UNAVAILABLE`（唯一标记为 retryable 的一项）、`7 STATE_CORRUPTED`、`8 INTERNAL_ERROR`。`CliError{code: ExitCode, ...}` 负责把内部错误统一映射过去，调用方脚本据此判断是重跑、等人批、还是必须停下来查。

## Crate 与模块

单 crate `pi-pipeline` v0.1.0（edition 2021），单二进制入口 `src/main.rs`。依赖只有 clap 4.5（derive）、rusqlite 0.32（bundled）、serde 与 serde_json、sha2、chrono、uuid v4，dev 依赖 libc 和 tempfile；没有 async 运行时、没有 LLM SDK、没有网络库，Phase 1 完全离线且确定性。

| 模块 | 职责 | 关键类型 |
|---|---|---|
| `main.rs` | CLI 解析、命令分派、退出码映射 | `Cli`、`Command`、`CliError` |
| `foundation.rs` | 状态机加载、校验、转换求值 | `Foundation`、`TransitionSpec`、`ExitCode` |
| `store.rs` | StateStore、schema 与全部事务 | `StateStore`、`GateRecord`、`StageCompletion` |
| `artifact.rs` | manifest 生成、原子提交、路径安全 | `Manifest`、`ArtifactEntry`、`ArtifactStore` |
| `orchestrator.rs` | Stage/Gate 抽象与 noop 实现 | `Stage`、`Gate`、`NoopStage`、`ManifestGate` |
| `stack.rs` | 只读栈扫描 | `StackProfile`、`Fact`、`CommandSpec`、`Unknown` |
| `lock.rs` | run 锁文件 | `RunLock` |

## 插件点与锁实现

`Stage{ id(); execute(ctx, artifacts)->StageResult }` 和 `Gate{ evaluate(&Manifest)->GateResult }` 就是未来接真实 LLM 阶段和真实质量门的插入位置：Core 不动，两个 trait 的实现可换。当前只有 `NoopStage`（睡一会儿写出 `noop.txt`）和 `ManifestGate`（`REQUIRED_ROLE="product-owner"`）。`RunLock` 用 `OpenOptions::create_new(true)` 独占创建 `.pipeline/locks/run.lock`，文件内含 run_id、pid、lock_id，`Drop` 时自动释放；进程被 kill -9 时锁文件会残留，所以只有 `resume --manual-fix` 能接管，这与断电恢复语义正好吻合。栈扫描侧的 `scan_repo` 是纯根目录文件证据探测，`matching_root_files` 按 `Cargo.toml`、`package.json`、`pyproject.toml` 这类特征文件匹配，产出的每条 `Fact` 都带证据路径和置信度，判不准的进 `unknowns`。
