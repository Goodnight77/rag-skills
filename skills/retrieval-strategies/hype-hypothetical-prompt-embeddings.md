---
title: "HyPE - Hypothetical Prompt Embeddings"
description: "Precompute hypothetical questions during indexing to eliminate runtime query expansion overhead."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["hype", "precomputed-queries", "indexing-time", "query-alignment"]
---

## Overview
HyPE (Hypothetical Prompt Embeddings) transforms retrieval from query-document matching to question-question matching by generating multiple hypothetical questions for each document chunk during the indexing phase. This eliminates runtime LLM calls while significantly improving retrieval precision.

## Problem Statement
Hybrid and enhanced retrieval techniques often require runtime query expansion:
- **Latency Overhead**: LLM-based query expansion adds significant per-query latency
- **Cost Accumulation**: Each query requires additional LLM calls
- **Style Mismatch**: Direct query-document matching suffers from linguistic differences
- **Variable Quality**: Runtime generation produces inconsistent results

## Key Concepts
- **Precomputed Questions**: Hypothetical questions generated once during document indexing
- **Question-Question Matching**: Retrieval transforms to matching similar question patterns
- **Multi-Vector Representation**: Each chunk indexed multiple times with different questions
- **Index-Time Processing**: All LLM work done offline, no runtime overhead
- **Coverage Expansion**: Multiple questions per chunk increase semantic coverage

## Implementation Guide

### Step 1: Generate Hypothetical Questions per Chunk
For each document chunk, generate 3-5 hypothetical questions that would retrieve it.

**Why**: Multiple questions per chunk create diverse entry points for retrieval, increasing the likelihood of matching various user query formulations.

Direct an LLM to create questions that, when answered, capture the main points of each chunk.

### Step 2: Embed Hypothetical Questions
Generate embeddings for all hypothetical questions and store them with their source chunks.

**Why**: Question embeddings align with user query embeddings better than raw document embeddings, while maintaining a link to original content for answer generation.

Embed each question using your preferred embedding model and maintain a mapping to the source chunk.

### Step 3: Build Multi-Vector Index Structure
Create an index structure that maps question embeddings to their source chunks.

**Why**: The index needs to efficiently retrieve the original chunk content after finding matching question embeddings. This requires maintaining proper mapping metadata.

Build a vector index where each question embedding points to its corresponding source chunk.

### Step 4: Implement Efficient Retrieval
Query the index directly without runtime question generation.

**Why**: Since questions are precomputed, retrieval is as fast as standard vector search—no LLM latency or cost at query time.

Perform standard vector similarity search using the user's query against the precomputed question embeddings.

### Step 5: Optimize Index Construction
Use parallel processing and batching for efficient index building.

**Why**: Index construction is one-time but can be time-consuming. Efficient processing reduces deployment time and resource usage.

Process multiple chunks in parallel and batch embedding calls when possible.

### Step 6: Build Complete HyPE Pipeline
Combine all components into a cohesive system.

**Why**: A complete pipeline with configurable parameters allows for optimization and experimentation with different window strategies.

For implementation patterns, see the [HyPE paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5139335), [FAISS documentation](https://github.com/facebookresearch/faiss/wiki), and vector database documentation for multi-vector indexing.

## When to Use This Skill
- Building production RAG systems where runtime latency is critical
- When query-document style mismatch is a known issue
- For large document collections where index construction time is acceptable
- When you can afford one-time LLM costs but not per-query costs
- When maximizing retrieval precision is more important than index size

## When NOT to Use This Skill
- For frequently changing document sets (index rebuilding is expensive)
- When storage or memory constraints are tight (multi-vector representation increases index size)
- For very small collections where direct search works adequately
- When query latency is not a critical concern (HyDE may be simpler)
- For real-time ingestion scenarios where documents arrive continuously

## Related Skills
- [HyDE](./hyde-hypothetical-document-embeddings.md) - Runtime alternative
- [Semantic Chunking](../chunking/semantic-chunking.md) - Better input quality
- [Fusion Retrieval](./hybrid-search-bm25-dense.md) - Combining retrieval methods

## Metrics & Success Criteria
- **Retrieval Precision**: Up to 42 percentage points improvement
- **Query Latency**: Zero additional latency vs. baseline vector search
- **Claim Recall**: Up to 45 percentage points improvement
- **Index Size**: Acceptable increase (typically 3-5x due to multiple questions per chunk)
- **Index Construction Time**: Efficient processing with parallelization