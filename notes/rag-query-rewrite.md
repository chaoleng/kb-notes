---
version: 1
id: rag-query-rewrite
title: RAG：查询改写与问题拆分
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把自然语言问题改造成更适合检索的一个或多个查询，同时保留原始意图。
created: 2026-07-23T04:42:14.733Z
updated: 2026-07-23T04:42:14.733Z
favorite: false
related:
  - rag-question-understanding
---

## 作用
查询改写解决“用户会问，但知识库不一定按这种说法存储”的问题。复杂问题可以拆成多个子问题，分别检索后再合并。

## 典型策略
- 补全省略的主语、产品名、时间范围。
- 为专业术语生成同义词和别名。
- 将比较题、因果题拆成可验证的子问题。
- 保留原问题用于最终回答，改写结果只服务于检索。

## 风险
必须避免凭空添加事实；改写结果应可追溯到原问题。