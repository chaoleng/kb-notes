---
version: 1
id: rag-evaluation
title: RAG：评估与持续优化
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 从检索质量、答案准确性、引用完整性和系统成本延迟等维度持续改进 RAG。
created: 2026-07-23T04:42:42.313Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag
  - rag-ops-iteration
  - rag-concept-evaluation
---

## 三层分开量
1. 检索层：正确证据有没有被召回、排在第几位。
2. 生成层：答案是否正确、是否被证据支持、引用是否指对。
3. 系统层：p95 延迟、单次问答 token 成本、知识新鲜度、权限拒绝是否正确。

三层要分别出分。只看一个端到端准确率，失败时无法定位是哪一层退化。

## 闭环节奏
固定问题集回归 → 记录每次的召回片段与答案 → 标注失败类型 → 只改一处（切分 / Embedding / 检索 / 重排 / Prompt / 模型）→ 重新跑同一套问题集。一次改多处就失去归因能力。指标口径见 [检索与生成指标](note://rag-evaluation-metrics)。

## 上线后才暴露的问题
真实流量里的问题分布与自建评估集通常差很远，因此线上日志与失败样本必须回流进回归集（见 [知识更新与线上迭代](note://rag-ops-iteration)）。

## 目标
用最少、最可靠的证据得到可核对的答案，而不是把上下文塞满。
