---
version: 1
id: rag-concept-grounding
title: 概念：Grounding（事实依据）
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 让模型输出的关键结论能够被检索证据支持并回溯到原始来源。
created: 2026-07-23T05:22:34.550Z
updated: 2026-07-23T11:56:56.255Z
favorite: false
related:
  - rag-concepts
  - rag-grounding-citation
  - rag-grounding-faithfulness
  - rag-grounding-conflict
---

## 定义
Grounding 指回答与外部证据之间的可验证对应关系：答案中的关键陈述应能在给定资料中找到支持。

## 表现
引用文档、章节或片段位置；区分资料事实、模型推断和未知信息；证据不足时拒答或明确说明。

## 与幻觉的关系
Grounding 越弱，模型越可能用自身先验补齐空白。它不能保证绝对正确，但能提高可核验性和问题定位能力。

## 详细分支
- [引用与来源定位](note://rag-grounding-citation)：把答案中的关键结论连接到文档、章节、URL 或片段位置。
- [答案忠实度](note://rag-grounding-faithfulness)：判断答案是否被检索证据支持，区分资料事实、模型推断和未知信息。
- [证据冲突处理](note://rag-grounding-conflict)：当多个来源对同一事实不一致时，按版本、时间、权威等级和适用范围进行判断。