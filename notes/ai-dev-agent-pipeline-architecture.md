---
version: 1
id: ai-dev-agent-pipeline-architecture
title: AI 开发 Agent Pipeline — 架构总览
tags:
  - Agent
  - 架构
  - AI应用
  - Pipeline
  - Rust
source: ai-dev-agent-pipeline 项目设计文档与 Phase 1 实现（crates/pi-pipeline）
summary: CLI 形态、可断点续跑、可审计的多智能体开发流水线的定位、技术基座与模块边界，细节分散在九张卡片里。
created: 2026-09-12T02:45:51.000Z
updated: 2026-09-23T11:00:00.000Z
favorite: false
related:
  - ai-dev-core-principles
  - ai-dev-stage-graph
  - ai-dev-skill-quality-gate
  - ai-dev-agent-persona-routing
  - ai-dev-document-index
  - ai-dev-confidentiality-layer
  - ai-dev-brownfield-adapter
  - ai-dev-runtime-state-machine
  - ai-dev-cli-contract
---

# AI 开发 Agent Pipeline — 架构总览

> CLI 形态、可断点续跑、可审计的多智能体开发流水线的定位、技术基座与模块边界，细节分散在九张卡片里。

## 定位与目标

这是一套把需求分析、架构设计、技术选型、Infra、前端、后端、单元测试、E2E 测试串成阶段图的开发流水线，每个阶段由 AI Agent 生成产物，阶段之间挂质量门与人工承認门。四条硬目标：产出质量经得起审计、不低于人工水平；凡确定性代码能解决的绝不调模型以压成本；满足保密要求并留下完整的过程文档与レビュー痕迹；能对接 Salesforce、多云这类企业外部系统。支持 Greenfield 从零开发与 Brownfield 在客户既有代码库上迭代两种模式。MVP 明确不做的事同样重要：全量语言框架适配、多人共享的远程状态、云上生产自动部署、用 AI 顶替真人审批或绕过质量门、Web 管理后台。

## 技术基座与 ADR-001

编排核心用 Rust 原生实现（workspace + rusqlite + serde + clap），ADR-001 明确弃用 LangGraph、CrewAI、AutoGen。理由是编译型 CLI 依赖少、跨平台分发方便、退出码稳定、边界控制严格；状态机本身由声明式配置驱动，运行时校验器从同一份数据源读取，再引入第二套图编排框架只会多一个真相源。LLM、MCP、Project Adapter 一律作为阶段插件接入，不侵入 Core 状态机。执行形态是 CLI，无常驻服务，状态持久化在项目目录的 `.pipeline/state.db` 加产物文件。后续文档与实现都不得再以 LangGraph 为前提书写。

## 模块边界

划成十二个模块：CLI Adapter（解析、校验、打印、退出码）、Pipeline Orchestrator（按状态图调度）、Stage Agent（读输入、调人格生成产物）、Skill Runner（跑确定性检查产出 GateResult）、State Store（SQLite 事务、checkpoint、锁）、Artifact Store（原子写与 manifest）、Confidentiality Layer（脱敏与出站判定）、LLM Gateway（模型路由、超时、调用摘要）、Review Manager（承認项、レビュー記録、冻结）、Project Adapter 与 Integration Adapter（Git、MCP、云白名单连接）。模块之间只通过结构化契约通信，所有状态变更统一由 Orchestrator 提交事务。

## 卡片导航

- [五条核心原则](note://ai-dev-core-principles)：状态真相源、确定性下沉、人工承認、事务归口与停机纪律。
- [流水线阶段图与 Stage/Gate 契约](note://ai-dev-stage-graph)：阶段链路、stage_id 与质量门映射、接口字段、重试预算。
- [Skill 层与质量门契约](note://ai-dev-skill-quality-gate)：两类 Skill、检查器统一输出字段、安全项不得降级、测试夹具要求。
- [Agent 人格分工与模型路由](note://ai-dev-agent-persona-routing)：四种人格的关注点与对应校验工具，按任务类型选模型。
- [Document Index 体系](note://ai-dev-document-index)：Index 冻结为文档模板契约，四段式文档与承認落库。
- [保密与脱敏层](note://ai-dev-confidentiality-layer)：检测矩阵、可逆令牌化、敏感度分级、外部送信ログ与执行期权限默认值。
- [Brownfield 三层适配](note://ai-dev-brownfield-adapter)：Core/Project/Tool 分层、事实边界与 unknowns、仓库角色隔离、MCP 接入优先级。
- [运行核心](note://ai-dev-runtime-state-machine)：状态链、SQLite 表与设计落差、事务事件日志、checkpoint 与产物原子提交。
- [CLI 契约与 Crate 结构](note://ai-dev-cli-contract)：子命令实现范围、八个固定退出码、模块划分与 trait 插件点。
