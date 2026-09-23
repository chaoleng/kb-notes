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
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-file-io
  - omp-harness-memory-management
---

# omp Harness：上下文缓存与节流

> 只把必要片段读进上下文窗口，大产物截断外置为可寻址引用，通过委派进一步压缩，避免把整文件或整日志塞进对话。

## 读取节流

`read` 支持 offset/limit 与行选择器：`file:50-200` 取区间、`:-60` 取尾部、`:5-16,960-973` 一次取多段、`:raw` 跳过转换。源码在无选择器时默认返回结构摘要，只给声明骨架并省略函数体，页脚列出可恢复的行范围，确认目标后只重读那几段，而不是把整个文件铺进窗口。

## 输出外置

`bash` 和各类工具的大输出会被自动截断并链接成 `artifact://<id>`，用 `:N-M` 分页取回而不是原样塞回对话。派给子 Agent 的长输入写进 `local://<name>.md` 再传 URI。日志、长文档、网页正文交给 `aegis-offload` / `ctx_store`，对话里只保留 id 与摘要。

## 委派压缩

探索式研究交给只读的 scout，主线程不必亲自翻几十个文件，只接收压缩后的结论。定位、小改动、看 diff 这类窄任务用轻量子 Agent，其 tool-result 体积远小于通用 Agent 的完整过程。

## 节流的判断顺序

每次要把内容拉进窗口前按顺序自问三步：能不能用行范围或结构摘要代替整块？能不能只留 id、需要时再取？能不能让子 Agent 读完只回结论？三问都否才允许整块进上下文。反过来，反复对同一文件做无选择器全量读，是窗口被吃光的最常见原因。
