---
version: 1
id: rag-evaluation-online-monitoring
title: RAG 评估：线上监控与反馈闭环
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。
created: 2026-07-23T11:56:34.785Z
updated: 2026-07-23T11:56:34.785Z
favorite: false
related:
  - rag-concept-evaluation
---

# RAG 评估：线上监控与反馈闭环

> 记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。

## 核心细节
将线上失败样本回流离线数据集，修改切分、检索或 Prompt 后做回归，形成持续优化闭环。

## 所属模块
[RAG 评估](note://rag-concept-evaluation)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。