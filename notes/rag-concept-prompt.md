---
version: 1
id: rag-concept-prompt
title: 概念：Prompt（提示词）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 用于约束模型角色、输入格式、证据使用方式和输出格式的指令模板。
created: 2026-07-23T05:22:32.189Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concepts
  - rag-prompt-template
  - rag-prompt-context-assembly
  - rag-prompt-injection-defense
  - rag-generation
---

## 定义
Prompt 是发送给模型的指令与上下文结构。在 RAG 中，它通常包含系统规则、用户问题、检索证据、引用要求和输出格式。

## 作用
告诉模型如何使用证据、证据不足时如何回答、如何区分事实与推断，以及如何返回引用。

## 误区
Prompt 不能修复缺失或错误的知识；过度堆叠规则也会增加冲突。外部文档中的指令应被视为数据，不能覆盖系统级约束。

## 详细分支
- [Prompt 模板结构](note://rag-prompt-template)：把角色规则、用户问题、检索证据、引用要求和输出格式分成清晰区块。
- [上下文组装](note://rag-prompt-context-assembly)：按照相关性、来源可信度、时间和互补性排列片段，并控制总 token 预算。
- [Prompt 注入防护](note://rag-prompt-injection-defense)：把外部文档当作数据而不是指令，限制工具调用和敏感信息输出。