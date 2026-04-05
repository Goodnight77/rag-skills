---
title: "Optimize Retrieval Latency"
description: "Reduce retrieval latency with caching, batching, and index-level optimization."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "performance-optimization"
tags": ["latency", "performance", "caching", "indexing", "optimization"]
---

## Overview
Optimizing RAG retrieval latency is critical for production applications where user experience depends on fast response times. This skill covers techniques to reduce query latency at every stage: indexing, embedding generation, search execution, and result processing.

## Problem Statement
RAG systems often have latency issues:
- Vector search operations take hundreds of milliseconds
- Embedding generation adds significant per-query overhead
- Network round trips between services compound delays
- Cold starts cause unpredictable latency spikes
- Trade-offs between accuracy and speed are unclear

## Key Concepts
- **Query Path**: Full journey from user request to retrieved results
- **Hot Path Optimization**: Focus on frequently executed operations
- **Cold Path**: Infrequent operations where accuracy matters more than speed
- **Caching Strategies**: Multi-level caching for repeated queries and embeddings
- **Index Tuning**: Balancing recall, build time, and search speed

## Implementation Guide

### Step 1: Measure Current Performance
Establish baseline measurements before optimization.

**Why**: You can't optimize what you don't measure. Profiling reveals the actual bottlenecks rather than assumptions.

### Step 2: Optimize Embedding Generation
Reduce the overhead of generating query embeddings.

**Why**: Embedding generation is often the bottleneck—caching reduces this overhead for repeated queries.

### Step 3: Optimize Vector Database Operations
Tune indexing and search parameters for latency.

**Why**: Index parameters directly impact search latency—lower `ef` values reduce search time at the cost of recall.

### Step 4: Implement Multi-Level Caching
Cache at multiple levels to reduce redundant work.

**Why**: Multi-level caching reduces computation for repeated queries without sacrificing freshness for unique queries.

### Step 5: Optimize Result Processing
Stream results and minimize post-processing overhead.

**Why**: Streaming reduces memory usage and allows users to see results sooner, improving perceived latency.

### Step 6: Implement Query Prioritization
Prioritize and batch queries for better resource utilization.

**Why**: Query prioritization ensures important queries get resources first and reduces contention.

Useful references include the [Qdrant production guide](https://qdrant.tech/documentation/guides/production/), [Qdrant snapshots concept](https://qdrant.tech/documentation/concepts/snapshots/), [ANN Benchmarks](https://ann-benchmarks.com/), and [AWS caching best practices](https://aws.amazon.com/caching/best-practices/).

## When to Use This Skill
- Production RAG systems with latency SLAs
- High-traffic applications (> 100 QPS)
- When user experience is critical
- Systems with repeat queries
- Resource-constrained environments

## When NOT to Use This Skill
- Early prototyping (premature optimization)
- Very low traffic (< 1 QPS)
- When accuracy is more important than speed
- For one-off batch operations

## Related Skills
- [Qdrant for Production RAG](../vector-databases/qdrant-for-production-rag.md) - Production setup
- [Multi-Pass Retrieval with Reranking](../retrieval-strategies/multi-pass-retrieval-with-reranking.md) - Two-stage optimization
- [Hybrid Search BM25 Dense](../retrieval-strategies/hybrid-search-bm25-dense.md) - Query optimization

## Metrics & Success Criteria
- **End-to-End Latency**: P50 < 100ms, P99 < 500ms for typical queries
- **Cache Hit Rate**: > 60% for common queries
- **Throughput**: > 100 QPS per instance
- **Recall Degradation**: < 5% vs. unoptimized baseline
- **Resource Efficiency**: CPU < 80%, Memory usage stable
