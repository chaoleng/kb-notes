---
version: 1
id: ai-dev-document-index
title: Document Index 驱动的文档体系与人工承認
tags:
  - Agent
  - Pipeline
  - 质量门
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: Index 经人工承認后冻结为文档模板契约，后续所有交付文档按它校验章节并留签字痕迹。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# Document Index 驱动的文档体系与人工承認

> Index 经人工承認后冻结为文档模板契约，后续所有交付文档按它校验章节并留签字痕迹。

## 从需求到冻结

需求文本进来先由 Index 生成 Agent 产出《Document Index》草稿，列出后续每份交付文档该有哪些章节、按什么顺序排列。草稿经人工承認后冻结成“文档模板契约”，此后不可中途变更；确有必要修改时须走正式变更流程并留下记录，而不是直接改文件。冻结这一步是整条流水线唯一一次“先定标准、再产内容”的机会，放过了后面每个阶段都会各写各的。

## 四段式交付文档

每份文档固定四部分：改訂履歴、正文（严格按 Index 的章节展开）、レビュー記録、承認。前两部分可以由 Agent 生成，レビュー記録记录评审意见与处理结果，承認栏必须真人签字，日本客户交付场景里这一栏就是责任归属的凭据。

## Index 如何被消费

冻结后的 Index 变成结构化输入，随 StageContext 的 `document_index` 字段传给每个阶段，Skill 拿它逐份比对章节完整性与顺序，缺章、错序、擅自加章节都会被判失败并打回重写。因此 Index 既是文档模板，也是 `index` 阶段之后所有文档类质量门的判定依据，字段流转见 [阶段图与契约](note://ai-dev-stage-graph)。

## 承認的落库形态

承認不是在文档里手写一行字了事：CLI 侧的 approve 命令带角色、审查人与意见，写进 `approvals` 表并触发阶段状态转换，状态机的守卫会同时检查阶段名、门状态、manifest 存在性与角色是否被允许，四项都成立才放行，具体判据见 [运行核心](note://ai-dev-runtime-state-machine)。这样“谁在什么时候批准了哪一版产物”可以从数据库直接查出来，而不是靠翻文档历史。
