---
version: 1
id: rag-vector-update-consistency
title: 向量数据库：索引更新一致性
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 新增、修改和删除文档时，原文、向量、元数据和搜索缓存需要保持一致。
created: 2026-07-23T11:55:43.270Z
updated: 2026-07-23T11:55:43.270Z
favorite: false
related:
  - rag-concept-vector-database
---

# 向量数据库：索引更新一致性

> 新增、修改和删除文档时，原文、向量、元数据和搜索缓存需要保持一致。

## 核心细节
用内容哈希识别变更，删除旧向量，记录索引版本，并在更新失败时避免暴露半更新状态。

## 所属模块
[向量数据库](note://rag-concept-vector-database)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。