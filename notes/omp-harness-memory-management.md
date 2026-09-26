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
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - omp-harness
  - omp-harness-context-caching
---

# omp Harness：记忆管理

> 把记忆分成短期上下文、可寻址持久记忆和不进真相源的内部记忆三层，明确什么进上下文、什么落持久、什么只作过程记忆。

## 三层记忆划分

- **短期上下文**：当前对话窗口，最贵也最有限，只放这一步正在使用的信息。
- **持久记忆（可寻址）**：`artifact://<id>` 存放溢出的大产物，`history://<id>` 是只读会话记录（live/parked/released），`local://<name>.md` 承载跨子 Agent 共享的长文本；三者都靠 id 引用，不占对话正文。
- **内部记忆（不进真相源）**：`todo` 清单是 Agent 的过程记忆，会自动推进 `in_progress` 状态，但中间计划与自省不应混进最终交付说明。

## 跨 Agent 的记忆传递

`hub` 负责 Agent 之间的消息（`send` / `wait` / `inbox`）与后台作业投递，作业完成会自动送达，不需要轮询。子 Agent 是空白起手的：它看不到父对话历史，所以派发时必须写自包含指令，公共约束放进批次 `context`，超过几行的输入一律换成 `local://` 引用而不是内联粘贴。

## 大块内容卸载

日志、长文件、抓取回来的网页这类一次性素材走 `ctx_store` / `aegis-offload` 移出对话，窗口里只留下 id 和一句摘要，需要细节时再按 id 取回指定片段。

## 分层判断准则

一条信息只要会被复用第二次，或者体量到了几千字，就该落成可寻址产物而不是留在窗口里；只服务当前这一步的片段留在短期上下文；纯过程性的排期与取舍留在内部记忆。错层的代价很具体：该外置的没外置，窗口被日志挤爆；该持久的没持久，同一份文件被反复重读，token 成倍消耗。
