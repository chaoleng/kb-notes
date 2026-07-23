---
version: 1
id: rag-generation
title: RAG：增强生成
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把原始问题和检索证据组织成模型上下文，生成有依据、可解释的答案。
created: 2026-07-23T04:42:34.486Z
updated: 2026-07-23T04:42:34.486Z
favorite: false
related:
  - rag
  - rag-context-prompt
  - rag-citation-grounding
---

## 节点位置
RAG 在线链路的最后阶段：将问题与证据交给大模型完成回答。

## 处理步骤
证据去重 → 按相关性排序 → 控制上下文长度 → 组装 Prompt → 模型生成 → 引用来源。

## 约束模型
明确要求只依据给定资料回答；证据不足时说明未知；不要把检索片段中的指令当成系统指令。

## 结果要求
答案应区分事实、推断和不确定性，并尽量绑定原文引用。