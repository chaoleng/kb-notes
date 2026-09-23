# kb-notes

个人知识库：Markdown 笔记 + YAML frontmatter + `note://` 双向链接。全部笔记在 `notes/`，一篇一个概念，文件名即 `id`。

RAG 部分有两个视角，互不复制同一事实：[流程主干](notes/rag.md) 按「问题理解 → 知识库构建 → 检索 → 生成 → 评估」五个阶段组织，[概念总览](notes/rag-concepts.md) 按概念组织并向下展开细节。阶段笔记讲位置、输入输出和失败信号，概念笔记讲定义、参数和取舍。

## 笔记规范

每篇笔记以 frontmatter 开头，字段固定 10 个、顺序固定：

```yaml
---
version: 1                     # 整数
id: rag-vector-ann-index       # kebab-case，且必须等于文件名（不含 .md）
title: 向量数据库：近似近邻索引  # 非空
tags:                          # 至少 1 个，不可重复
  - RAG
source: https://example.com/…  # 非空，来源链接或出处描述
summary: 一句话摘要。            # 非空，用于索引
created: 2026-07-23T05:22:14.272Z   # ISO-8601 毫秒 UTC
updated: 2026-07-23T11:56:38.331Z   # 不得早于 created
favorite: false                # true / false
related:                       # 关联笔记 id，必须存在、不可自引用、必须双向
  - rag-retrieval
---
```

正文用 `[标题](note://<id>)` 引用其他笔记，目标必须存在。`related` 是双向的：A 写了 B，B 也要写 A；正文链接不受此约束（主干笔记可以单向指向孙节点）。

正文另有两条硬约束，用来防止模板灌水复发：

- **实质内容 ≥ 150 字**：统计时排除标题行、`>` 摘要引用行和纯导航链接行。只写一句话再拿导航凑篇幅的笔记会被拦下。
- **同一句话最多出现在 2 篇笔记里**：跨 3 篇及以上的逐字重复句会被判定为样板句。导航请用 `related` 和本页索引，不要在每篇末尾复制同一段「学习提示」。

修改已有笔记时把 `updated` 改成当次时间；`created` 永远保持首次建立的时间。

`source` 写真实出处：有公开原始资料的写论文或官方文档名称（如 `Self-RAG (Asai et al., 2023)`、`Lost in the Middle (Liu et al., 2023)`、`Microsoft GraphRAG 官方文档`），来自自己踩坑总结的写 `工程实践总结`。**不要编造 URL、论文标题或作者**；一篇笔记在原始资料之外补了大量工程内容时，`source` 要同时体现两者。

## 工具

```bash
python3 tools/kb.py check   # 校验规范、断链、双向性、索引新鲜度；CI 用，出错退出码 1
python3 tools/kb.py index   # 重新生成下面的索引区块
```

仅依赖 Python 3 标准库。新增或修改笔记后跑一次 `index`，再跑 `check`。

<!-- BEGIN INDEX: 由 tools/kb.py 生成，勿手改 -->

共 90 篇笔记。

## 知识树

### 一图看懂RAG运行全流程

- [一图看懂RAG运行全流程](notes/rag.md) — RAG 是理解问题、构建知识、检索证据、增强生成和持续评估优化组成的完整链路。本笔记是 RAG 知识树根节点。
  - [RAG：概念总览](notes/rag-concepts.md) — RAG 核心概念索引：从 RAG、LLM、Embedding 到检索、生成、Grounding、幻觉和评估。
    - [概念：文档切分（Chunking）](notes/rag-concept-chunking.md) — 把长文档划分成适合检索和上下文拼接的知识片段。
      - [文档切分（Chunking）：片段重叠与上下文连续性](notes/rag-chunking-overlap.md) — 相邻片段保留少量重叠可以避免句子或论证被切断。
      - [文档切分（Chunking）：父子片段检索](notes/rag-chunking-parent-child.md) — 用小片段负责精准召回，再取其父章节或邻近片段补充完整上下文。
      - [文档切分（Chunking）：切分策略](notes/rag-chunking-strategies.md) — 固定长度、递归切分、按标题切分、语义切分和父子文档是常见策略。
    - [概念：Embedding（向量表示）](notes/rag-concept-embedding.md) — 把文本或其他对象映射为数值向量，用于计算语义相似度和进行近邻检索。
      - [Embedding：微调与领域适配](notes/rag-embedding-finetune.md) — 通用模型在领域术语上召回见顶时，用三元组数据微调并全量重算向量。
      - [Embedding：Embedding 模型选择](notes/rag-embedding-model-selection.md) — 语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。
      - [Embedding：向量相似度与距离](notes/rag-embedding-similarity.md) — 余弦相似度、点积或欧氏距离用于衡量查询向量与文档向量的接近程度。
      - [Embedding：向量版本与语义漂移](notes/rag-embedding-version-drift.md) — Embedding 模型升级会改变向量空间，旧向量与新查询向量可能不再兼容。
    - [概念：RAG 评估](notes/rag-concept-evaluation.md) — 评估检索证据、答案质量、事实忠实度、延迟成本和知识新鲜度的体系。
      - [RAG 工程：成本与延迟预算](notes/rag-cost-latency-budget.md) — 把单次问答拆成可相加的成本项，先定住 p95 与单价上限再反推候选数与模型档位。
      - [RAG 评估：评估数据集](notes/rag-evaluation-dataset.md) — 由真实问题、参考证据、参考答案和难例组成的可重复测试集。
      - [RAG 评估：检索与生成指标](notes/rag-evaluation-metrics.md) — 检索关注 Recall@K、Precision、MRR；生成关注相关性、完整性、Faithfulness 和引用正确性。
      - [RAG 评估：线上监控与反馈闭环](notes/rag-evaluation-online-monitoring.md) — 记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。
    - [概念：Grounding（事实依据）](notes/rag-concept-grounding.md) — 让模型输出的关键结论能够被检索证据支持并回溯到原始来源。
      - [Grounding：引用与来源定位](notes/rag-grounding-citation.md) — 把答案中的关键结论连接到文档、章节、URL 或片段位置。
      - [Grounding：证据冲突处理](notes/rag-grounding-conflict.md) — 当多个来源对同一事实不一致时，按版本、时间、权威等级和适用范围进行判断。
      - [Grounding：答案忠实度](notes/rag-grounding-faithfulness.md) — 判断答案是否被检索证据支持，区分资料事实、模型推断和未知信息。
    - [概念：幻觉（Hallucination）](notes/rag-concept-hallucination.md) — 模型生成看似合理但缺乏事实依据或与证据冲突的内容。
      - [幻觉（Hallucination）：幻觉成因](notes/rag-hallucination-causes.md) — 常见根因有知识缺失、召回错误、证据冲突、上下文过载和模型过度推断。
      - [幻觉：深入研究](notes/rag-hallucination-deep-research.md) — 从事实正确性、证据忠实度、形成链路、诊断方法、评估指标和缓解架构深入研究 LLM/RAG 幻觉。
        - [幻觉形成链路与诊断](notes/rag-hallucination-research-causal-chain.md) — 沿数据、训练、检索、上下文、生成和验证链路定位错误来源。
        - [幻觉检测与评估](notes/rag-hallucination-research-evaluation.md) — 使用原子事实、Faithfulness、FActScore、引用指标和拒答质量建立评估闭环。
        - [事实正确性与证据忠实度](notes/rag-hallucination-research-factuality.md) — 区分 Factuality 与 Faithfulness，避免把碰巧正确当成可靠回答。
        - [幻觉缓解架构](notes/rag-hallucination-research-mitigation.md) — 用知识治理、混合检索、证据门控、约束生成和生成后校验降低风险。
      - [幻觉（Hallucination）：幻觉缓解](notes/rag-hallucination-mitigation.md) — 通过更好的知识更新、混合检索、证据约束、引用检查、拒答策略和回归评估降低风险。
      - [幻觉（Hallucination）：幻觉类型](notes/rag-hallucination-types.md) — 包括无依据编造、引用错配、数字错误、实体混淆和把推断说成事实。
    - [概念：大语言模型（LLM）](notes/rag-concept-llm.md) — 根据上下文预测和生成文本的模型，负责理解问题、组织证据和生成自然语言答案。
      - [大语言模型（LLM）：LLM 上下文窗口](notes/rag-llm-context-window.md) — 模型一次请求能够接收的输入和输出 token 总量，决定可放入多少检索资料。
      - [大语言模型（LLM）：LLM 解码与生成参数](notes/rag-llm-decoding.md) — temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。
      - [大语言模型（LLM）：指令层级与模型约束](notes/rag-llm-instruction-hierarchy.md) — 系统指令、用户问题和外部文档之间存在优先级，外部资料不能覆盖系统规则。
      - [大语言模型（LLM）：长上下文模型与 RAG 的分工](notes/rag-long-context.md) — 窗口变大不等于可以取消检索，两者按成本、位置偏置和权限边界分工。
    - [概念：Prompt（提示词）](notes/rag-concept-prompt.md) — 用于约束模型角色、输入格式、证据使用方式和输出格式的指令模板。
      - [Prompt：上下文压缩与证据精简](notes/rag-context-compression.md) — 在不丢关键事实的前提下缩短证据长度，用抽取、摘要或按查询删句控制输入规模。
      - [Prompt：上下文组装](notes/rag-prompt-context-assembly.md) — 按照相关性、来源可信度、时间和互补性排列片段，并控制总 token 预算。
      - [Prompt：Prompt 注入防护](notes/rag-prompt-injection-defense.md) — 把外部文档当作数据而不是指令，限制工具调用和敏感信息输出。
      - [Prompt：Prompt 模板结构](notes/rag-prompt-template.md) — 把角色规则、用户问题、检索证据、引用要求和输出格式分成清晰区块。
    - [概念：RAG（检索增强生成）](notes/rag-concept-rag.md) — 通过外部知识检索增强大语言模型生成的系统方法，不等同于单纯的向量数据库。
      - [RAG（检索增强生成）：RAG 系统架构](notes/rag-rag-architecture.md) — 从数据源、索引、检索、上下文编排到模型生成，RAG 是多个组件协作的系统。
        - [RAG 工程：三层缓存策略](notes/rag-cache-strategy.md) — embedding、检索结果与生成结果三层缓存各有各的键构成和失效条件，键设计错了就是越权。
      - [RAG（检索增强生成）：RAG 的边界与适用场景](notes/rag-rag-limits.md) — RAG 适合知识查找和基于资料的问答，但不能替代所有数据库查询、计算和业务操作。
      - [RAG（检索增强生成）：RAG 端到端工作流](notes/rag-rag-workflow.md) — 理解问题、找证据、组织上下文、生成答案和评估反馈的完整闭环。
    - [概念：重排序器（Reranker）](notes/rag-concept-reranker.md) — 对初步召回的候选片段重新计算相关性并排序的组件。
      - [重排序器（Reranker）：Cross-Encoder 重排序](notes/rag-reranker-cross-encoder.md) — 让模型同时读取查询和候选片段，直接判断二者的相关性。
      - [重排序器（Reranker）：重排序评估](notes/rag-reranker-evaluation.md) — 比较重排前后的正确证据排名和最终答案质量，判断重排是否真的带来收益。
      - [重排序器（Reranker）：Top-K、延迟与上下文预算](notes/rag-reranker-topk-latency.md) — 候选数量、重排数量和最终保留数量共同决定质量、延迟和模型上下文成本。
    - [概念：检索器（Retriever）](notes/rag-concept-retriever.md) — 根据用户查询从知识库中召回候选片段的组件。
      - [RAG：自适应与迭代检索](notes/rag-adaptive-retrieval.md) — 把检不检、要不要再检一轮变成运行时决策，Self-RAG 靠反省 token，CRAG 靠轻量评估器。
      - [RAG：图检索与知识图谱](notes/rag-graph-retrieval.md) — GraphRAG 把语料抽成实体关系图并按社区分层摘要，专治跨文档汇总和多跳关系问题。
      - [检索器（Retriever）：混合检索](notes/rag-retriever-hybrid.md) — 通过结果融合或加权组合关键词、向量和结构化过滤，兼顾精确匹配与语义匹配。
      - [检索器（Retriever）：关键词检索与向量检索](notes/rag-retriever-lexical-vector.md) — BM25 等关键词检索擅长精确术语，向量检索擅长语义相近表达。
      - [检索器（Retriever）：召回质量指标](notes/rag-retriever-recall-metrics.md) — Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。
    - [概念：向量数据库](notes/rag-concept-vector-database.md) — 存储向量及其元数据并提供近似近邻搜索的数据库或索引系统。
      - [向量数据库：近似近邻索引](notes/rag-vector-ann-index.md) — HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。
      - [向量数据库：元数据过滤与权限](notes/rag-vector-metadata-filter.md) — 在向量相似搜索前后按租户、用户权限、版本、时间和文档类型过滤候选。
        - [RAG 工程：多租户隔离与分片](notes/rag-multi-tenant.md) — 共享集合加租户过滤还是每租户独立分片，取决于隔离强度、索引内存与长尾租户的管理成本。
      - [向量数据库：索引更新一致性](notes/rag-vector-update-consistency.md) — 新增、修改和删除文档时，原文、向量、元数据和搜索缓存需要保持一致。
  - [RAG：评估与持续优化](notes/rag-evaluation.md) — 从检索质量、答案准确性、引用完整性和系统成本延迟等维度持续改进 RAG。
    - [RAG：知识更新与线上迭代](notes/rag-ops-iteration.md) — 通过增量索引、版本管理、监控和失败样本回流，让知识库持续保持新鲜和可靠。
  - [RAG：增强生成](notes/rag-generation.md) — 把原始问题和检索证据组织成模型上下文，生成有依据、可解释的答案。
  - [RAG：知识库构建](notes/rag-knowledge-base.md) — 把原始文档加工成可检索知识的主干，包括采集、清洗、切分、向量化和索引。
    - [RAG：文档采集、清洗与切分](notes/rag-document-processing.md) — 将网页、PDF、Markdown、数据库记录等原始资料转换为边界清晰的知识片段。
      - [RAG：表格、OCR 与多模态入库](notes/rag-multimodal-ingestion.md) — 表格、扫描件、图表和代码需要各自的解析与切分规则才能进入索引。
    - [RAG：Embedding 与索引](notes/rag-embedding-index.md) — 把知识片段编码成向量并建立索引，让语义相近的问题能够找到相关内容。
  - [RAG：用户问题理解](notes/rag-question-understanding.md) — RAG 的入口：识别用户意图、补全查询和处理多轮上下文，决定后续检索方向。
    - [RAG：多轮对话上下文](notes/rag-conversation-context.md) — 从历史对话中解析指代、条件和用户偏好，形成当前检索所需的最小上下文。
    - [RAG：多路召回与查询扩展](notes/rag-query-expansion.md) — 同一意图并行生成多条查询分别召回再融合，HyDE 则先写假设答案再拿它去检索。
    - [RAG：查询改写与问题拆分](notes/rag-query-rewrite.md) — 把自然语言问题改造成更适合检索的一个或多个查询，同时保留原始意图。
    - [RAG：查询路由与意图分类](notes/rag-query-routing.md) — 先判断该不该检索，再判断该检索哪个子库，路由的两级决策决定了后续链路的上限。
  - [RAG：相关知识检索](notes/rag-retrieval.md) — 从知识库召回候选片段并排序，向生成模型提供少量高相关上下文。

### 流水线阶段图与 Stage/Gate 契约

- [流水线阶段图与 Stage/Gate 契约](notes/ai-dev-stage-graph.md) — 从需求输入到最终承認的阶段链路、每个阶段挂载的质量门，以及重试预算的硬边界。
  - [AI 开发 Agent Pipeline — 架构总览](notes/ai-dev-agent-pipeline-architecture.md) — CLI 形态、可断点续跑、可审计的多智能体开发流水线的定位、技术基座与模块边界，细节分散在九张卡片里。
    - [Agent 人格分工与模型路由](notes/ai-dev-agent-persona-routing.md) — 每个 LLM 节点绑定一个专家人格决定生成方向，达标与否交给对应的确定性校验工具。
    - [Brownfield 三层适配与仓库角色隔离](notes/ai-dev-brownfield-adapter.md) — Core 固定不变，项目与工具差异下沉到两层适配器，客户仓库与源码仓库的凭证和 remote 严格隔离。
    - [CLI 契约、退出码与 Crate 结构](notes/ai-dev-cli-contract.md) — 子命令与固定退出码构成对外契约，单 crate 的模块划分和 trait 抽象决定后续能替换什么。
    - [保密与脱敏层、安全默认值](notes/ai-dev-confidentiality-layer.md) — 出站内容先过本地脱敏与策略判定再发模型，返回后本地回填，执行期另有一套权限默认值。
    - [AI 开发 Agent Pipeline：五条核心原则](notes/ai-dev-core-principles.md) — 五条原则界定了状态真相源、LLM 与 Skill 的分工、人工承認的地位以及异常时的停机方式。
    - [Document Index 驱动的文档体系与人工承認](notes/ai-dev-document-index.md) — Index 经人工承認后冻结为文档模板契约，后续所有交付文档按它校验章节并留签字痕迹。
    - [运行核心：状态机、SQLite、事务与原子提交](notes/ai-dev-runtime-state-machine.md) — 状态图以声明式配置编译进二进制，所有变更在单个事务里落库并追加事件，产物先落文件再登记。
    - [Skill 层与质量门契约](notes/ai-dev-skill-quality-gate.md) — 确定性 Skill 负责判定成败，质量门按统一字段输出诊断，安全类检查不许降级。

### omp 编码 Agent Harness：上下文与记忆管理

- [omp 编码 Agent Harness：上下文与记忆管理](notes/omp-harness.md) — omp 这类编码 Agent harness 通过工具原语、内部与持久记忆分层、以及上下文节流三条机制管理有限的上下文窗口。
  - [omp Harness：上下文缓存与节流](notes/omp-harness-context-caching.md) — 只把必要片段读进上下文窗口，大产物截断外置为可寻址引用，通过委派进一步压缩，避免把整文件或整日志塞进对话。
  - [omp Harness：子 Agent 委派与并行编排](notes/omp-harness-delegation.md) — 用 task 派生背景子 Agent 时，指令必须自包含、批量派发才有真并行、文件所有权与接口契约必须提前拆清。
  - [omp Harness：文件读写](notes/omp-harness-file-io.md) — 用带快照指纹的专用读写检索原语操作文件，读靠选择器切片、写靠行锚定补丁与乐观锁，专用工具一律优先于 shell。
  - [omp Harness：记忆管理](notes/omp-harness-memory-management.md) — 把记忆分成短期上下文、可寻址持久记忆和不进真相源的内部记忆三层，明确什么进上下文、什么落持久、什么只作过程记忆。
  - [omp Harness：待办与阶段状态管理](notes/omp-harness-task-state.md) — 用 todo 把多步任务外化成可检查的阶段状态，靠真实任务文本、显式阻塞标记和与工具调用同轮的状态更新保持进度可信。
  - [omp Harness：专用工具优先的工具策略](notes/omp-harness-tool-policy.md) — 读写、检索、结构遍历、跨文件重命名都有专用原语，因其输出可寻址且编辑带乐观锁而优先于 shell 等价物。
  - [omp Harness：交付前的验证契约](notes/omp-harness-verification.md) — 交付前必须跑真实路径而非只跑测试文件，bug 要先复现后确认，子 Agent 的完成声明需要主 Agent 复验。

## 全部笔记

| id | 标题 | 标签 |
| --- | --- | --- |
| [ai-dev-agent-persona-routing](notes/ai-dev-agent-persona-routing.md) | Agent 人格分工与模型路由 | Agent / 架构 / Pipeline |
| [ai-dev-agent-pipeline-architecture](notes/ai-dev-agent-pipeline-architecture.md) | AI 开发 Agent Pipeline — 架构总览 | Agent / 架构 / AI应用 / Pipeline / Rust |
| [ai-dev-brownfield-adapter](notes/ai-dev-brownfield-adapter.md) | Brownfield 三层适配与仓库角色隔离 | 架构 / 安全 / Agent |
| [ai-dev-cli-contract](notes/ai-dev-cli-contract.md) | CLI 契约、退出码与 Crate 结构 | CLI / Rust / 架构 |
| [ai-dev-confidentiality-layer](notes/ai-dev-confidentiality-layer.md) | 保密与脱敏层、安全默认值 | 安全 / 架构 / Agent |
| [ai-dev-core-principles](notes/ai-dev-core-principles.md) | AI 开发 Agent Pipeline：五条核心原则 | Agent / 架构 / 质量门 |
| [ai-dev-document-index](notes/ai-dev-document-index.md) | Document Index 驱动的文档体系与人工承認 | Agent / Pipeline / 质量门 |
| [ai-dev-runtime-state-machine](notes/ai-dev-runtime-state-machine.md) | 运行核心：状态机、SQLite、事务与原子提交 | SQLite / Rust / 架构 |
| [ai-dev-skill-quality-gate](notes/ai-dev-skill-quality-gate.md) | Skill 层与质量门契约 | 质量门 / Agent / 安全 |
| [ai-dev-stage-graph](notes/ai-dev-stage-graph.md) | 流水线阶段图与 Stage/Gate 契约 | Pipeline / 架构 / 质量门 |
| [omp-harness](notes/omp-harness.md) | omp 编码 Agent Harness：上下文与记忆管理 | omp / harness / Agent |
| [omp-harness-context-caching](notes/omp-harness-context-caching.md) | omp Harness：上下文缓存与节流 | omp / harness / 上下文 |
| [omp-harness-delegation](notes/omp-harness-delegation.md) | omp Harness：子 Agent 委派与并行编排 | omp / harness / Agent |
| [omp-harness-file-io](notes/omp-harness-file-io.md) | omp Harness：文件读写 | omp / harness / 文件 |
| [omp-harness-memory-management](notes/omp-harness-memory-management.md) | omp Harness：记忆管理 | omp / harness / 记忆 |
| [omp-harness-task-state](notes/omp-harness-task-state.md) | omp Harness：待办与阶段状态管理 | omp / harness / 工程实践 |
| [omp-harness-tool-policy](notes/omp-harness-tool-policy.md) | omp Harness：专用工具优先的工具策略 | omp / harness / 工程实践 |
| [omp-harness-verification](notes/omp-harness-verification.md) | omp Harness：交付前的验证契约 | omp / harness / 工程实践 |
| [rag](notes/rag.md) | 一图看懂RAG运行全流程 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-adaptive-retrieval](notes/rag-adaptive-retrieval.md) | RAG：自适应与迭代检索 | RAG / 检索 / 自适应检索 / Self-RAG |
| [rag-cache-strategy](notes/rag-cache-strategy.md) | RAG 工程：三层缓存策略 | RAG / 工程实践 / 缓存 |
| [rag-chunking-overlap](notes/rag-chunking-overlap.md) | 文档切分（Chunking）：片段重叠与上下文连续性 | RAG / 概念 / 细节 |
| [rag-chunking-parent-child](notes/rag-chunking-parent-child.md) | 文档切分（Chunking）：父子片段检索 | RAG / 概念 / 细节 |
| [rag-chunking-strategies](notes/rag-chunking-strategies.md) | 文档切分（Chunking）：切分策略 | RAG / 概念 / 细节 |
| [rag-concept-chunking](notes/rag-concept-chunking.md) | 概念：文档切分（Chunking） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-embedding](notes/rag-concept-embedding.md) | 概念：Embedding（向量表示） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-evaluation](notes/rag-concept-evaluation.md) | 概念：RAG 评估 | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-grounding](notes/rag-concept-grounding.md) | 概念：Grounding（事实依据） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-hallucination](notes/rag-concept-hallucination.md) | 概念：幻觉（Hallucination） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-llm](notes/rag-concept-llm.md) | 概念：大语言模型（LLM） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-prompt](notes/rag-concept-prompt.md) | 概念：Prompt（提示词） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-rag](notes/rag-concept-rag.md) | 概念：RAG（检索增强生成） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-reranker](notes/rag-concept-reranker.md) | 概念：重排序器（Reranker） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-retriever](notes/rag-concept-retriever.md) | 概念：检索器（Retriever） | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concept-vector-database](notes/rag-concept-vector-database.md) | 概念：向量数据库 | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-concepts](notes/rag-concepts.md) | RAG：概念总览 | RAG / 概念 / 知识库 / AI应用 / Agent |
| [rag-context-compression](notes/rag-context-compression.md) | Prompt：上下文压缩与证据精简 | RAG / 概念 / 细节 |
| [rag-conversation-context](notes/rag-conversation-context.md) | RAG：多轮对话上下文 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-cost-latency-budget](notes/rag-cost-latency-budget.md) | RAG 工程：成本与延迟预算 | RAG / 工程实践 / 成本 |
| [rag-document-processing](notes/rag-document-processing.md) | RAG：文档采集、清洗与切分 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-embedding-finetune](notes/rag-embedding-finetune.md) | Embedding：微调与领域适配 | RAG / 概念 / 细节 |
| [rag-embedding-index](notes/rag-embedding-index.md) | RAG：Embedding 与索引 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-embedding-model-selection](notes/rag-embedding-model-selection.md) | Embedding：Embedding 模型选择 | RAG / 概念 / 细节 |
| [rag-embedding-similarity](notes/rag-embedding-similarity.md) | Embedding：向量相似度与距离 | RAG / 概念 / 细节 |
| [rag-embedding-version-drift](notes/rag-embedding-version-drift.md) | Embedding：向量版本与语义漂移 | RAG / 概念 / 细节 |
| [rag-evaluation](notes/rag-evaluation.md) | RAG：评估与持续优化 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-evaluation-dataset](notes/rag-evaluation-dataset.md) | RAG 评估：评估数据集 | RAG / 概念 / 细节 |
| [rag-evaluation-metrics](notes/rag-evaluation-metrics.md) | RAG 评估：检索与生成指标 | RAG / 概念 / 细节 |
| [rag-evaluation-online-monitoring](notes/rag-evaluation-online-monitoring.md) | RAG 评估：线上监控与反馈闭环 | RAG / 概念 / 细节 |
| [rag-generation](notes/rag-generation.md) | RAG：增强生成 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-graph-retrieval](notes/rag-graph-retrieval.md) | RAG：图检索与知识图谱 | RAG / 概念 / 细节 |
| [rag-grounding-citation](notes/rag-grounding-citation.md) | Grounding：引用与来源定位 | RAG / 概念 / 细节 |
| [rag-grounding-conflict](notes/rag-grounding-conflict.md) | Grounding：证据冲突处理 | RAG / 概念 / 细节 |
| [rag-grounding-faithfulness](notes/rag-grounding-faithfulness.md) | Grounding：答案忠实度 | RAG / 概念 / 细节 |
| [rag-hallucination-causes](notes/rag-hallucination-causes.md) | 幻觉（Hallucination）：幻觉成因 | RAG / 概念 / 细节 |
| [rag-hallucination-deep-research](notes/rag-hallucination-deep-research.md) | 幻觉：深入研究 | RAG / 概念 / 细节 / 深入研究 |
| [rag-hallucination-mitigation](notes/rag-hallucination-mitigation.md) | 幻觉（Hallucination）：幻觉缓解 | RAG / 概念 / 细节 |
| [rag-hallucination-research-causal-chain](notes/rag-hallucination-research-causal-chain.md) | 幻觉形成链路与诊断 | 幻觉 / 深入研究 / 诊断 |
| [rag-hallucination-research-evaluation](notes/rag-hallucination-research-evaluation.md) | 幻觉检测与评估 | 幻觉 / 深入研究 / 评估 |
| [rag-hallucination-research-factuality](notes/rag-hallucination-research-factuality.md) | 事实正确性与证据忠实度 | 幻觉 / 深入研究 / Factuality / Faithfulness |
| [rag-hallucination-research-mitigation](notes/rag-hallucination-research-mitigation.md) | 幻觉缓解架构 | 幻觉 / 深入研究 / 缓解 |
| [rag-hallucination-types](notes/rag-hallucination-types.md) | 幻觉（Hallucination）：幻觉类型 | RAG / 概念 / 细节 |
| [rag-knowledge-base](notes/rag-knowledge-base.md) | RAG：知识库构建 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-llm-context-window](notes/rag-llm-context-window.md) | 大语言模型（LLM）：LLM 上下文窗口 | RAG / 概念 / 细节 |
| [rag-llm-decoding](notes/rag-llm-decoding.md) | 大语言模型（LLM）：LLM 解码与生成参数 | RAG / 概念 / 细节 |
| [rag-llm-instruction-hierarchy](notes/rag-llm-instruction-hierarchy.md) | 大语言模型（LLM）：指令层级与模型约束 | RAG / 概念 / 细节 |
| [rag-long-context](notes/rag-long-context.md) | 大语言模型（LLM）：长上下文模型与 RAG 的分工 | RAG / 概念 / 细节 |
| [rag-multi-tenant](notes/rag-multi-tenant.md) | RAG 工程：多租户隔离与分片 | RAG / 工程实践 / 多租户 |
| [rag-multimodal-ingestion](notes/rag-multimodal-ingestion.md) | RAG：表格、OCR 与多模态入库 | RAG / 知识库 / 细节 |
| [rag-ops-iteration](notes/rag-ops-iteration.md) | RAG：知识更新与线上迭代 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-prompt-context-assembly](notes/rag-prompt-context-assembly.md) | Prompt：上下文组装 | RAG / 概念 / 细节 |
| [rag-prompt-injection-defense](notes/rag-prompt-injection-defense.md) | Prompt：Prompt 注入防护 | RAG / 概念 / 细节 |
| [rag-prompt-template](notes/rag-prompt-template.md) | Prompt：Prompt 模板结构 | RAG / 概念 / 细节 |
| [rag-query-expansion](notes/rag-query-expansion.md) | RAG：多路召回与查询扩展 | RAG / 检索 / 查询扩展 / HyDE |
| [rag-query-rewrite](notes/rag-query-rewrite.md) | RAG：查询改写与问题拆分 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-query-routing](notes/rag-query-routing.md) | RAG：查询路由与意图分类 | RAG / 检索 / 路由 / 工程实践 |
| [rag-question-understanding](notes/rag-question-understanding.md) | RAG：用户问题理解 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-rag-architecture](notes/rag-rag-architecture.md) | RAG（检索增强生成）：RAG 系统架构 | RAG / 概念 / 细节 |
| [rag-rag-limits](notes/rag-rag-limits.md) | RAG（检索增强生成）：RAG 的边界与适用场景 | RAG / 概念 / 细节 |
| [rag-rag-workflow](notes/rag-rag-workflow.md) | RAG（检索增强生成）：RAG 端到端工作流 | RAG / 概念 / 细节 |
| [rag-reranker-cross-encoder](notes/rag-reranker-cross-encoder.md) | 重排序器（Reranker）：Cross-Encoder 重排序 | RAG / 概念 / 细节 |
| [rag-reranker-evaluation](notes/rag-reranker-evaluation.md) | 重排序器（Reranker）：重排序评估 | RAG / 概念 / 细节 |
| [rag-reranker-topk-latency](notes/rag-reranker-topk-latency.md) | 重排序器（Reranker）：Top-K、延迟与上下文预算 | RAG / 概念 / 细节 |
| [rag-retrieval](notes/rag-retrieval.md) | RAG：相关知识检索 | RAG / 知识库 / AI应用 / Agent / 大模型 |
| [rag-retriever-hybrid](notes/rag-retriever-hybrid.md) | 检索器（Retriever）：混合检索 | RAG / 概念 / 细节 |
| [rag-retriever-lexical-vector](notes/rag-retriever-lexical-vector.md) | 检索器（Retriever）：关键词检索与向量检索 | RAG / 概念 / 细节 |
| [rag-retriever-recall-metrics](notes/rag-retriever-recall-metrics.md) | 检索器（Retriever）：召回质量指标 | RAG / 概念 / 细节 |
| [rag-vector-ann-index](notes/rag-vector-ann-index.md) | 向量数据库：近似近邻索引 | RAG / 概念 / 细节 |
| [rag-vector-metadata-filter](notes/rag-vector-metadata-filter.md) | 向量数据库：元数据过滤与权限 | RAG / 概念 / 细节 |
| [rag-vector-update-consistency](notes/rag-vector-update-consistency.md) | 向量数据库：索引更新一致性 | RAG / 概念 / 细节 |

<!-- END INDEX -->
