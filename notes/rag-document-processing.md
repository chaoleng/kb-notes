---
version: 1
id: rag-document-processing
title: RAG：文档采集、清洗与切分
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 将网页、PDF、Markdown、数据库记录等原始资料转换为边界清晰的知识片段。
created: 2026-07-23T04:42:22.072Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-knowledge-base
  - rag-concept-chunking
---

## 采集
统一接入网页、PDF、Office、Markdown、代码仓和数据库记录。入库时固定记录来源标识、抓取时间、文档版本和权限范围，后续所有片段都继承这组字段。

## 解析的难点在非文本
表格、代码块、公式和扫描件是解析阶段的主要失败源。表格转成纯文本会丢失行列对应关系，应保留为 Markdown 表格或结构化字段；扫描件需要 OCR，且要记录置信度，低置信度页面宁可不入库也不要污染检索结果。

## 清洗
去掉导航、页眉页脚、广告和重复模板文本，保留标题层级、列表结构和代码缩进。重复模板不清理，会在向量空间里形成一批彼此高度相似却毫无信息量的片段。

## 交接给切分
清洗后的产物应当是带标题路径的结构化文本，切分策略本身见 [Chunking](note://rag-concept-chunking)。验收方式：随机抽 20 条片段，逐条判断脱离原文后是否仍能独立看懂、是否能回溯到具体章节。
