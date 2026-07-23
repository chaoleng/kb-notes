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
updated: 2026-07-23T05:22:19.382Z
favorite: false
related:
  - rag-concepts
---

## 定义
Embedding 模型把文本编码为高维向量，使语义相近的内容在向量空间中更接近。

## 用途
文档片段建立向量，用户问题也建立向量，再通过距离或相似度找到候选知识。

## 关键因素
模型的语言和领域覆盖、文本长度、向量归一化、距离度量以及查询向量和文档向量是否使用兼容模型。

## 误区
向量相似只表示表达或语义接近，不代表事实正确；编号、版本号、精确术语和否定关系往往需要关键词或结构化过滤补充。