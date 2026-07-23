---
version: 1
id: rag-concept-rag
title: 概念：RAG（检索增强生成）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 通过外部知识检索增强大语言模型生成的系统方法，不等同于单纯的向量数据库。
created: 2026-07-23T05:22:14.272Z
updated: 2026-07-23T05:22:14.272Z
favorite: false
related:
  - rag-concepts
---

## 定义
RAG（Retrieval-Augmented Generation，检索增强生成）是在生成回答前，从外部知识源检索相关证据，再把证据交给大语言模型生成答案的方法。

## 解决的问题
模型参数中的知识可能过时、缺少企业内部资料，或者无法稳定提供来源。RAG 通过运行时检索补充这些知识。

## 核心链路
问题理解 → 知识库构建 → 检索 → 上下文增强 → 生成 → 引用与评估。

## 关系
Embedding、向量数据库、Retriever 和 Reranker 是检索侧概念；LLM 和 Prompt 是生成侧概念；Grounding 与评估负责约束和验证结果。

## 误区
RAG 不是“把所有文档塞进 Prompt”，也不是只安装一个向量数据库。数据处理、检索质量和生成约束同样决定效果。