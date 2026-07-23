---
version: 1
id: rag-chunking-overlap
title: 文档切分（Chunking）：片段重叠与上下文连续性
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 相邻片段保留少量重叠可以避免句子或论证被切断。
created: 2026-07-23T11:55:48.271Z
updated: 2026-07-23T11:55:48.271Z
favorite: false
related:
  - rag-concept-chunking
---

# 文档切分（Chunking）：片段重叠与上下文连续性

> 相邻片段保留少量重叠可以避免句子或论证被切断。

## 核心细节
重叠过小会丢失跨边界信息，过大则造成重复召回和索引膨胀。应通过问题集测试而不是固定追求某个比例。

## 所属模块
[文档切分（Chunking）](note://rag-concept-chunking)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。