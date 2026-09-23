---
version: 1
id: rag-hallucination-deep-research
title: 幻觉：深入研究
tags:
  - RAG
  - 概念
  - 细节
  - 深入研究
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 从事实正确性、证据忠实度、形成链路、诊断方法、评估指标和缓解架构深入研究 LLM/RAG 幻觉。
created: 2026-07-23T12:44:17.029Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-hallucination
  - rag-hallucination-research-factuality
  - rag-hallucination-research-causal-chain
  - rag-hallucination-research-evaluation
  - rag-hallucination-research-mitigation
---

# 幻觉：深入研究

## 研究定位
幻觉不是单一的模型错误，而是数据、训练、检索、上下文、生成、引用和评估共同作用的系统性问题。

## 研究框架
这条研究线沿四个问题展开，细节各自成篇，本页只做定位与串联：

1. 判什么——事实正确性与证据忠实度是两个独立维度（见 [事实正确性与证据忠实度](note://rag-hallucination-research-factuality)）。
2. 错在哪——幻觉沿数据、训练、检索、上下文、生成、验证六层传导（见 [幻觉形成链路与诊断](note://rag-hallucination-research-causal-chain)）。
3. 怎么量——原子事实分解、FActScore、引用精度与召回、拒答质量（见 [幻觉检测与评估](note://rag-hallucination-research-evaluation)）。
4. 怎么防——六道关卡与按风险分级的门控（见 [幻觉缓解架构](note://rag-hallucination-research-mitigation)）。

## 与工程视角的分工
概念树里的 [幻觉成因](note://rag-hallucination-causes)、[幻觉类型](note://rag-hallucination-types)、[幻觉缓解](note://rag-hallucination-mitigation) 面向日常排查，给的是可观测信号与按成本排序的手段；本研究线面向评估体系与论文口径，给的是指标定义与实验方法。两边不互相复制结论。

## 相关研究
TruthfulQA、SelfCheckGPT、FActScore、RAGTruth 和 RAG Faithfulness 研究分别覆盖真实度测试、黑盒一致性检测、原子事实评估、RAG 幻觉标注和证据忠实度。