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
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-knowledge-base
  - rag-concept-embedding
  - rag-concept-vector-database
---

## 这一步产出什么
片段的向量表示，加上支撑线上检索的三套索引：向量索引、关键词倒排索引、结构化元数据索引。只建向量索引，精确编号和错误码类查询会直接漏召。

## 批量向量化的工程点
按内容哈希去重后再调用 embedding 接口，避免重复付费；批量请求控制并发与重试；记录每条向量对应的模型名与版本，写进索引字段。没有版本字段，后续换模型时无法判断哪些向量需要重算（见 [向量版本与语义漂移](note://rag-embedding-version-drift)）。

## 索引选型的分界
数据量小到几万条时精确检索即可，无需近似索引；上到百万级再考虑 HNSW 或 IVF 的参数取舍（见 [近似近邻索引](note://rag-vector-ann-index)）。

## 查询侧必须对齐
查询向量与文档向量要用同一模型、同一归一化方式、同一距离度量。三者任一不一致，相似度分数就失去可比性，而且不会报错，只会安静地返回错误结果。
