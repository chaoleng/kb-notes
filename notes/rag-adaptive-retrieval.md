---
version: 1
id: rag-adaptive-retrieval
title: RAG：自适应与迭代检索
tags:
  - RAG
  - 检索
  - 自适应检索
  - Self-RAG
source: Self-RAG (Asai et al., 2023) / CRAG (Yan et al., 2024)
summary: 把检不检、要不要再检一轮变成运行时决策，Self-RAG 靠反省 token，CRAG 靠轻量评估器。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - rag-concept-retriever
---

# RAG：自适应与迭代检索

> 把检不检、要不要再检一轮变成运行时决策，Self-RAG 靠反省 token，CRAG 靠轻量评估器。

## 固定一轮的两种浪费
标准流水线对每个问题都检索一次、取固定 top-k。模型本来就会的常识题，检索只贡献噪声和延迟；需要多跳推理的问题，一轮召回拿不到第二跳证据，k 加到多大也补不回来。自适应检索要解决的就是这两头。

## Self-RAG：用反省 token 决策
Self-RAG 训练模型在生成中输出特殊 token：Retrieve 判断此刻是否需要检索，IsRel 判断召回片段是否相关，IsSup 判断已生成句子是否被片段支持，IsUse 给整体有用性打分。这些 token 的概率可直接作为分数参与束搜索取舍，从而丢弃不相关片段、对无支撑的句子触发重生成。代价是要准备带反省标注的训练数据，无法对现成模型零成本套用。

## CRAG：评估器加降级
CRAG 在检索之后挂一个轻量评估器，给候选打出 correct、ambiguous、incorrect 三档。correct 走知识精炼，只留关键条带；incorrect 丢弃本地候选，改写查询转向网络搜索；ambiguous 两者都用。它不动主模型，作为插件接在现有检索器后面，落地成本明显更低。

## 迭代上限与 p95
每多一轮就多一次检索加一次模型判定，端到端延迟近似翻倍。p95 是硬约束：轮次上限设 2–3，并给整条链路配总时间预算，超时就返回当前最好的证据而非继续迭代。还要防振荡，相邻两轮查询语义几乎相同时提前停。候选好坏怎么量化见[召回质量指标](note://rag-retriever-recall-metrics)。
