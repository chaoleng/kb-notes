---
version: 1
id: rag-embedding-index
title: RAG：Embedding 与索引
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把知识片段编码成向量并建立索引，让语义相近的问题能够找到相关内容。
created: 2026-07-23T04:42:24.820Z
updated: 2026-07-23T04:42:24.820Z
favorite: false
related:
  - rag-knowledge-base
---

## Embedding
Embedding 将文本映射为向量。模型选择、语言覆盖、领域适配和版本一致性会直接影响相似度。

## 索引
向量索引负责近似近邻搜索；同时建议保留关键词索引和结构化元数据过滤。

## 更新策略
文档变更时按内容哈希增量重算，删除文档时同步删除旧向量，避免“幽灵知识”。

## 注意
查询向量与文档向量必须使用兼容的模型、归一化方式和距离度量。