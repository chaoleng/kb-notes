---
version: 1
id: rag-hallucination-research-factuality
title: 事实正确性与证据忠实度
tags:
  - 幻觉
  - 深入研究
  - Factuality
  - Faithfulness
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ（原文框架）+ 工程实践补充
summary: 区分 Factuality 与 Faithfulness，避免把碰巧正确当成可靠回答。
created: 2026-07-23T13:15:26.518Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-hallucination-deep-research
---

# 事实正确性与证据忠实度

> 区分 Factuality 与 Faithfulness，避免把碰巧正确当成可靠回答。

## 两个维度互相独立
Factuality 问的是「这句话在现实世界里成立吗」，Faithfulness 问的是「这句话能从本次检索到的证据里推出来吗」。二者可以任意组合：模型凭参数记忆答对但证据里没有（高 Factuality、低 Faithfulness），或忠实复述了一份过期文档（高 Faithfulness、低 Factuality）。

## 为什么 RAG 必须同时量
只测 Factuality，系统会退化成「模型自己编、偶尔蒙对」，无法复现也无法审计；只测 Faithfulness，知识库里的错误会被原样放大成带引用的权威答案。两个指标分开出分，才能区分是知识源要治理还是生成约束要收紧。

## 评估方式不同
Faithfulness 是封闭判定：给定证据与答案，逐条原子事实判蕴含/矛盾/无关，可自动化。Factuality 是开放判定：需要外部权威源或人工核对，成本高得多，通常只对高风险问题抽样做。

## 工程含义
知识库版本更新后，Faithfulness 分数可能纹丝不动而 Factuality 骤降——这正是「忠实地复述旧事实」的典型信号，必须靠文档生效时间和版本过滤来兜，而不是调 Prompt。
