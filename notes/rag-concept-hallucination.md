---
version: 1
id: rag-concept-hallucination
title: 概念：幻觉（Hallucination）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 模型生成看似合理但缺乏事实依据或与证据冲突的内容。
created: 2026-07-23T05:22:37.284Z
updated: 2026-07-23T12:44:21.004Z
favorite: false
related:
  - rag-concepts
  - rag-hallucination-types
  - rag-hallucination-causes
  - rag-hallucination-mitigation
  - rag-hallucination-deep-research
---

## 定义
幻觉是答案流畅、形式正确，但内容没有证据支持、与来源冲突或凭空编造。

## RAG 中的来源
检索不到答案、召回了错误片段、上下文互相矛盾、Prompt 约束不足，或模型把不确定信息当成确定事实。

## 降低方法
提高知识新鲜度和召回质量；做重排序；要求引用和证据不足时说明未知；增加 Faithfulness 评估和失败样本回归。

## 误区
接入 RAG 不会自动消除幻觉。错误知识、错误检索和错误引用仍可能产生更“有根据外观”的幻觉。

## 详细分支
- [幻觉类型](note://rag-hallucination-types)：包括无依据编造、引用错配、数字错误、实体混淆和把推断说成事实。
- [幻觉成因](note://rag-hallucination-causes)：常见根因有知识缺失、召回错误、证据冲突、上下文过载和模型过度推断。
- [幻觉缓解](note://rag-hallucination-mitigation)：通过更好的知识更新、混合检索、证据约束、引用检查、拒答策略和回归评估降低风险。
- [幻觉深入研究](note://rag-hallucination-deep-research)：从事实正确性、证据忠实度、诊断、评估和缓解架构深入研究幻觉。