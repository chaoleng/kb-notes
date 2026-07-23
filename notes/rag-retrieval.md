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
updated: 2026-07-23T04:42:27.223Z
favorite: false
related:
  - rag
  - rag-vector-search
  - rag-hybrid-rerank
---

## 节点位置
承接问题理解和知识库，输出给增强生成阶段。

## 检索链路
查询 → 权限/元数据过滤 → 候选召回 → 去重 → 重排序 → 截取上下文。

## 关键平衡
召回太少会漏掉答案，召回太多会增加噪声和上下文成本。应根据问题类型动态调整数量。

## 验证指标
关注召回率、命中位置、片段相关性、来源覆盖和最终答案是否引用了正确片段。