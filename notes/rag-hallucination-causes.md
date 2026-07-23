---
version: 1
id: rag-hallucination-causes
title: 幻觉（Hallucination）：幻觉成因
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 常见根因有知识缺失、召回错误、证据冲突、上下文过载和模型过度推断。
created: 2026-07-23T11:56:25.375Z
updated: 2026-07-23T11:56:25.375Z
favorite: false
related:
  - rag-concept-hallucination
---

# 幻觉（Hallucination）：幻觉成因

> 常见根因有知识缺失、召回错误、证据冲突、上下文过载和模型过度推断。

## 核心细节
不要只通过降低 temperature 处理；生成参数只能影响随机性，不能补齐缺失证据。

## 所属模块
[幻觉（Hallucination）](note://rag-concept-hallucination)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。