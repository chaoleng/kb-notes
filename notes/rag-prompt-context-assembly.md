---
version: 1
id: rag-prompt-context-assembly
title: Prompt：上下文组装
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 按照相关性、来源可信度、时间和互补性排列片段，并控制总 token 预算。
created: 2026-07-23T11:56:10.702Z
updated: 2026-07-23T11:56:10.702Z
favorite: false
related:
  - rag-concept-prompt
---

# Prompt：上下文组装

> 按照相关性、来源可信度、时间和互补性排列片段，并控制总 token 预算。

## 核心细节
先去重和压缩，再放入上下文；保留标题、来源和定位字段，让模型更容易引用和判断冲突。

## 所属模块
[Prompt](note://rag-concept-prompt)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。