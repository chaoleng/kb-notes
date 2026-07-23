---
version: 1
id: rag-vector-metadata-filter
title: 向量数据库：元数据过滤与权限
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 在向量相似搜索前后按租户、用户权限、版本、时间和文档类型过滤候选。
created: 2026-07-23T11:55:40.965Z
updated: 2026-07-23T11:55:40.965Z
favorite: false
related:
  - rag-concept-vector-database
---

# 向量数据库：元数据过滤与权限

> 在向量相似搜索前后按租户、用户权限、版本、时间和文档类型过滤候选。

## 核心细节
权限过滤必须在检索链路中强制执行，不能只靠 Prompt 要求模型忽略越权资料。

## 所属模块
[向量数据库](note://rag-concept-vector-database)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。