---
version: 1
id: rag-rag-workflow
title: RAG（检索增强生成）：RAG 端到端工作流
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 理解问题、找证据、组织上下文、生成答案和评估反馈的完整闭环。
created: 2026-07-23T11:55:19.416Z
updated: 2026-07-23T11:55:19.416Z
favorite: false
related:
  - rag-concept-rag
---

# RAG（检索增强生成）：RAG 端到端工作流

> 理解问题、找证据、组织上下文、生成答案和评估反馈的完整闭环。

## 核心细节
一次请求可以拆为：问题分类 → 查询改写 → 权限过滤 → 多路召回 → 去重重排 → 上下文压缩 → Prompt 组装 → 模型生成 → 引用检查。任何一步都可能成为最终质量瓶颈。

## 所属模块
[RAG（检索增强生成）](note://rag-concept-rag)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。