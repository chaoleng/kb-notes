---
version: 1
id: rag-retrieval
title: RAG：相关知识检索
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 从知识库召回候选片段并排序，向生成模型提供少量高相关上下文。
created: 2026-07-23T04:42:27.223Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag
  - rag-concept-retriever
  - rag-concept-reranker
---

## 在链路中的位置
承接标准化查询，向生成层交付少量高相关证据。这是整条链路里唯一能同时影响正确性、延迟和 token 成本的阶段。

## 实际执行顺序
权限与元数据过滤 → 多通道召回（关键词 + 向量）→ 结果融合 → 去重 → 重排 → 按上下文预算截断。权限过滤必须在召回阶段完成，不能等生成阶段再筛。

## 三级数量收缩
召回若干十到上百条候选，重排保留几十条，最终进上下文的通常只有个位数。三个数字要一起调：召回数决定上限，重排数决定延迟，入窗数决定 token 成本。细节见 [混合检索](note://rag-retriever-hybrid) 与 [Top-K 与延迟](note://rag-reranker-topk-latency)。

## 怎么判断这一层是否合格
用固定问题集测 Recall@K 和正确证据的命中排名：召回不到就是召回层的问题，召回到了但排名靠后就是重排的问题，两者都没问题而答案仍错，才轮到生成层排查。
