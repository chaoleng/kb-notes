---
version: 1
id: rag-concept-embedding
title: 概念：Embedding（向量表示）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把文本或其他对象映射为数值向量，用于计算语义相似度和进行近邻检索。
created: 2026-07-23T05:22:19.382Z
updated: 2026-07-23T11:56:42.691Z
favorite: false
related:
  - rag-concepts
  - rag-embedding-similarity
  - rag-embedding-model-selection
  - rag-embedding-version-drift
---

## 定义
Embedding 模型把文本编码为高维向量，使语义相近的内容在向量空间中更接近。

## 用途
文档片段建立向量，用户问题也建立向量，再通过距离或相似度找到候选知识。

## 关键因素
模型的语言和领域覆盖、文本长度、向量归一化、距离度量以及查询向量和文档向量是否使用兼容模型。

## 误区
向量相似只表示表达或语义接近，不代表事实正确；编号、版本号、精确术语和否定关系往往需要关键词或结构化过滤补充。

## 详细分支
- [向量相似度与距离](note://rag-embedding-similarity)：余弦相似度、点积或欧氏距离用于衡量查询向量与文档向量的接近程度。
- [Embedding 模型选择](note://rag-embedding-model-selection)：语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。
- [向量版本与语义漂移](note://rag-embedding-version-drift)：Embedding 模型升级会改变向量空间，旧向量与新查询向量可能不再兼容。