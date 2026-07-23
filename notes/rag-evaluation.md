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
updated: 2026-07-23T04:42:42.313Z
favorite: false
related:
  - rag
  - rag-quality-evaluation
  - rag-ops-iteration
---

## 评估层次
1. 检索层：是否召回正确资料，相关片段排名是否靠前。
2. 生成层：答案是否正确、完整、忠实于证据。
3. 系统层：延迟、成本、稳定性、权限和知识新鲜度。

## 闭环
建立代表性问题集 → 记录检索与回答 → 标注失败类型 → 针对性调整切分、Embedding、检索、Prompt 或模型 → 回归验证。

## 目标
不是盲目追求更长上下文，而是用最少、最可靠的证据生成可验证答案。