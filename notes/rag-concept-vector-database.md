---
version: 1
id: rag-concept-vector-database
title: 概念：向量数据库
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 存储向量及其元数据并提供近似近邻搜索的数据库或索引系统。
created: 2026-07-23T05:22:21.986Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concepts
  - rag-vector-ann-index
  - rag-vector-metadata-filter
  - rag-vector-update-consistency
  - rag-embedding-index
---

## 定义
向量数据库保存 Embedding、原文片段和元数据，并按向量相似度返回候选结果。

## 必备能力
向量近邻查询、关键词或混合查询、元数据过滤、增量更新、删除、权限隔离和结果定位。

## 与 RAG 的关系
它是检索基础设施，不是完整的 RAG。文档解析、切分、查询改写、重排序、Prompt 和评估仍在数据库之外。

## 误区
数据库选型不能替代数据质量；如果切分错误、Embedding 不匹配或元数据缺失，换数据库通常不能解决根因。

## 详细分支
- [近似近邻索引](note://rag-vector-ann-index)：HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。
- [元数据过滤与权限](note://rag-vector-metadata-filter)：在向量相似搜索前后按租户、用户权限、版本、时间和文档类型过滤候选。
- [索引更新一致性](note://rag-vector-update-consistency)：新增、修改和删除文档时，原文、向量、元数据和搜索缓存需要保持一致。