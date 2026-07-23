---
version: 1
id: rag-concepts
title: RAG：概念总览
tags:
  - RAG
  - 概念
  - 知识库
  - AI应用
  - Agent
source: https://mp.weixin.qq.com/s/revpUlIxGWwMWT7289sFpQ
summary: RAG 核心概念索引：从 RAG、LLM、Embedding 到检索、生成、Grounding、幻觉和评估。
created: 2026-07-23T05:22:42.184Z
updated: 2026-07-23T12:44:23.317Z
favorite: false
related:
  - rag
  - rag-concept-rag
  - rag-concept-llm
  - rag-concept-embedding
  - rag-concept-vector-database
  - rag-concept-chunking
  - rag-concept-retriever
  - rag-concept-reranker
  - rag-concept-prompt
  - rag-concept-grounding
  - rag-concept-hallucination
  - rag-concept-evaluation
---

# RAG：概念总览

本节点解释 RAG 运行链路中的核心名词。每个概念继续拆成“工作机制、工程实现、常见问题/评估”三个细节分支。

## [RAG（检索增强生成）](note://rag-concept-rag)
- [RAG 系统架构](note://rag-rag-architecture)：从数据源、索引、检索、上下文编排到模型生成，RAG 是多个组件协作的系统。
- [RAG 端到端工作流](note://rag-rag-workflow)：理解问题、找证据、组织上下文、生成答案和评估反馈的完整闭环。
- [RAG 的边界与适用场景](note://rag-rag-limits)：RAG 适合知识查找和基于资料的问答，但不能替代所有数据库查询、计算和业务操作。

## [大语言模型（LLM）](note://rag-concept-llm)
- [LLM 上下文窗口](note://rag-llm-context-window)：模型一次请求能够接收的输入和输出 token 总量，决定可放入多少检索资料。
- [LLM 解码与生成参数](note://rag-llm-decoding)：temperature、top_p、最大输出长度等参数共同影响回答的稳定性和多样性。
- [指令层级与模型约束](note://rag-llm-instruction-hierarchy)：系统指令、用户问题和外部文档之间存在优先级，外部资料不能覆盖系统规则。

## [Embedding](note://rag-concept-embedding)
- [向量相似度与距离](note://rag-embedding-similarity)：余弦相似度、点积或欧氏距离用于衡量查询向量与文档向量的接近程度。
- [Embedding 模型选择](note://rag-embedding-model-selection)：语言覆盖、领域术语、维度、吞吐量和成本决定模型是否适合知识库。
- [向量版本与语义漂移](note://rag-embedding-version-drift)：Embedding 模型升级会改变向量空间，旧向量与新查询向量可能不再兼容。

## [向量数据库](note://rag-concept-vector-database)
- [近似近邻索引](note://rag-vector-ann-index)：HNSW、IVF 等索引通过牺牲少量精确度换取更快的向量近邻搜索。
- [元数据过滤与权限](note://rag-vector-metadata-filter)：在向量相似搜索前后按租户、用户权限、版本、时间和文档类型过滤候选。
- [索引更新一致性](note://rag-vector-update-consistency)：新增、修改和删除文档时，原文、向量、元数据和搜索缓存需要保持一致。

## [文档切分（Chunking）](note://rag-concept-chunking)
- [切分策略](note://rag-chunking-strategies)：固定长度、递归切分、按标题切分、语义切分和父子文档是常见策略。
- [片段重叠与上下文连续性](note://rag-chunking-overlap)：相邻片段保留少量重叠可以避免句子或论证被切断。
- [父子片段检索](note://rag-chunking-parent-child)：用小片段负责精准召回，再取其父章节或邻近片段补充完整上下文。

## [检索器（Retriever）](note://rag-concept-retriever)
- [关键词检索与向量检索](note://rag-retriever-lexical-vector)：BM25 等关键词检索擅长精确术语，向量检索擅长语义相近表达。
- [混合检索](note://rag-retriever-hybrid)：通过结果融合或加权组合关键词、向量和结构化过滤，兼顾精确匹配与语义匹配。
- [召回质量指标](note://rag-retriever-recall-metrics)：Recall@K、Precision@K、MRR 和命中排名用于衡量检索是否找到正确证据。

## [重排序器（Reranker）](note://rag-concept-reranker)
- [Cross-Encoder 重排序](note://rag-reranker-cross-encoder)：让模型同时读取查询和候选片段，直接判断二者的相关性。
- [Top-K、延迟与上下文预算](note://rag-reranker-topk-latency)：候选数量、重排数量和最终保留数量共同决定质量、延迟和模型上下文成本。
- [重排序评估](note://rag-reranker-evaluation)：比较重排前后的正确证据排名和最终答案质量，判断重排是否真的带来收益。

## [Prompt](note://rag-concept-prompt)
- [Prompt 模板结构](note://rag-prompt-template)：把角色规则、用户问题、检索证据、引用要求和输出格式分成清晰区块。
- [上下文组装](note://rag-prompt-context-assembly)：按照相关性、来源可信度、时间和互补性排列片段，并控制总 token 预算。
- [Prompt 注入防护](note://rag-prompt-injection-defense)：把外部文档当作数据而不是指令，限制工具调用和敏感信息输出。

## [Grounding](note://rag-concept-grounding)
- [引用与来源定位](note://rag-grounding-citation)：把答案中的关键结论连接到文档、章节、URL 或片段位置。
- [答案忠实度](note://rag-grounding-faithfulness)：判断答案是否被检索证据支持，区分资料事实、模型推断和未知信息。
- [证据冲突处理](note://rag-grounding-conflict)：当多个来源对同一事实不一致时，按版本、时间、权威等级和适用范围进行判断。

## [幻觉（Hallucination）](note://rag-concept-hallucination)
- [幻觉类型](note://rag-hallucination-types)：包括无依据编造、引用错配、数字错误、实体混淆和把推断说成事实。
- [幻觉成因](note://rag-hallucination-causes)：常见根因有知识缺失、召回错误、证据冲突、上下文过载和模型过度推断。
- [幻觉缓解](note://rag-hallucination-mitigation)：通过更好的知识更新、混合检索、证据约束、引用检查、拒答策略和回归评估降低风险。

## [RAG 评估](note://rag-concept-evaluation)
- [评估数据集](note://rag-evaluation-dataset)：由真实问题、参考证据、参考答案和难例组成的可重复测试集。
- [检索与生成指标](note://rag-evaluation-metrics)：检索关注 Recall@K、Precision、MRR；生成关注相关性、完整性、Faithfulness 和引用正确性。
- [线上监控与反馈闭环](note://rag-evaluation-online-monitoring)：记录查询、召回片段、答案、引用、延迟、成本、用户反馈和失败类型。

## 阅读路径
先理解 RAG 总体架构，再沿每个模块进入机制、实现和风险节点；最后通过评估节点把知识转成可回归的工程指标。

## 幻觉深入研究
- [幻觉深入研究](note://rag-hallucination-deep-research)：从事实正确性、证据忠实度、诊断、评估和缓解架构深入研究幻觉。