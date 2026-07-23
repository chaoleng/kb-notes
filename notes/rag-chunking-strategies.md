---
version: 1
id: rag-chunking-strategies
title: 文档切分（Chunking）：切分策略
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 固定长度、递归切分、按标题切分、语义切分和父子文档是常见策略。
created: 2026-07-23T11:55:45.837Z
updated: 2026-07-23T11:55:45.837Z
favorite: false
related:
  - rag-concept-chunking
---

# 文档切分（Chunking）：切分策略

> 固定长度、递归切分、按标题切分、语义切分和父子文档是常见策略。

## 核心细节
技术文档适合保留标题层级，表格和代码需要特殊处理；切分策略应与问题类型和引用粒度匹配。

## 所属模块
[文档切分（Chunking）](note://rag-concept-chunking)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。