---
version: 1
id: rag-grounding-conflict
title: Grounding：证据冲突处理
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 当多个来源对同一事实不一致时，按版本、时间、权威等级和适用范围进行判断。
created: 2026-07-23T11:56:20.417Z
updated: 2026-07-23T11:56:20.417Z
favorite: false
related:
  - rag-concept-grounding
---

# Grounding：证据冲突处理

> 当多个来源对同一事实不一致时，按版本、时间、权威等级和适用范围进行判断。

## 核心细节
不能简单拼接互相矛盾的片段；应展示冲突、说明采用的依据，必要时向用户追问。

## 所属模块
[Grounding](note://rag-concept-grounding)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。