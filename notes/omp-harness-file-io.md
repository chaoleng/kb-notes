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
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-context-caching
---

# omp Harness：文件读写

> 用带快照指纹的专用读写检索原语操作文件，读靠选择器切片、写靠行锚定补丁与乐观锁，专用工具一律优先于 shell。

## 读取与快照指纹

`read` 覆盖文件、目录、归档成员、SQLite 表、图片、文档与 URL；带选择器时返回快照头 `[FILE#TAG]` 加编号行，`#TAG` 就是这次快照的指纹。目录路径直接列条目，源码在无选择器时给结构摘要。指纹的意义在于：后续编辑必须声明自己基于哪一份快照。

## 行锚定补丁与乐观锁

`edit` 是行锚定的补丁语言，头部必须写最新 `read` 给出的 `#TAG`，正文用 `PUT N.=M` 覆盖区间、`PUT N*` 覆盖整个语法块、`CUT` 删除并捕获。一旦文件被改动，`#TAG` 失效且行号重排，必须重读才能继续——这就是乐观锁：基于陈旧快照的补丁会被直接拒绝，而不是盲写覆盖别人刚落地的修改。

## 写入与检索原语

`write` 负责创建或整体覆盖，也能写归档条目与 SQLite 行；小范围改动一律用 `edit` 做外科式修改，不做整文件重写。检索侧 `glob` 找路径、`grep` 按 Rust regex 搜内容并支持跨行与分页，替代 `ls`、`find`、`rg` 这些 shell 等价物。

## 典型闭环

一次安全修改的固定节奏是：`grep` 定位到行 → `read` 取那一段并拿到 `#TAG` → `edit` 基于该指纹落补丁 → 编辑返回新行号与新指纹，作为下一次改动的基准。跳过任一步，要么改错位置，要么覆盖并发改动。
