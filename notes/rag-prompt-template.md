---
version: 1
id: rag-prompt-template
title: Prompt：Prompt 模板结构
tags:
  - RAG
  - 概念
  - 细节
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: 把角色规则、用户问题、检索证据、引用要求和输出格式分成清晰区块。
created: 2026-07-23T11:56:08.346Z
updated: 2026-09-23T10:30:00.000Z
favorite: false
related:
  - rag-concept-prompt
---

# Prompt：Prompt 模板结构

> 把角色规则、用户问题、检索证据、引用要求和输出格式分成清晰区块。

## 五个区块怎么分隔
模板固定切成规则、用户问题、检索证据、引用要求、输出格式五块，块间用 `<rules>`、`<question>`、`<evidence>` 这类闭合标签包裹，比用一行短横线更难被文档正文伪造。规则区只写角色、可回答范围和拒答条件，不混进任何检索结果。

## 让证据可被引用
每个片段以 `[3] title=… | source=… | date=…` 开头，编号在同一次请求内唯一且连续，原文紧跟其后。引用要求写成硬约束：每个结论句末尾必须带方括号编号，编号只能取自证据区；后处理用正则比对编号集合，出现证据里不存在的编号就判为幻觉并触发重答。

## 输出 JSON 的约束写法
需要结构化输出时把字段清单写死（answer: string、citations: number[]、insufficient: boolean），只给一个最小示例避免模型照抄示例内容，并显式禁止代码围栏和解释性前后缀。能用 response_format 或 function calling 在解码层约束的，就不要只靠自然语言描述格式。

## 模板当代码管
模板带版本号入库，改动灰度发布并记录命中版本；FAQ、多跳推理、表格问数各维护一套模板，而不是塞进一个巨模板里用条件分支切换。
