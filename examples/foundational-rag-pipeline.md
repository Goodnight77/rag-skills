---
title: "Foundational RAG Pipeline Example"
category: "rag-agents"
tags: ["workflow", "quickstart", "pipeline"]
author: "rag-skills"
---

## Overview
This example shows the minimum viable shape of a RAG pipeline without turning the repository into an implementation repo. Use it as a reference workflow for agents and developers who need to understand the sequence of stages, the key decisions, and where to look for production-ready code.

## Goal
Build a simple question-answering workflow that:
1. Loads source documents
2. Chunks and embeds them
3. Stores them in a vector database
4. Retrieves relevant context at query time
5. Generates an answer grounded in retrieved passages

## Recommended Workflow

### Stage 1: Ingestion
- Load source documents from files, docs platforms, or APIs
- Normalize text and preserve useful metadata such as title, URL, section, and timestamp
- Apply a chunking strategy that matches the corpus

### Stage 2: Indexing
- Generate embeddings for each chunk
- Store vectors, chunk text, and metadata in a vector database
- Validate that filtering and retrieval work before moving on

### Stage 3: Retrieval
- Embed the user query
- Retrieve the top candidate chunks
- Optionally rerank or filter results before generation

### Stage 4: Answer Generation
- Pass the query and retrieved context to the model
- Require grounded answers and source attribution
- Return both answer text and the supporting chunks

## Reference Architecture

```text
Documents -> Loader -> Chunker -> Embedder -> Vector DB
User Query -> Query Embedder -> Retriever -> Prompt Builder -> LLM -> Answer + Sources
```

## Pseudocode

```text
load documents
chunk documents with metadata preserved
embed chunks
store chunks + embeddings in vector database

for each user query:
  embed query
  retrieve top-k chunks
  optionally rerank
  generate answer from retrieved context
  return answer with sources
```

## Design Choices

### Keep It Simple First
- Start with one loader, one chunking strategy, one embedding model, and one vector store
- Avoid hybrid retrieval and agent orchestration until the baseline is working

### Preserve Metadata Early
- Store source, section, and document identifiers during ingestion
- This enables filtering, citations, debugging, and later migration

### Measure Before Optimizing
- Check whether the retrieved chunks are actually relevant before tuning prompts
- Most early RAG failures are indexing or chunking problems, not generation problems

## Common Failure Modes
- Chunk size is too large, so retrieval returns noisy context
- Chunk size is too small, so meaning gets fragmented
- Metadata is missing, so debugging and citations are weak
- Retrieval is evaluated only by final answer quality instead of retrieval quality
- The pipeline uses synthetic examples that are too easy and hide failure cases

## When to Use This Example
- As the first pipeline shape for a new RAG application
- As the baseline architecture before adding reranking or agents
- As a teaching document for junior contributors or coding agents

## When NOT to Use This Example
- When the system already requires hybrid retrieval or multimodal ingestion
- When the main problem is orchestration across multiple tools or agents
- When the corpus depends heavily on layout parsing, code structure, or hierarchical retrieval

## External Implementations
- [LangChain RAG guide](https://docs.langchain.com/oss/python/langchain/rag)
- [LlamaIndex Introduction to RAG](https://docs.llamaindex.ai/en/stable/understanding/rag/)
- [Qdrant quickstart](https://qdrant.tech/documentation/quickstart/)
- [OpenAI cookbook RAG examples](https://github.com/openai/openai-cookbook/tree/main/examples)

## Related Skills
- [Semantic Chunking](../skills/chunking/semantic-chunking/SKILL.md)
- [Qdrant Setup for RAG](../skills/vector-databases/qdrant-setup-rag/SKILL.md)
- [Hybrid Search BM25 Dense](../skills/retrieval-strategies/hybrid-search-bm25-dense/SKILL.md)
