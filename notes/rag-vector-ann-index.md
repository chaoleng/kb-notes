---
version: 1
id: rag-vector-ann-index
title: 向量数据库：近似近邻索引
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。
created: 2026-07-23T11:55:38.595Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-vector-database
---

# 向量数据库：近似近邻索引

> HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。

## 三类索引各自的适用规模
Flat 做暴力全扫描，召回恒为 1，百万条 768 维 float32 约占 3GB，单查询几十到上百毫秒，适合十万量级以内以及给离线评测当基线。IVF 用 k-means 把向量切成 nlist 个簇，查询只扫 nprobe 个簇，nlist 常取 sqrt(N) 附近，nprobe 越大越接近暴力搜索。HNSW 建分层邻接图并沿图贪心下降，是在线检索的默认选择。

## HNSW 的三个旋钮
M 是每个节点的出边数，典型 16–48，图结构本身的内存大致随 M 线性增长。efConstruction 控制建图时的候选队列，常取 128–512，只影响构建耗时与图质量。efSearch 是唯一的在线旋钮，必须不小于 topK，从 64 提到 256 往往把 Recall@10 由 0.90 推到 0.98，代价是 p95 延迟近似线性上涨。调参顺序：固定 M 与 efConstruction 建一次图，再用带标注的查询集扫 efSearch，取达标的最小值。

## 量化省内存的代价
SQ8 把 float32 压成 int8，内存降到四分之一，召回损失通常在一个百分点以内。PQ 把维度切成 m 个子空间各用 256 个码字，压缩比可达数十倍，但 Recall@10 可能掉 5 到 15 个点，必须配 refine：先用码字取 topK 的四倍候选，再拿原始向量重排。

## 构建成本也要计入
千万级 HNSW 建图常需数小时且中途难以复用，IVF 训练只要几分钟，这在需要频繁重建的场景里比查询延迟更关键。
