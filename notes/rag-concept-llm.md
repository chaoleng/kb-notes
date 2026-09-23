---
version: 1
id: rag-concept-llm
title: 概念：大语言模型（LLM）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 根据上下文预测和生成文本的模型，负责理解问题、组织证据和生成自然语言答案。
created: 2026-07-23T05:22:16.837Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - rag-concepts
  - rag-llm-context-window
  - rag-llm-decoding
  - rag-llm-instruction-hierarchy
  - rag-long-context
---

## 定义
大语言模型（Large Language Model，LLM）通过大规模文本训练获得语言理解和生成能力。

## 在 RAG 中的角色
LLM 可以负责查询改写、问题拆分、答案生成、摘要和结果判断，但它本身不是知识库，也不保证记忆中的事实永远最新。

## 与 RAG 的关系
RAG 把外部检索证据放入 LLM 的上下文，使模型能在不重新训练的情况下使用新知识和私有知识。

## 误区
模型“知道”某件事不等于它能给出可验证答案；上下文中出现的文本也不自动成为事实，仍需要来源和一致性检查。

## 详细分支
- [LLM 上下文窗口](note://rag-llm-context-window)：模型一次请求能够接收的输入和输出 token 总量，决定可放入多少检索资料。
- [LLM 解码与生成参数](note://rag-llm-decoding)：temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。
- [指令层级与模型约束](note://rag-llm-instruction-hierarchy)：系统指令、用户问题和外部文档之间存在优先级，外部资料不能覆盖系统规则。
- [长上下文模型与 RAG 的分工](note://rag-long-context)：窗口变大不等于可以取消检索，位置偏置、成本与权限过滤仍要靠 RAG 解决。
