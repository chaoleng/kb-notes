---
version: 1
id: ai-dev-confidentiality-layer
title: 保密与脱敏层、安全默认值
tags:
  - 安全
  - 架构
  - Agent
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: 出站内容先过本地脱敏与策略判定再发模型，返回后本地回填，执行期另有一套权限默认值。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# 保密与脱敏层、安全默认值

> 出站内容先过本地脱敏与策略判定再发模型，返回后本地回填，执行期另有一套权限默认值。

## 脱敏层的位置与检测矩阵

Confidentiality Layer 夹在“Agent 生成内容”和“发往远程 LLM”之间，本身是确定性 Skill，不调用任何模型。

| 检测对象 | 工具 | 处理方式 |
|---|---|---|
| 通用 PII：邮箱、手机、证件、信用卡、IP | Microsoft Presidio（本地开源） | 替换为占位符 |
| 密钥、密码、服务器地址、连接串 | gitleaks / detect-secrets | 命中即硬拦截，本地占位，不接受半脱敏 |
| 客户名、项目代号 | 自定义 glossary（本地） | 按用户登记的映射表替换 |

## 令牌化与分级放行

可逆令牌化的路径是：真实内容在本地脱敏成占位符后发出，模型返回的文本再用本地映射表回填，最后写入本地文件；映射表只留在本地并可加密，绝不随 prompt 出境。完整调用链固定为 `内容 → 本地扫描 → 令牌化 → policy decision → LLM Gateway → 本地回填 → artifact`，中间任何一环失败都不发送。敏感度分三级：`public` 可用配置内的供应商，`confidential` 只能走经批准的零数据保留供应商，`restricted` 默认限本地模型，Ollama 与 llama.cpp 是这一级的逃生舱。

## 外部送信ログ

Gateway 每次调用生成一个 `call_id`，记 provider 与 model、所属阶段、令牌数、耗时、脱敏摘要的 hash、策略版本，汇总成审计成果物。反过来，原始 prompt、原始 response、令牌映射表和客户机密一律不记录——审计需要的是“何时向谁发了多少”，不是内容本身。

## 执行期默认值

项目外路径只读，写入必须落在项目根或 `--repo` 指定的根内，`../` 逃逸、未授权命令、未批准的远程 URL、危险 shell 参数一律拒绝。外部工具用 argv 数组调起，配固定 cwd、环境变量 allowlist 和 timeout，禁止动态拼接命令行，禁止未经批准的 `curl|sh`、安装脚本、真实 terraform apply 和破坏性 DB 操作。需求文本只当数据看待，不得被解释成命令、路径或权限。工具的 stdout 与 stderr 先写受控日志、再做 secret redact、然后才生成证据文件，审计事件只追加不修改。
