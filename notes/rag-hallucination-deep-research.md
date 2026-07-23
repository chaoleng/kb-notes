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
updated: 2026-07-23T13:15:37.875Z
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

## Factuality 与 Faithfulness
- **Factuality**：回答是否符合现实中可验证的事实。
- **Faithfulness**：回答是否被当前检索上下文支持。
- “事实正确但没有证据”仍然不是可靠的 RAG 回答。

## 幻觉形成链路
数据层 → 训练层 → 检索层 → 上下文层 → 生成层 → 验证层。

## 诊断路径
1. 原始资料中是否存在答案？
2. 正确片段是否被召回？
3. 模型是否正确使用证据？
4. 引用是否真正支持结论？
5. 来源本身是否正确、有效且未过期？

## 评估方法
使用原子事实分解、Faithfulness、Citation precision/recall、Recall@K、MRR、拒答质量和线上失败切片；FActScore 可表示为“被支持的原子事实数 / 原子事实总数”。

## 缓解架构
知识源版本治理 → 混合检索与重排 → 证据充分性判断 → 证据约束生成 → 原子事实与引用校验 → 风险分级拒答。

## 相关研究
TruthfulQA、SelfCheckGPT、FActScore、RAGTruth 和 RAG Faithfulness 研究分别覆盖真实度测试、黑盒一致性检测、原子事实评估、RAG 幻觉标注和证据忠实度。

## 所属模块
[幻觉（Hallucination）](note://rag-concept-hallucination)

## 研究分支
- [事实正确性与证据忠实度](note://rag-hallucination-research-factuality)：区分 Factuality 与 Faithfulness，避免把碰巧正确当成可靠回答。
- [幻觉形成链路与诊断](note://rag-hallucination-research-causal-chain)：沿数据、训练、检索、上下文、生成和验证链路定位错误来源。
- [幻觉检测与评估](note://rag-hallucination-research-evaluation)：使用原子事实、Faithfulness、FActScore、引用指标和拒答质量建立评估闭环。
- [幻觉缓解架构](note://rag-hallucination-research-mitigation)：用知识治理、混合检索、证据门控、约束生成和生成后校验降低风险。