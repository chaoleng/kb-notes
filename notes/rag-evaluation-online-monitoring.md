---
version: 1
id: rag-evaluation-online-monitoring
title: RAG 评估：线上监控与反馈闭环
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: 记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。
created: 2026-07-23T11:56:34.785Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-evaluation
  - rag-ops-iteration
---

# RAG 评估：线上监控与反馈闭环

> 记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。

## 落库字段
每次请求落一条 trace：原始查询与改写后查询、召回片段 id 及分数、最终进入 Prompt 的片段、答案文本、答案里的引用、检索与生成的分段耗时、prompt 与 completion 的 token 数。没有片段 id 就无法事后复现当时的检索结果，这条比存答案更重要。

## 延迟与成本
延迟看 p50 和 p95 两个分位，均值会被长尾掩盖；分段计时才能区分慢在向量检索还是重排。成本按单次问答的 token 折算，重排和超长上下文最容易让单价翻倍而质量不变。

## 反馈信号
显式信号是点赞点踩加上「引用不对」这类细分选项；隐式信号包括复制答案、就同一问题反复追问、转人工。隐式负反馈的量级通常是显式的十倍以上，只盯点踩率会严重低估问题面。

## 回流闭环
踩过的样本按失败类型归档：没召回、召回了没用上、引用错位、越权、该拒答没拒。每周挑一批补进[离线评估集](note://rag-evaluation-dataset)，改完切分、检索或 Prompt 后跑全量回归，确认新问题修好且旧样本没退化再灰度放量。
