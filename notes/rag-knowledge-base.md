---
version: 1
id: rag-knowledge-base
title: RAG：知识库构建
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把原始文档加工成可检索知识的主干，包括采集、清洗、切分、向量化和索引。
created: 2026-07-23T04:42:19.529Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag
  - rag-document-processing
  - rag-embedding-index
---

## 在链路中的位置
离线侧的全部工作。线上检索只能在这里产出的片段集合里找答案，这一层丢掉的信息，任何重排和 Prompt 技巧都补不回来。

## 主流程
文档采集 → 格式解析 → 清洗 → 切分（见 [Chunking](note://rag-concept-chunking)）→ 元数据补充 → 向量化与建索引（见 [Embedding 与索引](note://rag-embedding-index)）。

## 必须随片段一起落库的元数据
来源文件与 URL、章节标题路径、更新时间、文档版本、权限/租户范围、原文偏移或页码。缺任何一项，线上都会出现「答得对但引用不回去」或「越权看到不该看的内容」。

## 可运维性要求
索引必须支持按文档 id 的增量更新与删除，而不是每次全量重建；每条片段要能反查到源文档，也要能从源文档正查到它产生的全部片段，否则文档下线时清不干净。
