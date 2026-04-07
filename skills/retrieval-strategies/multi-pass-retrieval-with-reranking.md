---
title: "Multi-Pass Retrieval with Reranking"
description: "Use a two-stage retrieval pipeline with reranking to balance recall, precision, and latency."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["reranking", "cross-encoder", "two-stage", "relevance"]
---

## Overview
Multi-pass retrieval with reranking is a two-stage approach that first retrieves a broad set of candidates using fast bi-encoder search, then refines them using a more accurate but slower cross-encoder reranker. This balances recall and relevance while maintaining acceptable latency.

## Problem Statement
Single-stage retrieval has inherent trade-offs:
- **Bi-encoder only**: Fast but limited relevance—struggles with complex query-document relationships
- **Cross-encoder only**: Accurate but too slow for large document collections
- **Fixed top-k**: Can't adapt to query difficulty—some queries need more/ fewer candidates
- **Static retrieval**: Can't incorporate user feedback or context during retrieval

## Key Concepts
- **Bi-Encoder**: Fast encoding model that produces fixed vectors for documents and queries
- **Cross-Encoder**: Joint query-document encoder for accurate scoring (but slower)
- **Two-Stage Retrieval**: Broad retrieval followed by refinement
- **Adaptive Top-K**: Dynamically adjust retrieval depth based on query characteristics
- **Reranking Pipeline**: Post-retrieval scoring and reordering of candidates

## Implementation Guide

### Step 1: Set Up Bi-Encoder Retrieval
Implement the first-stage retrieval using your vector database.

**Why**: Bi-encoder retrieval is fast and scalable but produces approximate scores—suitable for the first pass to narrow candidates.

### Step 2: Set Up Cross-Encoder Reranking
Implement the second-stage reranking for accurate scoring.

**Why**: Cross-encoders produce more accurate relevance scores by jointly encoding query-document pairs, but are too slow for full-scale retrieval.

### Step 3: Implement Adaptive Retrieval
Dynamically adjust retrieval parameters based on query characteristics.

**Why**: Adaptive retrieval ensures complex queries get more candidates for reranking while simple queries remain fast.

### Step 4: Build the Multi-Pass Pipeline
Combine all components into a complete retrieval pipeline.

**Why**: A unified pipeline with timing and explanation makes it easy to optimize and debug the retrieval system.

### Step 5: Implement Cache and Optimization
Add caching and optimizations for production use.

**Why**: Caching reduces computation for repeated queries, which is common in production systems.

For working examples, see [Sentence Transformers CrossEncoder docs](https://www.sbert.net/docs/package_reference/cross_encoder/cross_encoder.html), [Sentence Transformers rerankers](https://www.sbert.net/examples/cross_encoder/training/rerankers/README.html), [Sentence Transformers retrieve & re-rank](https://www.sbert.net/examples/applications/retrieve_rerank/README.html), and the [MonoT5 paper](https://arxiv.org/abs/2207.14235).

## When to Use This Skill
- Production RAG systems where relevance is critical
- When document collections are too large for full cross-encoder search
- For complex queries where bi-encoder precision is insufficient
- When you can tolerate slightly higher latency for better results
- For applications with clear performance metrics (NDCG, precision@k)

## When NOT to Use This Skill
- When latency must be minimized (single bi-encoder is faster)
- For very small collections where full cross-encoder is feasible
- When bi-encoder already provides excellent relevance
- For simple keyword searches (BM25 may suffice)

## Related Skills
- [Hybrid Search BM25 Dense](./hybrid-search-bm25-dense.md) - First-stage enhancement
- [Semantic Chunking](../chunking/semantic-chunking.md) - Better input for retrieval
- [Optimize Retrieval Latency](../performance-optimization/optimize-retrieval-latency.md) - Performance tuning

## Metrics & Success Criteria
- **Relevance**: NDCG@10 improvement > 10% over bi-encoder alone
- **Latency**: Total retrieval < 500ms for typical queries
- **Recall**: Maintain > 95% recall of first stage
- **Reranking Quality**: Reranked top-10 should significantly outscore stage-1 top-10
- **Cost Efficiency**: Acceptable computational overhead vs. relevance gain
