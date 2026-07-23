---
version: 1
id: rag-citation-grounding
title: RAG：引用与事实依据
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 让回答中的关键结论能够回溯到检索片段和原始文档，提升可验证性。
created: 2026-07-23T04:42:39.918Z
updated: 2026-07-23T04:42:39.918Z
favorite: false
related:
  - rag-generation
---

## Grounding
每个关键结论都应能在检索证据中找到支持；证据没有覆盖的内容应明确标记为推断或未知。

## 引用设计
引用应包含文档标题、章节、URL 或片段定位，而不是只给一个模糊来源。

## 检查
可用规则或模型检查“结论—证据”是否匹配，重点发现引用错位、过度推断和互相矛盾的资料。