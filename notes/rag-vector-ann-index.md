---
version: 1
id: rag-vector-ann-index
title: 向量数据库：近似近邻索引
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。
created: 2026-07-23T11:55:38.595Z
updated: 2026-07-23T11:55:38.595Z
favorite: false
related:
  - rag-concept-vector-database
---

# 向量数据库：近似近邻索引

> HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。

## 核心细节
索引参数影响召回率、内存和延迟。生产环境应根据数据规模和 Recall@K 调整，而不是只看默认配置。

## 所属模块
[向量数据库](note://rag-concept-vector-database)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。