---
version: 1
id: rag-context-prompt
title: RAG：上下文拼接与 Prompt
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 将多个检索片段按相关性、来源和长度限制组织成模型可用的上下文。
created: 2026-07-23T04:42:37.624Z
updated: 2026-07-23T04:42:37.624Z
favorite: false
related:
  - rag-generation
---

## 拼接原则
- 先放最相关、最能直接回答问题的证据。
- 保留标题、来源和时间等定位信息。
- 去除重复片段，避免同一事实占满上下文。
- 超出窗口时优先保留高分且互补的证据。

## Prompt 约束
区分系统规则、用户问题和外部资料；要求模型标注无法从资料得出的部分；防止文档内容覆盖更高优先级指令。