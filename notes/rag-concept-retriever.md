---
version: 1
id: rag-concept-retriever
title: 概念：检索器（Retriever）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 根据用户查询从知识库中召回候选片段的组件。
created: 2026-07-23T05:22:27.110Z
updated: 2026-07-23T05:22:27.110Z
favorite: false
related:
  - rag-concepts
---

## 定义
Retriever 接受查询，返回若干可能包含答案的文档片段及其相关性分数。

## 类型
向量检索适合语义匹配，关键词检索适合精确术语，结构化过滤适合版本、时间和权限；实际系统经常组合使用。

## 关键指标
召回率、Precision、Recall@K、命中排名、延迟和权限正确性。

## 误区
检索器只负责找候选，不负责最终回答；如果候选不相关，后续模型再强也可能被错误上下文带偏。