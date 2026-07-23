---
version: 1
id: rag-retriever-lexical-vector
title: 检索器（Retriever）：关键词检索与向量检索
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: BM25 等关键词检索擅长精确术语，向量检索擅长语义相近表达。
created: 2026-07-23T11:55:53.478Z
updated: 2026-07-23T11:55:53.478Z
favorite: false
related:
  - rag-concept-retriever
---

# 检索器（Retriever）：关键词检索与向量检索

> BM25 等关键词检索擅长精确术语，向量检索擅长语义相近表达。

## 核心细节
产品型号、错误码、版本号和人名常需要关键词能力；自然语言描述和同义表达更适合向量能力。

## 所属模块
[检索器（Retriever）](note://rag-concept-retriever)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。