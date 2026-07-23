---
version: 1
id: rag-embedding-similarity
title: Embedding：向量相似度与距离
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 余弦相似度、点积或欧氏距离用于衡量查询向量与文档向量的接近程度。
created: 2026-07-23T11:55:31.529Z
updated: 2026-07-23T11:55:31.529Z
favorite: false
related:
  - rag-concept-embedding
---

# Embedding：向量相似度与距离

> 余弦相似度、点积或欧氏距离用于衡量查询向量与文档向量的接近程度。

## 核心细节
距离指标必须与 Embedding 模型的训练和归一化方式匹配。相似度高只说明语义接近，不能单独证明片段包含正确答案。

## 所属模块
[Embedding](note://rag-concept-embedding)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。