---
version: 1
id: rag-embedding-model-selection
title: Embedding：Embedding 模型选择
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: 语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。
created: 2026-07-23T11:55:33.877Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-embedding
---

# Embedding：Embedding 模型选择

> 语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。

## 先划掉不满足硬约束的
中文知识库先确认模型的训练语料是否含中文，纯英文模型对中文短语的区分度常常塌缩成一团。再看 max_seq_length，多数开源模型只有 512 token，超出部分被静默截断，片段尺寸必须与之对齐。药品名、器件型号、内部缩写这类术语若被分词切碎，语义通道基本指望不上，得靠关键词检索兜底。

## 维度、吞吐与成本
768 维和 1536 维在多数业务集上 Recall@10 只差几个点，存储与内存占用却翻倍，距离计算耗时也接近线性上升。千万级片段优先 768 维，或选支持 Matryoshka 截断的模型在 1024 维处截取。自托管要压测单卡 QPS 和 p95 编码延迟，走 API 则要核算每百万 token 单价与限流配额。

## 用自己的问题集横评
抽 200–300 条真实提问，标注出应当命中的片段，固定切分与索引参数，只替换模型，比较 Recall@5、Recall@20 和 MRR@10。公开榜单的平均分代替不了这一步，它的语料分布跟你的库大概率对不上。

## 上线前复核两件事
查询侧与文档侧必须是同一模型同一版本；以及确认模型是否要求 `query:` / `passage:` 这类非对称前缀，前缀写错会让整体分数系统性偏低而不报任何错。
