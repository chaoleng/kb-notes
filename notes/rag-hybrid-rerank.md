---
version: 1
id: rag-hybrid-rerank
title: RAG：混合检索与重排序
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 结合关键词、向量和结构化过滤，再用重排序模型提升候选片段的最终相关性。
created: 2026-07-23T04:42:32.128Z
updated: 2026-07-23T04:42:32.128Z
favorite: false
related:
  - rag-retrieval
---

## 混合检索
关键词检索擅长精确匹配，向量检索擅长语义匹配，结构化过滤负责时间、版本、权限和业务范围。

## 重排序
先用低成本方法召回较大的候选集，再用 Cross-Encoder 或规则模型对候选重新排序。

## 取舍
重排序提高相关性但增加延迟和成本；需要通过离线评估确定候选数量与截断位置。