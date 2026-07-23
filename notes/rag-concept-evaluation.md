---
version: 1
id: rag-concept-evaluation
title: 概念：RAG 评估
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 评估检索证据、答案质量、事实忠实度、延迟成本和知识新鲜度的体系。
created: 2026-07-23T05:22:39.822Z
updated: 2026-07-23T11:57:00.716Z
favorite: false
related:
  - rag-concepts
  - rag-evaluation-dataset
  - rag-evaluation-metrics
  - rag-evaluation-online-monitoring
---

## 定义
RAG 评估不是只看最终答案是否像人话，而是分别观察检索、生成和系统运行质量。

## 主要维度
- 检索：正确证据是否被召回，是否排名靠前。
- 生成：答案相关性、完整性和事实忠实度。
- 可验证性：关键结论是否有正确引用。
- 系统：延迟、成本、稳定性、权限和更新及时性。

## 方法
建立带参考答案和参考证据的问题集，记录每次检索与回答，按失败类型回归测试。

## 详细分支
- [评估数据集](note://rag-evaluation-dataset)：由真实问题、参考证据、参考答案和难例组成的可重复测试集。
- [检索与生成指标](note://rag-evaluation-metrics)：检索关注 Recall@K、Precision、MRR；生成关注相关性、完整性、Faithfulness 和引用正确性。
- [线上监控与反馈闭环](note://rag-evaluation-online-monitoring)：记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。