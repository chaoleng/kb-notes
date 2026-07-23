---
version: 1
id: rag-quality-evaluation
title: RAG：召回率、准确性与幻觉评估
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 用可重复的问题集评估检索命中、答案正确性、证据忠实度和未知问题处理。
created: 2026-07-23T04:42:44.613Z
updated: 2026-07-23T04:42:44.613Z
favorite: false
related:
  - rag-evaluation
---

## 核心指标
- Recall@K：正确证据是否进入前 K 个结果。
- Precision：召回片段中有多少真正相关。
- Faithfulness：答案是否被证据支持。
- Answer relevance：答案是否真正回应问题。

## 测试集
覆盖简单查找、跨文档综合、版本冲突、无答案、越权和多轮问题。评估结果要能定位到 RAG 链路中的具体失败环节。