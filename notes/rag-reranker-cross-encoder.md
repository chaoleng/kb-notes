---
version: 1
id: rag-reranker-cross-encoder
title: 重排序器（Reranker）：Cross-Encoder 重排序
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 让模型同时读取查询和候选片段，直接判断二者的相关性。
created: 2026-07-23T11:56:00.953Z
updated: 2026-07-23T11:56:00.953Z
favorite: false
related:
  - rag-concept-reranker
---

# 重排序器（Reranker）：Cross-Encoder 重排序

> 让模型同时读取查询和候选片段，直接判断二者的相关性。

## 核心细节
Cross-Encoder 通常比向量距离更精确但更慢，适合对有限候选集做第二阶段排序。

## 所属模块
[重排序器（Reranker）](note://rag-concept-reranker)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。