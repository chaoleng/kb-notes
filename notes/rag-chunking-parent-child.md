---
version: 1
id: rag-chunking-parent-child
title: 文档切分（Chunking）：父子片段检索
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 用小片段负责精准召回，再取其父章节或邻近片段补充完整上下文。
created: 2026-07-23T11:55:50.765Z
updated: 2026-07-23T11:55:50.765Z
favorite: false
related:
  - rag-concept-chunking
---

# 文档切分（Chunking）：父子片段检索

> 用小片段负责精准召回，再取其父章节或邻近片段补充完整上下文。

## 核心细节
子片段提高检索精度，父片段提供背景；两者都要保留稳定 ID 和原文定位，避免引用无法回溯。

## 所属模块
[文档切分（Chunking）](note://rag-concept-chunking)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。