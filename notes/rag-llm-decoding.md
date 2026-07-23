---
version: 1
id: rag-llm-decoding
title: 大语言模型（LLM）：LLM 解码与生成参数
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。
created: 2026-07-23T11:55:26.779Z
updated: 2026-07-23T11:55:26.779Z
favorite: false
related:
  - rag-concept-llm
---

# 大语言模型（LLM）：LLM 解码与生成参数

> temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。

## 核心细节
知识问答通常需要较稳定的输出，温度过高会增加措辞和事实波动。参数不能修复错误检索，必须结合证据质量和回归集调节。

## 所属模块
[大语言模型（LLM）](note://rag-concept-llm)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。