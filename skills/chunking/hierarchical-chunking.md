---
title: "Hierarchical Chunking"
description: "Chunk nested documents into parent-child levels so retrieval can move from broad sections to fine-grained passages."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "chunking"
tags: ["nested", "multi-level", "document-structure", "parent-child"]
---

## Overview
Hierarchical chunking creates multi-level chunk structures that preserve document hierarchies (chapters, sections, subsections). This enables both broad-overview retrieval (high-level chunks) and detailed retrieval (low-level chunks) with parent-child relationships for context propagation.

## Problem Statement
Flat chunking strategies lose the structural relationships within documents:
- Questions about broad topics retrieve detailed fragments instead of summaries
- No way to retrieve "context for context" - when a detail is retrieved, its containing section is lost
- Navigation through document hierarchies becomes impossible
- Retrieval results can't be organized by document structure

## Key Concepts
- **Parent-Child Relationships**: Links between summary chunks and their detailed sub-chunks
- **Multi-Level Granularity**: Chunks at different abstraction levels (document → chapter → section → paragraph)
- **Context Propagation**: Ability to include parent context when retrieving child chunks
- **Metadata Enrichment**: Storing hierarchy information for filtering and navigation
- **Recursive Chunking**: Applying chunking rules recursively through document structure

## Implementation Guide

### Step 1: Parse Document Structure
Extract the hierarchical structure of your documents.

**Why**: Proper parsing is foundational—you can't create a hierarchy without understanding the structure.

### Step 2: Create Multi-Level Chunks
Generate chunks at multiple levels from the parsed hierarchy.

**Why**: Multiple chunk levels allow different retrieval strategies—summary chunks for broad questions, detailed chunks for specifics.

### Step 3: Store Hierarchy Metadata
Persist hierarchy information for retrieval-time context propagation.

**Why**: Metadata enables filtering and hierarchical queries (e.g., "retrieve from level 2 or deeper").

### Step 4: Implement Hierarchical Retrieval
Retrieve chunks with optional parent context.

**Why**: Hierarchical retrieval allows users to "zoom in" from broad topics to specific details, just like browsing a table of contents.

For implementation details, see the [LlamaIndex hierarchical node parser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/), [LangChain RecursiveCharacterTextSplitter](https://reference.langchain.com/python/langchain-text-splitters/character/RecursiveCharacterTextSplitter), [Haystack PreProcessor for structured documents](https://docs.haystack.deepset.ai/reference/experimental-preprocessors-api), and [LlamaIndex Structured Hierarchical Retrieval](https://developers.llamaindex.ai/python/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/).

## When to Use This Skill
- Long-form documents with clear structure (books, technical documentation, research papers)
- When you need both summary and detailed retrieval
- For applications that support "drill-down" navigation
- When building document browsing/search interfaces
- For Q&A systems that benefit from hierarchical context

## When NOT to Use This Skill
- Flat content without structure (blog posts, single-page articles)
- When storage complexity outweighs retrieval benefits
- For small document collections where simple chunking suffices
- When retrieval latency is critical (hierarchical retrieval adds overhead)

## Related Skills
- [Semantic Chunking](./semantic-chunking.md) - For content-aware chunking
- [Sliding Window Chunking](./sliding-window-chunking.md) - For context overlap
- [Multi-Pass Retrieval with Reranking](../retrieval-strategies/multi-pass-retrieval-with-reranking.md) - For refining hierarchical results

## Metrics & Success Criteria
- **Coverage**: All document content preserved across hierarchy levels
- **Retrieval Flexibility**: Can retrieve at any abstraction level
- **Context Relevance**: Parent context improves answer quality for detailed questions
- **Storage Efficiency**: Metadata overhead doesn't exceed 30% of storage
- **Query Latency**: Hierarchical retrieval within 2x of flat retrieval
