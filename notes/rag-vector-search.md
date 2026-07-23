---
version: 1
id: rag-vector-search
title: RAG：向量检索
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 利用向量相似度召回语义相近的知识片段，适合表达方式不同但含义相近的问题。
created: 2026-07-23T04:42:29.713Z
updated: 2026-07-23T04:42:29.713Z
favorite: false
related:
  - rag-retrieval
---

## 优点
不依赖完全相同的关键词，能处理同义表达和自然语言提问。

## 局限
对精确编号、专有名词、版本号和否定词可能不敏感；向量相似不等于事实相关。

## 实践
结合元数据过滤、关键词检索和重排序；为不同领域设定独立的评估集。