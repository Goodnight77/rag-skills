---
title: "Choosing a Chunking Framework"
description: "Select the right chunking framework based on document type, pipeline architecture, and retrieval goals."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "chunking"
tags: ["framework-selection", "chonkie", "langchain", "llamaindex", "haystack", "unstructured"]
---

## Overview
Chunking quality depends as much on the framework as on the strategy itself. This guide helps a coding agent choose between chunking frameworks based on the shape of the data, the surrounding RAG stack, and whether the main need is speed, structure-awareness, retrieval quality, or integration simplicity.

## Problem Statement
Teams often pick a chunking framework for the wrong reason:
- They default to the framework already in the app, even when it has weaker chunking primitives for the data type
- They choose a sophisticated semantic chunker for documents that only need simple deterministic splitting
- They use generic text splitters for PDFs, tables, or code repositories where structure matters more than raw length
- They optimize for chunking features without considering metadata propagation, ingestion workflow, or downstream retrieval

## Key Concepts
- **Framework Fit**: How well the chunking library matches the rest of the ingestion and retrieval stack
- **Structure Awareness**: Whether the framework understands sections, headings, tables, pages, or code blocks
- **Semantic Awareness**: Whether the framework can chunk by meaning rather than only size or delimiters
- **Operational Simplicity**: How easy it is to adopt the framework without introducing a second ingestion system
- **Chunking Depth**: Whether you need only fixed-size chunks or richer patterns like hierarchical, sentence-window, or code-aware chunking

## Implementation Guide

### Step 1: Identify the Dominant Document Type
Decide whether the corpus is mostly plain text, structured documents, code, or messy extracted files.

**Why**: Chunking frameworks differ most sharply in how they handle document structure. The right choice for markdown docs is often wrong for scanned PDFs or source code.

Use this default mapping:
- Plain text and generic prose: favor LangChain or Chonkie
- Metadata-rich RAG pipelines: favor LlamaIndex
- Pipeline-centric search applications: favor Haystack
- Parsed PDFs, office files, and layout-heavy documents: favor Unstructured
- Code-heavy repositories: favor Chonkie first, then LangChain if you need simpler integration

### Step 2: Check Whether Chunking Is a Core Requirement or Just a Utility
Determine whether chunking itself is a strategic part of the system or just one preprocessing step.

**Why**: If chunking is central to recall quality, code structure, or high-throughput ingestion, you want a framework with deeper chunking specialization. If it is incidental, use the framework already governing the RAG pipeline.

Choose this way:
- If chunking sophistication is a competitive advantage, start with Chonkie
- If chunking is just one component in a broader orchestration framework, prefer LangChain, LlamaIndex, or Haystack based on the app stack

### Step 3: Match the Framework to the Retrieval Pattern
Choose a framework whose chunking model supports the retrieval pattern you intend to use.

**Why**: Some frameworks are built around plain chunks, while others are better for hierarchical retrieval, metadata-enriched nodes, or section-preserving document flows.

Recommended fit by retrieval pattern:
- Simple vector search over text: LangChain or Chonkie
- Hierarchical retrieval and parent-child context: LlamaIndex or Haystack
- Section-aware retrieval for reports and long docs: Unstructured or Chonkie recursive chunking
- Code search and AST-aware chunking: Chonkie
- Fine-grained sentence-level retrieval with context reconstruction: LlamaIndex

### Step 4: Use the Framework Decision Matrix
Pick the framework whose strengths best match the workload.

**Why**: A framework should be chosen by tradeoff, not popularity.

| Framework | Best At | Choose It When | Avoid It When |
|----------|---------|----------------|---------------|
| **[Chonkie](https://docs.chonkie.ai/oss/chunkers/overview)** | Specialized chunking strategies, high throughput, semantic and code-aware chunking | Chunking is a first-class problem, you need semantic/code chunkers, or ingestion speed matters | You want the simplest possible default inside an existing LangChain or Haystack app |
| **[LangChain Text Splitters](https://docs.langchain.com/oss/python/integrations/splitters/index)** | Simple, reliable general-purpose chunking tightly integrated with LangChain apps | You already use LangChain or LangGraph and need practical default chunking with minimal extra tooling | You need deeply specialized code, layout, or semantic chunking beyond standard splitter patterns |
| **[LlamaIndex Node Parsers](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/)** | Metadata-rich nodes, sentence windows, hierarchical parsing, retrieval-aware chunking | You use LlamaIndex ingestion/query pipelines or need chunking that preserves node relationships and retrieval metadata | You only need straightforward standalone chunking without adopting LlamaIndex concepts |
| **[Haystack Preprocessors](https://docs.haystack.deepset.ai/docs/documentsplitter)** | Deterministic pipeline-based splitting for production search systems | You are building around Haystack pipelines and want predictable document preprocessing components | You need more advanced semantic or code-aware chunking than Haystack’s built-in preprocessors provide |
| **[Unstructured Chunking](https://docs.unstructured.io/open-source/core-functionality/chunking)** | Partition-first chunking for PDFs, Office docs, HTML, tables, and layout-heavy content | Your main challenge is document parsing and structural preservation before chunking | Your corpus is already clean text and you do not need layout-aware parsing |

### Step 5: Apply Framework-Specific Guidance
Use the framework only in the situations where it has a clear advantage.

**Why**: Each framework has a distinct operating model. Mixing them without a reason usually adds complexity.

#### Chonkie
Use [Chonkie](https://www.chonkie.ai/) when chunking itself is the focus of the system.

Strong fit:
- You need a dedicated chunking library rather than a general LLM framework
- You want to choose among token, sentence, recursive, semantic, late, fast, or code chunkers
- You have code repositories or technical docs where chunk coherence matters
- You have high-throughput ingestion where fast chunking is important

Especially relevant docs:
- [Chunkers overview](https://docs.chonkie.ai/oss/chunkers/overview)
- [RecursiveChunker](https://docs.chonkie.ai/oss/chunkers/recursive-chunker)
- [SemanticChunker](https://docs.chonkie.ai/oss/chunkers/semantic-chunker)
- [CodeChunker](https://docs.chonkie.ai/oss/chunkers/code-chunker)
- [FastChunker](https://docs.chonkie.ai/oss/chunkers/fast-chunker)

Do not choose Chonkie just because it has more chunkers. Choose it when those chunkers materially improve your corpus handling.

#### LangChain
Use [LangChain Text Splitters](https://docs.langchain.com/oss/python/integrations/splitters/index) when you want a practical default inside a LangChain or LangGraph application.

Strong fit:
- You already use LangChain loaders, embeddings, retrievers, or agents
- You want an opinionated default like `RecursiveCharacterTextSplitter`
- You need markdown, JSON, HTML, or code splitting without introducing another ingestion framework
- You value integration speed over chunking specialization

Especially relevant docs:
- [Text splitters overview](https://docs.langchain.com/oss/python/integrations/splitters/index)
- [RecursiveCharacterTextSplitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter)
- [CharacterTextSplitter](https://docs.langchain.com/oss/python/integrations/splitters/character_text_splitter)

Do not choose LangChain if you need the strongest code-aware or layout-aware chunking and are willing to use a more specialized tool.

#### LlamaIndex
Use [LlamaIndex Node Parsers](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/) when chunking is tightly coupled to retrieval behavior and metadata-rich nodes.

Strong fit:
- You want sentence-window retrieval, node relationships, or hierarchical retrieval patterns
- You care about chunk metadata because retrieval and postprocessing depend on it
- You are already using LlamaIndex ingestion pipelines, retrievers, and node postprocessors
- You want chunking that fits directly into a retrieval-aware framework

Especially relevant docs:
- [Node parser usage](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/)
- [HierarchicalNodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)
- [SentenceWindowNodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)

Do not choose LlamaIndex if you only need a lightweight chunker and do not want its document and node abstractions in the pipeline.

#### Haystack
Use [Haystack preprocessors](https://docs.haystack.deepset.ai/docs/documentsplitter) when the application is built as a search or RAG pipeline and you want deterministic preprocessing components.

Strong fit:
- You use Haystack pipelines end-to-end
- You need sentence, passage, page, line, or function splitting in a production-oriented indexing flow
- You want hierarchical document splitting without adopting a different ingestion framework
- You value stable preprocessing stages more than cutting-edge chunking algorithms

Especially relevant docs:
- [DocumentSplitter](https://docs.haystack.deepset.ai/docs/documentsplitter)
- [HierarchicalDocumentSplitter](https://docs.haystack.deepset.ai/docs/hierarchicaldocumentsplitter)
- [DocumentPreprocessor](https://docs.haystack.deepset.ai/docs/documentpreprocessor)

Do not choose Haystack for advanced semantic chunking if you are not otherwise using Haystack.

#### Unstructured
Use [Unstructured chunking](https://docs.unstructured.io/open-source/core-functionality/chunking) when the hard problem is not text splitting but extracting meaningful document elements first.

Strong fit:
- Your corpus includes PDFs, PowerPoints, HTML, tables, page layouts, and other messy enterprise documents
- You want chunking to follow structural elements created during partitioning
- You need section-preserving chunking such as `by_title`
- You care about table isolation, page boundaries, or composite document elements

Especially relevant docs:
- [Open-source chunking](https://docs.unstructured.io/open-source/core-functionality/chunking)
- [Platform API chunking strategies](https://docs.unstructured.io/platform-api/partition-api/chunking)

Do not choose Unstructured when the documents are already clean plain text and layout parsing adds no value.

## When to Use This Skill
- When deciding which chunking framework a coding agent should adopt for a new RAG pipeline
- When replacing ad hoc chunking logic with a framework-backed approach
- When the team needs a framework-level recommendation before tuning chunk size or overlap
- When the corpus mixes prose, code, and structured enterprise documents

## When NOT to Use This Skill
- When the framework is already fixed by platform constraints
- When the problem is chunk sizing rather than framework choice
- When you only need one simple deterministic splitter and framework selection is not material

## Related Skills
- [Semantic Chunking](./semantic-chunking.md) - Meaning-aware chunk boundaries
- [Hierarchical Chunking](./hierarchical-chunking.md) - Multi-level chunk structures
- [Sliding Window Chunking](./sliding-window-chunking.md) - Overlap-based chunking
- [RAG for Code Documentation](../data-type-handling/rag-for-code-documentation.md) - Code-heavy corpus guidance

## Metrics & Success Criteria
- **Framework Fit**: The chosen framework matches the dominant document and retrieval pattern
- **Operational Simplicity**: The framework does not introduce unnecessary ingestion complexity
- **Retrieval Quality**: Chunking improves recall and answer quality for the actual corpus
- **Maintainability**: The chunking approach is understandable and sustainable for the team
- **Migration Cost**: The framework choice does not create avoidable lock-in without clear upside
