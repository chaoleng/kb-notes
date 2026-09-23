---
version: 1
id: rag-evaluation-metrics
title: RAG 评估：检索与生成指标
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 检索关注 Recall@K、Precision、MRR；生成关注相关性、完整性、Faithfulness 和引用正确性。
created: 2026-07-23T11:56:32.281Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-evaluation
---

# RAG 评估：检索与生成指标

> 检索关注 Recall@K、Precision、MRR；生成关注相关性、完整性、Faithfulness 和引用正确性。

## 检索侧口径
Recall@K 看正确证据是否落进前 K 条，K 一般同时取 5 和 20：K=20 衡量召回层的上限，K=5 衡量送进 Prompt 之后还剩多少可用证据。Precision 统计召回片段里真正相关的比例，直接决定上下文的噪声量。MRR 只关心第一条正确结果的倒数排名，适合单证据问答；nDCG 按位置对多条证据加权打折，跨文档综合题必须用它。

## 生成侧口径
Faithfulness 判断答案的每个断言是否被给定证据支持，Answer relevance 判断答案有没有真正回应问题。两者会分离：照抄证据的答案忠实度满分却答非所问。再加上引用正确性与要点完整性，四项分开报，不要合成一个总分。

## 单一分数为何不可信
自动评分模型与人工判断的一致率常在 0.7 上下，并且系统性偏爱更长的答案。这类指标只适合做回归报警：某次改动让 Recall@5 掉 3 个点值得回查，涨 1 个点不值得庆祝。关键场景每轮抽 30–50 条人工复核，再绑定一个业务口径（如工单自助解决率），结论才站得住。
