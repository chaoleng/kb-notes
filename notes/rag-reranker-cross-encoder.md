---
version: 1
id: rag-reranker-cross-encoder
title: 重排序器（Reranker）：Cross-Encoder 重排序
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 让模型同时读取查询和候选片段，直接判断二者的相关性。
created: 2026-07-23T11:56:00.953Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-reranker
---

# 重排序器（Reranker）：Cross-Encoder 重排序

> 让模型同时读取查询和候选片段，直接判断二者的相关性。

## 与双塔结构的差别
Bi-Encoder 把问题和文档分别编码，文档向量可以离线算好写进索引，线上只做一次近邻查找。Cross-Encoder 则把二者拼成一条序列送进同一个 Transformer 联合编码，注意力可以在问题词与文档词之间直接交互，最后输出一个标量相关性分数。精度更高的原因就在这层交互。

## 算力账：无法预计算
分数依赖具体问题，文档侧没有任何中间结果能提前缓存：来一个问题，有多少候选就要跑多少次前向，开销随候选数线性增长。base 规模模型在单张 GPU 上处理一百条 512 token 候选约需几十到一百多毫秒，放大到一千条就是秒级，足以打穿 p95 预算。

## 只重排头部候选
通行做法是召回层交出 50–100 条，重排只覆盖这一段。再往外扩，延迟线性上涨而收益迅速衰减；若正确证据连前一百都进不去，该修的是召回通道而不是把重排窗口开大。

## 落地时容易踩的坑
截断长度要与分块长度匹配，候选超过 max_length 会被截尾，长片段的关键句可能根本没进模型。批量推理按长度分桶可减少 padding 浪费。输出是未校准的 logit，只在同一问题内部有序，跨问题设统一阈值做过滤会误杀。
