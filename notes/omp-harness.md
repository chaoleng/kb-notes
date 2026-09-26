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
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - omp-harness-memory-management
  - omp-harness-context-caching
  - omp-harness-file-io
  - omp-harness-delegation
  - omp-harness-task-state
  - omp-harness-tool-policy
  - omp-harness-verification
---

# omp 编码 Agent Harness：上下文与记忆管理

> omp 这类编码 Agent harness 通过工具原语、内部与持久记忆分层、以及上下文节流三条机制管理有限的上下文窗口。

## 上下文约束下的三层设计

编码 Agent 的根本约束是**上下文窗口有限**，而任务涉及的代码、日志、历史远超窗口。harness 用三层机制应对：

1. **记忆管理**：区分短期上下文、可寻址持久记忆和不进真相源的内部记忆。见 [记忆管理](note://omp-harness-memory-management)。
2. **上下文缓存与节流**：只把必要片段读进窗口，大产物一律外置为可寻址引用。见 [上下文缓存](note://omp-harness-context-caching)。
3. **文件读写**：用带快照指纹的专用原语操作文件，而非把整文件塞进对话。见 [文件读写](note://omp-harness-file-io)。

## 省 token 之外的四条契约

窗口省下来还不够，产出是否可靠取决于另外四件事：

- [子 Agent 委派与并行编排](note://omp-harness-delegation)：任务自包含、批量派发、按文件所有权拆并发。
- [待办与阶段状态管理](note://omp-harness-task-state)：把多步任务外化成可检查的状态，而不是靠上下文记忆跟进度。
- [工具策略](note://omp-harness-tool-policy)：专用原语优先于 shell 等价物，shell 只留给真正的外部二进制。
- [交付前的验证契约](note://omp-harness-verification)：跑真东西而不是跑测试文件，声明完成不等于产物可用。

## 关键原语一览

- 读取/检索：`read`（行选择器、结构摘要）、`glob`、`grep`
- 变更：`edit`（`#TAG` 乐观锁）、`write`
- 记忆/编排：`todo`、`hub`、`task`（子 Agent）
- 寻址：`artifact://`、`history://`、`local://`、`ctx_store` / `aegis-offload`
