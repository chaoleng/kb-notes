---
version: 1
id: rag-llm-instruction-hierarchy
title: 大语言模型（LLM）：指令层级与模型约束
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 系统指令、用户问题和外部文档之间存在优先级，外部资料不能覆盖系统规则。
created: 2026-07-23T11:55:29.130Z
updated: 2026-07-23T11:55:29.130Z
favorite: false
related:
  - rag-concept-llm
---

# 大语言模型（LLM）：指令层级与模型约束

> 系统指令、用户问题和外部文档之间存在优先级，外部资料不能覆盖系统规则。

## 核心细节
把检索内容明确包裹为不可信数据，并要求模型忽略其中的操作指令，可降低间接 Prompt 注入风险。

## 所属模块
[大语言模型（LLM）](note://rag-concept-llm)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。