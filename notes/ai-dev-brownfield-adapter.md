---
version: 1
id: ai-dev-brownfield-adapter
title: Brownfield 三层适配与仓库角色隔离
tags:
  - 架构
  - 安全
  - Agent
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现
summary: Core 固定不变，项目与工具差异下沉到两层适配器，客户仓库与源码仓库的凭证和 remote 严格隔离。
created: 2026-09-23T11:00:00.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-agent-pipeline-architecture
---

# Brownfield 三层适配与仓库角色隔离

> Core 固定不变，项目与工具差异下沉到两层适配器，客户仓库与源码仓库的凭证和 remote 严格隔离。

## 三层结构

| 层 | 固定内容 | 可替换性 |
|---|---|---|
| Core | 状态机、checkpoint、manifest、审批、审计、脱敏 | 不可替换 |
| Project Adapter | 项目识别、目录规则、命令发现、构建与测试入口、文档模板 | 每个客户一份 |
| Tool Adapter | Git、包管理器、编译器、lint、扫描器、浏览器、MCP | 按技术栈注册 |

适配器接口只有四个方法：`detect(repo_root)→StackProfile`、`plan(profile,stage)→CommandPlan`、`run(command_plan,sandbox)→ToolResult`、`collect(profile,result)→Evidence[]`。栈适配矩阵覆盖 Python、Node、Java、Go、.NET、Ruby、PHP、Rust、Terraform 与 Salesforce，每栈各写识别证据、默认工具链与适配要点。

## 事实边界

现状扫描 Skill 以只读方式看客户代码，产出 `brownfield-inventory.json`，字段包括 languages、frameworks、build_commands、datastores、interfaces、constraints 和 unknowns，每项都带证据路径与置信度。`StackProfile` 进一步记语言、框架、包管理器、运行时版本、构建与测试命令、源码与生成目录、锁文件、部署方式，以及 `allowed_tools`、`forbidden_operations`、`unknowns`。适配器以能力矩阵声明支持范围，矩阵之外的门返回 `unsupported` 并转人工，不能拿一个假的 passed 蒙混过去。变更边界同样严格：默认只在项目根内读写，先给适配计划和变更清单再动手写代码，不借“修复环境”的名义整体升级依赖；破坏性 DB 迁移、公共 API 变更、运行时升级、基础设施变更各自需单独的人工承認。

## 两类仓库不许混用

`pi-pipeline` 自身的源码仓库按维护者授权和分支保护提交；`--repo` 指向的客户项目仓库按 Index 冻结的 host 白名单提交。两者的凭证、工作目录、Git remote、审计记录必须彻底分开。客户目标仓库禁止用 GitHub.com 或任何公网 SaaS Git 作为 remote——Skill 层在 `git push` 前校验 remote host 是否落在冻结白名单里，`--force` 和环境变量都绕不过去。客户侧的“承認”动作就是 review 并 merge 对应 PR，PR comments 自然构成レビュー記録。

## 外部系统接入优先级

优先级固定为官方 MCP Server > 社区 MCP（需额外安全审查）> 自建轻量 wrapper。测试平台用 Salesforce Hosted MCP 与 Playwright MCP；多云侧有 AWS `awslabs/mcp`、Azure MCP、GCP MCP preview、Cloudflare Workers MCP，阿里云只有社区版所以需自建。IaC 收敛到 Terraform 或 OpenTofu，由 HashiCorp 官方 MCP 生成并校验 HCL，云专属操作再叠加对应云的官方 MCP。文件存储取 S3 兼容协议作公约数，S3、OSS、R2、GCS、MinIO 均可覆盖，Azure Blob 需单独适配；代码里走 `fsspec` 或 `unstorage` 这类存储抽象接口，而不是直接锁定某家 SDK。
