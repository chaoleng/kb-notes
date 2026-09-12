---
version: 1
id: omp-harness-file-io
title: omp Harness：文件读写
tags:
  - omp
  - harness
  - 文件
source: omp harness (oh-my-pi) 工具契约
summary: 用带快照指纹的专用读写检索原语操作文件，读靠选择器切片、写靠行锚定补丁与乐观锁，专用工具一律优先于 shell。
created: 2026-09-12T00:00:00.000Z
updated: 2026-09-12T00:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-context-caching
---

# omp Harness：文件读写

> 用带快照指纹的专用读写检索原语操作文件，读靠选择器切片、写靠行锚定补丁与乐观锁，专用工具一律优先于 shell。

## 核心细节

**读（`read`）：** 可读文件、目录、归档、SQLite、图片、文档、URL；支持行选择器（范围、`:raw`、多段）；返回带快照头 `[FILE#TAG]` 的带号行，`#TAG` 是后续锚定编辑的指纹；目录路径列条目；源码无选择器时返回结构摘要。

**写（`edit` / `write`）：**

- `edit` 是**行锚定补丁语言**，必须引用最新 `read` 的 `#TAG`；一旦改动，`#TAG` 失效、行号重排，需要重读——这是**乐观锁**：基于陈旧内容的编辑会被拒绝，防止盲改。
- `write` 用于创建/覆盖整文件，也支持写归档条目和 SQLite 行。
- 原则：小改动用 `edit` 做外科式修改，不整文件重写。

**检索（`glob` / `grep`）：** `glob` 找路径、`grep` 正则搜内容（Rust regex，可跨行/分页），取代 shell 的 `ls`/`find`/`grep`。

**纪律：** 专用工具优先于 shell——shell 只留真实二进制和短管道；文件读、写、检索、代码智能都走对应专用工具，保证输出可控、可寻址、可审计。

## 所属模块
[omp 编码 Agent Harness](note://omp-harness)

## 学习提示
记住"读→拿 `#TAG`→基于该指纹编辑"的闭环；指纹一变就重读，是避免覆盖他人改动的关键。
