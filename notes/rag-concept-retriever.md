---
version: 1
id: rag-concept-retriever
title: 概念：检索器（Retriever）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 根据用户查询从知识库中召回候选片段的组件。
created: 2026-07-23T05:22:27.110Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concepts
  - rag-retriever-lexical-vector
  - rag-retriever-hybrid
  - rag-retriever-recall-metrics
  - rag-retrieval
---

## 定义
Retriever 接受查询，返回若干可能包含答案的文档片段及其相关性分数。

## 类型
向量检索适合语义匹配，关键词检索适合精确术语，结构化过滤适合版本、时间和权限；实际系统经常组合使用。

## 关键指标
召回率、Precision、Recall@K、命中排名、延迟和权限正确性。

## 误区
检索器只负责找候选，不负责最终回答；如果候选不相关，后续模型再强也可能被错误上下文带偏。

## 详细分支
- [关键词检索与向量检索](note://rag-retriever-lexical-vector)：BM25 等关键词检索擅长精确术语，向量检索擅长语义相近表达。
- [混合检索](note://rag-retriever-hybrid)：通过结果融合或加权组合关键词、向量和结构化过滤，兼顾精确匹配与语义匹配。
- [召回质量指标](note://rag-retriever-recall-metrics)：Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。