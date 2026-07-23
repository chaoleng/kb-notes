---
version: 1
id: rag-concept-reranker
title: 概念：重排序器（Reranker）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 对初步召回的候选片段重新计算相关性并排序的组件。
created: 2026-07-23T05:22:29.699Z
updated: 2026-07-23T05:22:29.699Z
favorite: false
related:
  - rag-concepts
---

## 定义
Reranker 在初步召回后，对“查询—候选片段”成对判断相关性，把最有用的证据排到前面。

## 为什么需要
向量检索通常追求低延迟和较大召回量，结果中可能混入语义相近但不能回答问题的片段，重排序可进一步筛选。

## 代价
重排序通常比简单向量距离更耗时，应限制候选数量，并通过离线评估确定收益是否值得成本。