---
version: 1
id: rag-retriever-hybrid
title: 检索器（Retriever）：混合检索
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 通过结果融合或加权组合关键词、向量和结构化过滤，兼顾精确匹配与语义匹配。
created: 2026-07-23T11:55:56.272Z
updated: 2026-07-23T11:55:56.272Z
favorite: false
related:
  - rag-concept-retriever
---

# 检索器（Retriever）：混合检索

> 通过结果融合或加权组合关键词、向量和结构化过滤，兼顾精确匹配与语义匹配。

## 核心细节
可使用分数归一化、排名融合或 RRF；融合策略要在代表性问题集上验证，避免一条通道压制另一条通道。

## 所属模块
[检索器（Retriever）](note://rag-concept-retriever)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。