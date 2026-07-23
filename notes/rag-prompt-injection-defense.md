---
version: 1
id: rag-prompt-injection-defense
title: Prompt：Prompt 注入防护
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把外部文档当作数据而不是指令，限制工具调用和敏感信息输出。
created: 2026-07-23T11:56:13.241Z
updated: 2026-07-23T11:56:13.241Z
favorite: false
related:
  - rag-concept-prompt
---

# Prompt：Prompt 注入防护

> 把外部文档当作数据而不是指令，限制工具调用和敏感信息输出。

## 核心细节
系统规则必须独立于检索内容；对网页、代码和用户上传文档进行边界标记，并对输出做权限和格式检查。

## 所属模块
[Prompt](note://rag-concept-prompt)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。