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
updated: 2026-07-23T05:22:37.284Z
favorite: false
related:
  - rag-concepts
---

## 定义
幻觉是答案流畅、形式正确，但内容没有证据支持、与来源冲突或凭空编造。

## RAG 中的来源
检索不到答案、召回了错误片段、上下文互相矛盾、Prompt 约束不足，或模型把不确定信息当成确定事实。

## 降低方法
提高知识新鲜度和召回质量；做重排序；要求引用和证据不足时说明未知；增加 Faithfulness 评估和失败样本回归。

## 误区
接入 RAG 不会自动消除幻觉。错误知识、错误检索和错误引用仍可能产生更“有根据外观”的幻觉。