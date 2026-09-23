---
version: 1
id: rag-retriever-recall-metrics
title: 检索器（Retriever）：召回质量指标
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。
created: 2026-07-23T11:55:58.657Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-retriever
---

# 检索器（Retriever）：召回质量指标

> Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。

## 每个指标回答一个问题
Recall@K 问的是正确证据有没有进入前 K，它是整条链路的天花板：没进候选池的内容，后面任何环节都救不回来。Precision@K 问前 K 条里有多少真正有用，决定送进上下文的噪声比例。MRR 取首个正确结果名次的倒数再平均，对排第一还是排第五特别敏感。

## K 要和下游消费者对齐
汇报时的 K 不能随手挑。召回层看 Recall@100，因为这正是交给重排的候选数量；重排之后看 Recall@5 和 Precision@5，因为这是真正拼进 prompt 的片段数。报一个下游根本不会消费的 Recall@1000，数字好看却无法指导任何决策。

## 看分布而不是只看均值
把每条问题的命中名次画成直方图更有用：七成落在前三位、两成掉到四十位之后，这条长尾会被平均值抹平。长尾正是重排可能捞回的部分，也是设定重排候选数的直接依据；如果正确证据大量落在两百位开外，先修召回。

## 低分要做三分归因
拿到不及格的结果先分三类：证据压根不在候选集，属召回缺失，该动分块或补通道；在候选集但名次靠后，属排序问题，引入重排更划算；证据本身残缺或过期，属语料问题，得回到文档处理。三类混在一起统计，任何调整都像有效果。评测前先备好带参考证据的[评估集](note://rag-evaluation-dataset)。
