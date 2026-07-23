---
version: 1
id: rag
title: 一图看懂RAG运行全流程
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: RAG 是理解问题、构建知识、检索证据、增强生成和持续评估优化组成的完整链路。本笔记是 RAG 知识树根节点。
created: 2026-07-23T04:36:36.967Z
updated: 2026-07-23T05:22:45.828Z
favorite: false
related:
  - rag-question-understanding
  - rag-knowledge-base
  - rag-retrieval
  - rag-generation
  - rag-evaluation
  - rag-concepts
---

# RAG 运行全流程：知识树主干

> 来源文章：一图看懂RAG运行全流程
> https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ

RAG 不是简单地“给大模型接一个知识库”，而是一条完整的信息处理链路：理解问题 → 构建并检索知识 → 组织上下文 → 生成有依据的答案 → 评估和持续优化。

## 知识树

- **问题理解**：识别意图、查询改写、多轮上下文。
  - [rag-question-understanding](note://rag-question-understanding)
    - [rag-query-rewrite](note://rag-query-rewrite)
    - [rag-conversation-context](note://rag-conversation-context)
- **知识库构建**：采集、清洗、切分、Embedding 和索引。
  - [rag-knowledge-base](note://rag-knowledge-base)
    - [rag-document-processing](note://rag-document-processing)
    - [rag-embedding-index](note://rag-embedding-index)
- **相关知识检索**：向量、关键词、混合检索和重排序。
  - [rag-retrieval](note://rag-retrieval)
    - [rag-vector-search](note://rag-vector-search)
    - [rag-hybrid-rerank](note://rag-hybrid-rerank)
- **增强生成**：上下文拼接、Prompt、引用和事实依据。
  - [rag-generation](note://rag-generation)
    - [rag-context-prompt](note://rag-context-prompt)
    - [rag-citation-grounding](note://rag-citation-grounding)
- **评估与持续优化**：质量指标、知识更新、监控和迭代。
  - [rag-evaluation](note://rag-evaluation)
    - [rag-quality-evaluation](note://rag-quality-evaluation)
    - [rag-ops-iteration](note://rag-ops-iteration)

## 一句话总览

先把问题问清楚，再从新鲜、可追溯的知识中找对证据，最后让模型只基于证据回答，并用评估结果反过来改进数据、检索和生成。

## 使用方式

从任一分支进入都可以回到主干：想了解“为什么答错”，先看检索和评估；想搭建系统，先看知识库构建，再看检索和生成；想降低幻觉，重点看引用与事实依据。