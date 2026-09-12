---
version: 1
id: omp-harness
title: omp 编码 Agent Harness：上下文与记忆管理
tags:
  - omp
  - harness
  - Agent
source: omp harness (oh-my-pi) 工具契约
summary: omp 这类编码 Agent harness 通过工具原语、内部与持久记忆分层、以及上下文节流三条机制管理有限的上下文窗口。
created: 2026-09-12T00:00:00.000Z
updated: 2026-09-12T00:00:00.000Z
favorite: false
related:
  - omp-harness-memory-management
  - omp-harness-context-caching
  - omp-harness-file-io
---

# omp 编码 Agent Harness：上下文与记忆管理

> omp 这类编码 Agent harness 通过工具原语、内部与持久记忆分层、以及上下文节流三条机制管理有限的上下文窗口。

## 核心机制

编码 Agent 的根本约束是**上下文窗口有限**，而任务涉及的代码、日志、历史远超窗口。omp harness 用三层设计应对：

1. **记忆管理**：区分短期上下文、可寻址持久记忆和不进真相源的内部记忆。见 [记忆管理](note://omp-harness-memory-management)。
2. **上下文缓存/节流**：只把必要片段读进窗口，大产物一律外置为可寻址引用。见 [上下文缓存](note://omp-harness-context-caching)。
3. **文件读写**：用带快照指纹的专用读写原语，而非把整文件塞进对话。见 [文件读写](note://omp-harness-file-io)。

## 关键原语一览

- 读取/检索：`read`（行选择器、结构摘要）、`glob`、`grep`
- 变更：`edit`（`#TAG` 乐观锁）、`write`
- 记忆/编排：`todo`、`hub`、`task`（子 Agent）
- 寻址：`artifact://`、`history://`、`local://`、`ctx_store` / `aegis-offload`

## 学习提示
先理解"上下文窗口有限"这个约束，再看三篇子笔记如何分别用记忆分层、读取节流和可寻址外置来省 token。
