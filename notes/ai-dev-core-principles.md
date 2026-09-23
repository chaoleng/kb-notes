---
version: 1
id: ai-dev-core-principles
title: AI 开发 Agent Pipeline：五条核心原则
tags:
  - Agent
  - 架构
  - 质量门
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 五条原则界定了状态真相源、LLM 与 Skill 的分工、人工承認的地位以及异常时的停机方式。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# AI 开发 Agent Pipeline：五条核心原则

> 五条原则界定了状态真相源、LLM 与 Skill 的分工、人工承認的地位以及异常时的停机方式。

## 状态只有一个真相源

流程状态全部落在项目目录下的 `.pipeline/state.db`，文件成果物只是可审计输出，必须由 manifest 登记之后才算提交。任何组件都不许靠扫描目录名、文件名去推断“跑到哪一步了”：中断留下的临时目录和半写文件会让这种推断与真实进度分叉，而分叉之后没有任何办法判定哪一边为准。

## 能验证的工作不交给 LLM

规则明确、结果可重复的工作一律下沉成确定性 Skill，不发起模型调用；模型只留在生成型和主观判断型节点上。质量门消费的是成果物和结构化诊断，不接受模型自评式的“我认为达标”。这同时是成本约束：用代码就能算出结论的部分不该进 token 账单。

## 人工承認不可被替代

AI 可以起草レビュー内容，但承認栏必须真人签字，经 CLI `approve` 写入文档正式章节；缺承認记录的阶段不允许向后推进，冻结与签字流程见 [Document Index 体系](note://ai-dev-document-index)。

## 转换归口与停机纪律

状态转换统一由 Orchestrator 在事务中提交：Stage Agent 不直接写库，Skill 不直接改阶段状态，越权写入等于绕开事件日志。遇到不确定或疑似损坏就停机并留出人工恢复路径——不猜测、不自动删除、不拿旧 checkpoint 反推现场。Brownfield 场景下核实不了的技术事实写进 `unknowns`，适配层覆盖不到的质量门也不能包装成通过。
