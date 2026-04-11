---
name: retrieval-strategies
title: "Retrieval Strategies"
description: "Route RAG retrieval quality work across hybrid search, reranking, query transformation, HyDE, Self-RAG, RAPTOR, CRAG, and Graph RAG."
category: "retrieval-strategies"
tags: ["retrieval", "ranking", "hybrid-search", "rag"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Retrieval Strategies

## Overview
Use this parent skill when the main RAG problem is search quality, ranking, recall, context selection, or evidence traceability. Route to the child skill that best matches the retrieval failure.

## Problem Statement
Embedding search alone often misses exact terms, ranks weak evidence too high, or retrieves incomplete context. RAG systems need retrieval strategies that adapt to query type and evidence requirements.

## Key Concepts
- **Hybrid search**: Combine sparse and dense signals.
- **Reranking**: Reorder broad candidate sets with stronger relevance models.
- **Query transformation**: Rewrite, expand, or decompose user questions.
- **Corrective retrieval**: Validate and repair weak evidence before generation.

## Implementation Guide

### Step 1: Diagnose the Failure
Identify whether the issue is recall, ranking, query mismatch, missing context, or poor citations.

### Step 2: Select the Retrieval Pattern
Choose hybrid search for exact-term misses, reranking for noisy top-k results, query transformation for vague questions, and corrective patterns for unreliable evidence.

### Step 3: Evaluate With Grounded Metrics
Measure recall at k, MRR or nDCG, citation accuracy, answer faithfulness, and latency impact.

## When to Use This Skill
- Improving retrieval quality in an existing RAG pipeline
- Selecting a search pattern for a new RAG system
- Debugging weak citations or irrelevant context

## When NOT to Use This Skill
- The source content has not been parsed or chunked yet
- The main issue is vector database deployment
- The task is pure generation without retrieval

## Related Skills
- [Hybrid Search BM25 Dense](hybrid-search-bm25-dense/SKILL.md)
- [Multi-Pass Retrieval with Reranking](multi-pass-retrieval-with-reranking/SKILL.md)
- [Query Transformation Strategies](query-transformation-strategies/SKILL.md)
- [Adaptive Retrieval](adaptive-retrieval/SKILL.md)
- [Graph RAG](graph-rag/SKILL.md)

## Metrics & Success Criteria
- Improved recall and ranking quality on evaluation queries
- Better answer faithfulness and citation accuracy
- Latency remains acceptable for the product workflow
