---
version: 1
id: rag-question-understanding
title: RAG：用户问题理解
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: RAG 的入口：识别用户意图、补全查询和处理多轮上下文，决定后续检索方向。
created: 2026-07-23T04:42:12.347Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - rag
  - rag-query-rewrite
  - rag-conversation-context
  - rag-query-routing
  - rag-query-expansion
---

## 在链路中的位置
主干第一步。它的输出是检索层的唯一输入，这一步判错，后面的召回、重排和生成都在为错误的问题服务。

## 输入与输出
- 输入：原始提问、历史对话、用户身份与权限、当前产品/版本上下文。
- 输出：一到多条标准化检索查询、结构化过滤条件（时间、版本、租户、权限）、回答范围声明。

## 这一步要拿下的三个判断
1. 问的是查找型问题（走检索）还是计算/操作型问题（走 SQL 或工具调用，见 [RAG 的边界](note://rag-rag-limits)）。
2. 问题是否自足，指代和省略要先补全，再交给检索。
3. 需要几条查询：比较类和因果类问题往往要拆成多条子查询分别召回。

## 失败信号
检索结果与问题主题明显无关、同一问题换个说法结果差异很大、多轮对话中第二轮开始召回质量骤降——这三种现象通常都不是检索器的锅，而是问题理解没做。

## 展开阅读
判断走不走检索、路由到哪个库见 [查询路由与意图分类](note://rag-query-routing)；同一意图并行多条查询见 [多路召回与查询扩展](note://rag-query-expansion)。
