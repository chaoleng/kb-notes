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
updated: 2026-07-23T05:22:39.822Z
favorite: false
related:
  - rag-concepts
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