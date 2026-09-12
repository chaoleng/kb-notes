---
version: 1
id: omp-harness-memory-management
title: omp Harness：记忆管理
tags:
  - omp
  - harness
  - 记忆
source: omp harness (oh-my-pi) 工具契约
summary: 把记忆分成短期上下文、可寻址持久记忆和不进真相源的内部记忆三层，明确什么进上下文、什么落持久、什么只作过程记忆。
created: 2026-09-12T00:00:00.000Z
updated: 2026-09-12T00:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-context-caching
---

# omp Harness：记忆管理

> 把记忆分成短期上下文、可寻址持久记忆和不进真相源的内部记忆三层，明确什么进上下文、什么落持久、什么只作过程记忆。

## 核心细节

**三层记忆：**

- **短期上下文**：当前对话窗口，最贵、最有限，只放正在用的信息。
- **持久记忆（可寻址）**：`artifact://<id>` 溢出产物、`history://<id>` 只读会话记录（live/parked/released）、`local://<name>.md` 跨子 Agent 共享内容——用 id 引用，不占对话正文。
- **内部记忆（不进真相源）**：`todo` 任务清单是 Agent 的过程记忆，会自动推进 `in_progress`，但**不是状态真相源**，中间计划和自省不应污染最终审计。

**跨 Agent 记忆：**

- `hub` 负责 Agent 间消息（`send`/`wait`/`inbox`）与后台作业投递；作业完成自动送达，无需轮询。
- 子 Agent **空白起手**：没有父对话历史，必须给自包含指令，用共享 `context` 传契约；大 payload 走 `local://` 而非内联。

**卸载：** 大块一次性内容（日志、长文件、抓取网页）用 `ctx_store` / `aegis-offload` 移出对话，只在对话里留 id 和摘要，需要时再取回。

## 所属模块
[omp 编码 Agent Harness](note://omp-harness)

## 学习提示
判断每条信息该进哪一层：正在用→短期；以后可能查→持久可寻址；只是过程计划→内部记忆，绝不进真相源。
