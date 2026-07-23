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
updated: 2026-07-23T04:42:19.529Z
favorite: false
related:
  - rag
  - rag-document-processing
  - rag-embedding-index
---

## 节点位置
RAG 的离线基础设施。在线回答质量很大程度取决于这里是否保留了完整、准确、可定位的知识。

## 主流程
文档采集 → 格式解析 → 清洗 → 语义切分 → 元数据补充 → Embedding → 建立索引。

## 必须保留的元数据
来源文件、章节标题、更新时间、版本、权限范围和原文定位信息。

## 质量原则
切分不能破坏语义；索引必须支持增量更新和删除；每个片段都应能回溯到原始来源。