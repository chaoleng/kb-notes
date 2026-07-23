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
updated: 2026-07-23T05:22:42.184Z
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

# RAG 概念总览

本节点解释 RAG 运行链路中的核心名词。它与流程树相互补充：流程树回答“先做什么、后做什么”，概念树回答“每个组件是什么、解决什么问题”。

## 概念分支
- [概念：RAG（检索增强生成）](note://rag-concept-rag)：通过外部知识检索增强大语言模型生成的系统方法，不等同于单纯的向量数据库。
- [概念：大语言模型（LLM）](note://rag-concept-llm)：根据上下文预测和生成文本的模型，负责理解问题、组织证据和生成自然语言答案。
- [概念：Embedding（向量表示）](note://rag-concept-embedding)：把文本或其他对象映射为数值向量，用于计算语义相似度和进行近邻检索。
- [概念：向量数据库](note://rag-concept-vector-database)：存储向量及其元数据并提供近似近邻搜索的数据库或索引系统。
- [概念：文档切分（Chunking）](note://rag-concept-chunking)：把长文档划分成适合检索和上下文拼接的知识片段。
- [概念：检索器（Retriever）](note://rag-concept-retriever)：根据用户查询从知识库中召回候选片段的组件。
- [概念：重排序器（Reranker）](note://rag-concept-reranker)：对初步召回的候选片段重新计算相关性并排序的组件。
- [概念：Prompt（提示词）](note://rag-concept-prompt)：用于约束模型角色、输入格式、证据使用方式和输出格式的指令模板。
- [概念：Grounding（事实依据）](note://rag-concept-grounding)：让模型输出的关键结论能够被检索证据支持并回溯到原始来源。
- [概念：幻觉（Hallucination）](note://rag-concept-hallucination)：模型生成看似合理但缺乏事实依据或与证据冲突的内容。
- [概念：RAG 评估](note://rag-concept-evaluation)：评估检索证据、答案质量、事实忠实度、延迟成本和知识新鲜度的体系。

## 阅读路径
先理解 RAG，再理解 LLM、Embedding、Chunking 和向量数据库；然后学习 Retriever、Reranker、Prompt 和 Grounding；最后用幻觉与评估节点检查系统质量。