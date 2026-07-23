---
version: 1
id: rag-reranker-evaluation
title: 重排序器（Reranker）：重排序评估
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 比较重排前后的正确证据排名和最终答案质量，判断重排是否真的带来收益。
created: 2026-07-23T11:56:05.776Z
updated: 2026-07-23T11:56:05.776Z
favorite: false
related:
  - rag-concept-reranker
---

# 重排序器（Reranker）：重排序评估

> 比较重排前后的正确证据排名和最终答案质量，判断重排是否真的带来收益。

## 核心细节
不能只看排序分数；应观察 Recall@K、MRR、答案忠实度、延迟和成本的整体变化。

## 所属模块
[重排序器（Reranker）](note://rag-concept-reranker)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。