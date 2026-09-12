---
version: 1
id: omp-harness-context-caching
title: omp Harness：上下文缓存与节流
tags:
  - omp
  - harness
  - 上下文
source: omp harness (oh-my-pi) 工具契约
summary: 只把必要片段读进上下文窗口，大产物截断外置为可寻址引用，通过委派进一步压缩，避免把整文件或整日志塞进对话。
created: 2026-09-12T00:00:00.000Z
updated: 2026-09-12T00:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-file-io
---

# omp Harness：上下文缓存与节流

> 只把必要片段读进上下文窗口，大产物截断外置为可寻址引用，通过委派进一步压缩，避免把整文件或整日志塞进对话。

## 核心细节

**读取节流：**

- `read` 用 offset/limit 和行选择器（`file:50-200`、`:-60` 尾部、`:5-16,960-973` 多段、`:raw`），只取需要的行。
- 源码**结构摘要优先**：无选择器读代码只返回声明骨架、省略函数体，页脚给出可恢复的行范围，需要时只重读那几段。

**输出外置：**

- `bash`/工具的大输出会被截断并链接为 `artifact://<id>`，用 `:N-M` 分页取回，不塞回上下文。
- 给子 Agent 传大 payload 用 `local://<name>.md` URI，而非内联文本。
- 大块一次性内容（日志、长文件、网页）走 `aegis-offload` / `ctx_store`，对话里只留 id 和摘要。

**委派省 context：**

- 用只读 `scout` 做探索式研究，主线程不必自己翻大量文件。
- 专用轻量子 Agent（如 cavecrew 系列）返回的 tool-result 更小，定位/小改动/看 diff 都比通用 Agent 省上下文。

## 所属模块
[omp 编码 Agent Harness](note://omp-harness)

## 学习提示
默认假设"读进来的东西都要花 token"，所以先问能不能用行范围、结构摘要或 id 引用替代整块内容。
