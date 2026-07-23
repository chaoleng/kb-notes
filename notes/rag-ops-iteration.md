---
version: 1
id: rag-ops-iteration
title: RAG：知识更新与线上迭代
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 通过增量索引、版本管理、监控和失败样本回流，让知识库持续保持新鲜和可靠。
created: 2026-07-23T04:42:47.048Z
updated: 2026-07-23T04:42:47.048Z
favorite: false
related:
  - rag-evaluation
---

## 知识更新
使用内容哈希识别新增、修改和删除，增量更新索引；记录文档版本和生效时间。

## 线上监控
跟踪延迟、检索为空、低置信度、用户反馈、引用缺失和权限拒绝。

## 迭代方法
把失败问答加入回归集，先判断是数据缺失、切分问题、检索问题还是生成约束问题，再做最小修改并重新评估。