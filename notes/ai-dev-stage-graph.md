---
version: 1
id: ai-dev-stage-graph
title: 流水线阶段图与 Stage/Gate 契约
tags:
  - Pipeline
  - 架构
  - 质量门
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 从需求输入到最终承認的阶段链路、每个阶段挂载的质量门，以及重试预算的硬边界。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# 流水线阶段图与 Stage/Gate 契约

> 从需求输入到最终承認的阶段链路、每个阶段挂载的质量门，以及重试预算的硬边界。

## 链路形状

```
需求输入（brownfield 先跑现状扫描 Skill）
  → Index 生成（PM 人格）→ 承認后冻结 Document Index
  → 架构设计 → 质量门①结构完整性 → レビュー门①
  → 技术选型 → 质量门②必选项覆盖 → レビュー门②
  → 并行：Infra / Frontend / Backend
  → 质量门③ build + lint + typecheck
  → 单元测试 → 质量门④覆盖率阈值
  → E2E 测试 → 质量门⑤通过率与证据完整性
  → レビュー门③最终交付承認 → 最终报告与全部成果物
```

技术选型那一门通过时会顺带冻结云厂商、存储方案与 Git 私仓白名单。默认串行执行，只有加 `--parallel` 才打开中间那段并发。

## stage_id 与主检查项

| stage_id | 主要质量门 |
|---|---|
| `brownfield-scan` | 只读性、证据齐备、敏感信息检查 |
| `index` | 章节完整性，随后人工冻结 |
| `architecture` | 结构、引用、图文一致 |
| `technology-selection` | 必选项、许可证、EOL、供应商白名单 |
| `infra` | fmt、validate、secret scan |
| `frontend` | build、lint、typecheck、accessibility |
| `backend` | build、lint、typecheck、security scan |
| `unit-test` | 覆盖率阈值 |
| `e2e-test` | 通过率与证据 |

## 接口与成果物契约

统一签名是 `Stage.run(context: StageContext) -> StageResult` 与 `Gate.evaluate(result, context: GateContext) -> GateResult`。StageContext 携带 `run_id`、`stage_id`、`attempt`、`mode`、`repository_root`、`stack_profile`、`document_index`、`frozen_decisions`、`approved_artifacts`、`config_snapshot`、`sensitivity_level`、`allowed_tools`。StageResult 返回 `status`（succeeded / failed / blocked）、`artifact_ids[]`、`diagnostic_ids[]`、`next_action`（continue / retry / await_approval / manual_intervention）和 summary。GateResult 返回 `gate_id`、`status`（passed / failed / skipped / unsupported）、`checks[{check_id,status,severity,message,evidence_uri}]`、`attempt`、`evaluated_at`、`tool_versions`。产物写盘后生成不可变的 `artifact-manifest.json`，登记相对路径、SHA-256、大小、阶段、attempt 与 schema 版本；同一 `artifact_id` 不覆盖，重试只会开新 attempt。

## 重试预算

任一质量门失败默认最多重试 3 次，超预算转 `manual_intervention`，之后只能由 `resume --manual-fix` 接手。参数错误、权限拒绝、脱敏失败、schema 错误属于确定性故障，重跑必然复现同一结果，因此禁止进入重试循环，直接停下报错。落库细节见 [运行核心](note://ai-dev-runtime-state-machine)。
