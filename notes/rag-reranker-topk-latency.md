---
version: 1
id: rag-reranker-topk-latency
title: 重排序器（Reranker）：Top-K、延迟与上下文预算
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 候选数量、重排数量和最终保留数量共同决定质量、延迟和模型上下文成本。
created: 2026-07-23T11:56:03.360Z
updated: 2026-07-23T11:56:03.360Z
favorite: false
related:
  - rag-concept-reranker
---

# 重排序器（Reranker）：Top-K、延迟与上下文预算

> 候选数量、重排数量和最终保留数量共同决定质量、延迟和模型上下文成本。

## 核心细节
可以先扩大召回，再限制重排输入，最后保留少量互补证据；所有阈值都应有离线和线上指标支撑。

## 所属模块
[重排序器（Reranker）](note://rag-concept-reranker)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。