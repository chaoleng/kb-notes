---
version: 1
id: rag-conversation-context
title: RAG：多轮对话上下文
tags:
  - RAG
  - 知识库
  - AI应用
  - Agent
  - 大模型
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 从历史对话中解析指代、条件和用户偏好，形成当前检索所需的最小上下文。
created: 2026-07-23T04:42:17.239Z
updated: 2026-07-23T04:42:17.239Z
favorite: false
related:
  - rag-question-understanding
---

## 重点
多轮对话中的“它”“上一个方案”“这个版本”必须先解析，才能检索正确资料。

## 处理原则
- 只保留与当前问题相关的历史信息。
- 将已确认条件和待确认条件分开。
- 对时间、版本、权限等约束显式化。
- 上下文不确定时优先追问，不要让检索器猜测。