---
version: 1
id: ai-dev-skill-quality-gate
title: Skill 层与质量门契约
tags:
  - 质量门
  - Agent
  - 安全
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 确定性 Skill 负责判定成败，质量门按统一字段输出诊断，安全类检查不许降级。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# Skill 层与质量门契约

> 确定性 Skill 负责判定成败，质量门按统一字段输出诊断，安全类检查不许降级。

## 回路与两类 Skill

一圈的形状是：Agent 用 LLM 生成 → Skill 做确定性校验 → 达标进入下一阶段，不达标带着诊断打回重试。Skill 分两类。现成开源工具占多数：eslint、ruff、mypy、pytest、jest、playwright、terraform validate、trivy、npm audit、markdownlint。自定义 Skill 补业务语义那一块：Index 章节完整性、架构文档与 mock 的一致性、前端接口与后端字段对齐、覆盖率阈值判定。

## 谁来判定

五个质量门里四个以上是纯 Skill 自动裁决。唯一需要 LLM 复核的是“这套技术选型是否真的匹配业务”这类主观命题，而且只把结构化诊断结果喂回模型，不让它重读原始文档，目的是把调用量压在可预测的范围内。

## 统一输出契约

每个检查器必须吐出同一组字段：`check_id`、执行的命令与工具版本、起止时间、退出码、摘要、证据路径、严重级别。默认 `error` 阻断流程、`warning` 只记录；项目配置可以把阈值调严，但不得调松任何安全拦截项。安全扫描、权限校验、secret scan 三类检查不允许用 `unsupported` 搪塞，一旦跑不起来就转人工处理。

## 测试策略与夹具

单元测试覆盖状态转换、重试预算、配置优先级、路径校验、脱敏规则与退出码；集成测试覆盖 SQLite checkpoint、断点续跑、artifact manifest 以及 Project/Tool adapter 的 fixture；安全测试针对越权路径、remote 白名单、secret 硬拦截、日志脱敏和工具参数注入；端到端测试跑通 `run → approve → resume → 最终报告`，含门失败重试与人工跳过分支。硬性要求是每个质量门都配一个可复现的通过样例和一个能真正阻断流程的失败样例，夹具里不得出现真实客户数据、凭证或公网 push 地址。
