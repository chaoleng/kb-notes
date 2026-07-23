---
version: 1
id: rag-retriever-recall-metrics
title: 检索器（Retriever）：召回质量指标
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。
created: 2026-07-23T11:55:58.657Z
updated: 2026-07-23T11:55:58.657Z
favorite: false
related:
  - rag-concept-retriever
---

# 检索器（Retriever）：召回质量指标

> Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。

## 核心细节
先建立带参考证据的问题集，再区分“没召回”“召回但排名靠后”和“证据本身不完整”，否则难以定位问题。

## 所属模块
[检索器（Retriever）](note://rag-concept-retriever)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。