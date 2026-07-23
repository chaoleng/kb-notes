---
version: 1
id: rag-embedding-version-drift
title: Embedding：向量版本与语义漂移
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: Embedding 模型升级会改变向量空间，旧向量与新查询向量可能不再兼容。
created: 2026-07-23T11:55:36.184Z
updated: 2026-07-23T11:55:36.184Z
favorite: false
related:
  - rag-concept-embedding
---

# Embedding：向量版本与语义漂移

> Embedding 模型升级会改变向量空间，旧向量与新查询向量可能不再兼容。

## 核心细节
索引中记录模型版本；升级时批量重建或维护双版本索引，并通过回归集确认质量没有下降。

## 所属模块
[Embedding](note://rag-concept-embedding)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。