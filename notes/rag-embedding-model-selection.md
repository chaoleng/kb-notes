---
version: 1
id: rag-embedding-model-selection
title: Embedding：Embedding 模型选择
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。
created: 2026-07-23T11:55:33.877Z
updated: 2026-07-23T11:55:33.877Z
favorite: false
related:
  - rag-concept-embedding
---

# Embedding：Embedding 模型选择

> 语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。

## 核心细节
应使用真实问题集比较不同模型的 Recall@K 和排序质量，并保持查询与文档使用兼容版本。

## 所属模块
[Embedding](note://rag-concept-embedding)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。