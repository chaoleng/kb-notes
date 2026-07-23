---
version: 1
id: rag-llm-context-window
title: 大语言模型（LLM）：LLM 上下文窗口
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 模型一次请求能够接收的输入和输出 token 总量，决定可放入多少检索资料。
created: 2026-07-23T11:55:24.455Z
updated: 2026-07-23T11:55:24.455Z
favorite: false
related:
  - rag-concept-llm
---

# 大语言模型（LLM）：LLM 上下文窗口

> 模型一次请求能够接收的输入和输出 token 总量，决定可放入多少检索资料。

## 核心细节
上下文窗口不是越大越好。冗余片段会增加成本和延迟，并可能让模型忽略关键证据。应先去重、排序、压缩，再按预算放入上下文。

## 所属模块
[大语言模型（LLM）](note://rag-concept-llm)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。