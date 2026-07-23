---
version: 1
id: rag-question-understanding
title: RAG：用户问题理解
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: RAG 的入口：识别用户意图、补全查询和处理多轮上下文，决定后续检索方向。
created: 2026-07-23T04:42:12.347Z
updated: 2026-07-23T04:42:12.347Z
favorite: false
related:
  - rag
  - rag-query-rewrite
  - rag-conversation-context
---

## 节点位置
RAG 主干的第一步，位于用户问题与知识库检索之间。

## 核心职责
1. 判断问题的真实意图和需要的知识范围。
2. 将口语、缩写或不完整的问题转换为可检索查询。
3. 从多轮对话中提取当前问题依赖的上下文。

## 输入与输出
- 输入：原始问题、历史对话、用户约束。
- 输出：标准化查询、过滤条件、回答范围和必要的引用要求。

## 常见方法
- 意图分类与实体抽取。
- 查询改写、拆分和扩展。
- 多轮问题指代消解。

## 常见问题
改写过度会改变原意；上下文过长会引入噪声；忽略时间、权限或产品版本会导致检索结果失真。