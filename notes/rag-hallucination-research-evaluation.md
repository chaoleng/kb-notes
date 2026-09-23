---
version: 1
id: rag-hallucination-research-evaluation
title: 幻觉检测与评估
tags:
  - 幻觉
  - 深入研究
  - 评估
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 使用原子事实、Faithfulness、FActScore、引用指标和拒答质量建立评估闭环。
created: 2026-07-23T13:15:32.000Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-hallucination-deep-research
---

# 幻觉检测与评估

> 使用原子事实、Faithfulness、FActScore、引用指标和拒答质量建立评估闭环。

## 原子事实分解
把答案拆成不可再分的断言，每个数字、日期、条件限定各算一条，再逐条对证据判蕴含、矛盾或无关。FActScore 即「被证据支持的原子事实数 ÷ 原子事实总数」，分母透明，比笼统的「答案质量分」可归因得多。

## 引用侧指标
Citation precision 看给出的引用里有多少真正支持对应结论，Citation recall 看需要引用的结论里有多少给了引用。前者低说明模型乱挂引用，后者低说明大量结论在裸奔，两者要分开报。

## 拒答质量
在明知无答案的样本上统计正确拒答率，同时监控在有答案样本上的误拒率。只压前者会让系统变成「什么都不敢答」，两个数必须成对看。

## 可用的公开基准
TruthfulQA 测模仿性谎言，SelfCheckGPT 用多次采样的自洽性做黑盒检测，RAGTruth 提供 RAG 场景的逐段幻觉标注。公开集只用于横向比较模型，上线判据仍要用自建业务问题集。
