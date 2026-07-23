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
updated: 2026-07-23T04:42:22.072Z
favorite: false
related:
  - rag-knowledge-base
---

## 采集
统一接入网页、PDF、Office、Markdown、数据库和内部系统，记录来源与版本。

## 清洗
去除导航、重复页眉页脚、乱码和无意义空白；表格、代码和列表要保留结构。

## 切分
优先按标题、段落、列表和语义边界切分，再设置适度重叠。过大降低检索精度，过小会丢失上下文。

## 验证
随机抽查片段是否可独立理解，并确认每个片段都带有可回溯的来源定位。