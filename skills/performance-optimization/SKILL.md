---
name: performance-optimization
title: "Performance Optimization"
description: "Route RAG performance work for latency, caching, indexing, filtering, batching, and query optimization."
category: "performance-optimization"
tags: ["latency", "performance", "caching", "rag"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Performance Optimization

## Overview
Use this parent skill when the RAG system works functionally but is too slow, expensive, or unstable under expected traffic. Route to targeted latency and retrieval optimization guidance.

## Problem Statement
RAG latency can come from embedding calls, vector search, metadata filters, reranking, prompt assembly, or repeated work. Optimization requires profiling the full retrieval path before changing architecture.

## Key Concepts
- **Latency budget**: Allocate time across embedding, retrieval, reranking, and generation.
- **Caching**: Avoid repeated work for common queries and stable documents.
- **Index tuning**: Match search parameters and indexes to workload.
- **Query planning**: Reduce unnecessary retrieval and reranking work.

## Implementation Guide

### Step 1: Profile the Retrieval Path
Measure embedding, search, filtering, reranking, prompt assembly, and model latency separately.

### Step 2: Apply Targeted Optimizations
Use caching, batching, payload indexes, top-k tuning, and reranker gating where profiling shows bottlenecks.

### Step 3: Recheck Quality and Cost
Confirm optimizations do not reduce recall, faithfulness, citation quality, or operational reliability.

## When to Use This Skill
- Retrieval is too slow for the product experience
- Reranking or query expansion adds too much latency
- Metadata filters or vector indexes need tuning

## When NOT to Use This Skill
- Retrieval quality is poor but latency is acceptable
- The corpus has not been chunked or indexed yet
- The system lacks baseline measurements

## Related Skills
- [Optimize Retrieval Latency](optimize-retrieval-latency/SKILL.md)
- [Qdrant for Production RAG](../vector-databases/qdrant-for-production-rag/SKILL.md)
- [Multi-Pass Retrieval with Reranking](../retrieval-strategies/multi-pass-retrieval-with-reranking/SKILL.md)

## Metrics & Success Criteria
- Lower p50 and p95 retrieval latency
- Stable answer quality after optimization
- Reduced cost per query without hiding failures
