---
version: 1
id: rag-rag-architecture
title: RAG（检索增强生成）：RAG 系统架构
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 从数据源、索引、检索、上下文编排到模型生成，RAG 是多个组件协作的系统。
created: 2026-07-23T11:55:16.747Z
updated: 2026-07-23T11:55:16.747Z
favorite: false
related:
  - rag-concept-rag
---

# RAG（检索增强生成）：RAG 系统架构

> 从数据源、索引、检索、上下文编排到模型生成，RAG 是多个组件协作的系统。

## 核心细节
架构通常分离为离线知识加工链路和在线问答链路。离线侧负责解析、清洗、切分、向量化和索引；在线侧负责查询改写、召回、重排、上下文拼接和生成。系统边界还应包含权限、来源追踪、缓存和评估。

## 所属模块
[RAG（检索增强生成）](note://rag-concept-rag)

## 学习提示
先理解该节点解决的问题，再结合父模块观察它在 RAG 链路中的输入、输出和失败边界。