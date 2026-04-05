---
title: "Hybrid Search: BM25 + Dense"
description: "Combine BM25 and dense retrieval signals to improve search quality across keyword and semantic queries."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["hybrid", "bm25", "dense", "fusion", "keyword"]
---

## Overview
Hybrid search combines BM25 (keyword search) with dense vector embeddings (semantic search) to leverage both exact term matching and semantic understanding. This dual approach improves retrieval quality across diverse query types—keyword queries get exact matches, while semantic queries capture conceptual relationships.

## Problem Statement
Pure semantic search or pure keyword search each have limitations:
- **Dense-only search**: Struggles with exact term matches, proper nouns, and domain-specific terminology
- **Keyword-only search**: Fails at understanding synonyms, paraphrasing, and conceptual relationships
- **Different query types**: Some queries are keyword-focused ("error code 404") while others are semantic ("how to fix authentication")

## Key Concepts
- **BM25**: Okapi BM25 algorithm for keyword search with TF-IDF weighting
- **Dense Search**: Vector-based semantic search using embeddings
- **Reciprocal Rank Fusion (RRF)**: Combines results from multiple ranking methods
- **Score Normalization**: Bringing different scoring systems to common scale
- **Alpha Parameter**: Controls the weighting between keyword and semantic components

## Implementation Guide

### Step 1: Set Up Dense Search
Implement vector-based semantic search with your chosen embedding model.

**Why**: Dense search captures semantic meaning but may miss exact term matches that are crucial for many queries.

### Step 2: Set Up BM25 Search
Implement keyword-based search using BM25.

**Why**: BM25 excels at exact term matching, domain-specific terminology, and proper noun searches where semantic models might struggle.

### Step 3: Implement Score Normalization
Normalize scores from different ranking methods to comparable scales.

**Why**: Different scoring systems (cosine similarity vs. BM25 scores) can't be directly combined—normalization creates a common scale.

### Step 4: Implement Result Fusion
Combine results from multiple search methods.

**Why**: RRF is robust to different scoring scales and doesn't require explicit score normalization, making it ideal for fusion.

### Step 5: Build the Hybrid Searcher
Combine all components into a single interface.

**Why**: A unified interface simplifies usage and allows easy experimentation with different fusion strategies and weights.

For implementation patterns, compare [OpenSearch hybrid search docs](https://docs.opensearch.org/docs/3.0/vector-search/ai-search/hybrid-search/index/), [OpenSearch hybrid search guide](https://docs.opensearch.org/2.17/search-plugins/hybrid-search/), the [reciprocal rank fusion paper](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf), and [Sentence Transformers retrieve & re-rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/).

## When to Use This Skill
- Building production RAG systems where both precision and recall matter
- Handling diverse query types (keyword + semantic)
- When exact term matching is important alongside conceptual understanding
- For technical documentation with specific terminology
- When user queries vary from natural language to specific terms

## When NOT to Use This Skill
- When pure semantic search already provides excellent results
- For very small datasets where complexity isn't justified
- When query latency must be minimized (hybrid adds overhead)
- When using a vector database that already implements hybrid search (e.g., Weaviate)

## Related Skills
- [Multi-Pass Retrieval with Reranking](./multi-pass-retrieval-with-reranking.md) - Further refine results
- [Semantic Chunking](../chunking/semantic-chunking.md) - Improve content quality
- [Optimize Retrieval Latency](../performance-optimization/optimize-retrieval-latency.md) - Performance tuning

## Metrics & Success Criteria
- **Retrieval Quality**: Improved NDCG/precision/recall vs. single-method search
- **Query Type Coverage**: Good results for both keyword and semantic queries
- **Latency**: Hybrid search within 1.5x of single-method latency
- **Maintainability**: Clear separation of components
- **Flexibility**: Easy to adjust alpha and fusion method
