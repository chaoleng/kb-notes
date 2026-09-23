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
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: RAG 是理解问题、构建知识、检索证据、增强生成和持续评估优化组成的完整链路。本笔记是 RAG 知识树根节点。
created: 2026-07-23T04:36:36.967Z
updated: 2026-09-23T10:30:00.000Z
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

## 五个阶段

本笔记是流程视角的主干，每个阶段一篇；概念视角的定义与细节在 [RAG：概念总览](note://rag-concepts) 一侧，两边不重复描述同一事实。

- **问题理解**：意图判断、查询改写、多轮指代消解。
  - [用户问题理解](note://rag-question-understanding)
    - [查询改写与问题拆分](note://rag-query-rewrite)
    - [多轮对话上下文](note://rag-conversation-context)
- **知识库构建**：采集、解析、清洗、切分、向量化与建索引。
  - [知识库构建](note://rag-knowledge-base)
    - [文档采集、清洗与切分](note://rag-document-processing)
    - [Embedding 与索引](note://rag-embedding-index)
- **相关知识检索**：过滤、多通道召回、融合、重排、截断。
  - [相关知识检索](note://rag-retrieval) → 细节见 [检索器](note://rag-concept-retriever) 与 [重排序器](note://rag-concept-reranker)
- **增强生成**：上下文组装、Prompt 约束、引用绑定。
  - [增强生成](note://rag-generation) → 细节见 [Prompt](note://rag-concept-prompt) 与 [Grounding](note://rag-concept-grounding)
- **评估与持续优化**：分层指标、回归闭环、线上回流。
  - [评估与持续优化](note://rag-evaluation) → 细节见 [RAG 评估](note://rag-concept-evaluation)
    - [知识更新与线上迭代](note://rag-ops-iteration)

## 一句话总览

先把问题问清楚，再从新鲜、可追溯的知识中找对证据，最后让模型只基于证据回答，并用评估结果反过来改进数据、检索和生成。

## 使用方式

想搭系统，按五个阶段顺序读；想排查「为什么答错」，从评估分层开始，先定位是检索层还是生成层；想降低幻觉，直接进概念树的 Grounding 与幻觉两支。