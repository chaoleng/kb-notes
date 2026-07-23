---
version: 1
id: rag-concept-chunking
title: 概念：文档切分（Chunking）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把长文档划分成适合检索和上下文拼接的知识片段。
created: 2026-07-23T05:22:24.385Z
updated: 2026-07-23T05:22:24.385Z
favorite: false
related:
  - rag-concepts
---

## 定义
Chunking 是把文档按标题、段落、列表、代码或语义边界拆成片段，并保留必要的重叠和元数据。

## 目标
每个片段要足够小，便于精准召回；同时要足够完整，能够独立表达一个事实或论点。

## 常见策略
固定长度、递归字符切分、按 Markdown 标题切分、语义切分和父子文档切分。

## 误区
片段越小不一定越好；过度切分会丢失上下文，片段过大则会降低相关性并浪费上下文窗口。