---
version: 1
id: rag-concept-prompt
title: 概念：Prompt（提示词）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 用于约束模型角色、输入格式、证据使用方式和输出格式的指令模板。
created: 2026-07-23T05:22:32.189Z
updated: 2026-07-23T05:22:32.189Z
favorite: false
related:
  - rag-concepts
---

## 定义
Prompt 是发送给模型的指令与上下文结构。在 RAG 中，它通常包含系统规则、用户问题、检索证据、引用要求和输出格式。

## 作用
告诉模型如何使用证据、证据不足时如何回答、如何区分事实与推断，以及如何返回引用。

## 误区
Prompt 不能修复缺失或错误的知识；过度堆叠规则也会增加冲突。外部文档中的指令应被视为数据，不能覆盖系统级约束。