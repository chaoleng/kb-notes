---
version: 1
id: rag-llm-decoding
title: 大语言模型（LLM）：LLM 解码与生成参数
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。
created: 2026-07-23T11:55:26.779Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-llm
---

# 大语言模型（LLM）：LLM 解码与生成参数

> temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。

## 参数各自在改什么
temperature 缩放 logits，值越大低概率词越容易被选中。top_p 按累积概率截断候选集，top_k 按固定个数截断，两者同时开启时取交集。repetition_penalty 对已出现 token 的 logit 打折以抑制复读。max_tokens 只决定何时停下，不改变分布形状。

## RAG 场景的推荐区间
知识问答把 temperature 设在 0.1 到 0.3，top_p 设 0.8 到 0.9，top_k 关掉或设 40 以上让 top_p 主导。repetition_penalty 保持 1.0 到 1.05；超过 1.2 会让模型回避原文中反复出现的专有名词和数字，反而改写掉正确内容。

## 不要把 temperature=0 当万能开关
贪心解码确实让输出可复现，但它同时放大了模型的先验偏好：证据模糊时，模型会稳定地选那个最像答案的说法，错误也随之固定，靠重跑发现不了。保留 0.1 到 0.2 的温度并采样多次做自洽性比对，更容易暴露不可靠的回答。

## 最大输出长度的隐性代价
max_tokens 给得过小会在引用列表处截断，让校验器误判为没有引用；给得过大则鼓励模型展开没有证据支撑的补充说明。按任务实测的 p95 输出长度再加 20% 设定比较稳妥。