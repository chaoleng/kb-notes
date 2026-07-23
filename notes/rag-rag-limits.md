---
version: 1
id: rag-rag-limits
title: RAG（检索增强生成）：RAG 的边界与适用场景
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: RAG 适合知识查找和基于资料的问答，但不能替代所有数据库查询、计算和业务操作。
created: 2026-07-23T11:55:22.104Z
updated: 2026-07-23T11:55:22.104Z
favorite: false
related:
  - rag-concept-rag
---

# RAG（检索增强生成）：RAG 的边界与适用场景

> RAG 适合知识查找和基于资料的问答，但不能替代所有数据库查询、计算和业务操作。

## 核心细节
当问题需要实时交易数据、精确聚合、复杂计算或执行动作时，应结合 SQL、API、工具调用或 Agent。RAG 的核心产物是证据上下文，不是业务状态变更。

## 所属模块
[RAG（检索增强生成）](note://rag-concept-rag)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。