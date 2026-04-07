---
title: "Adaptive Retrieval"
description: "Dynamically select retrieval strategies based on query type and characteristics."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["adaptive", "query-classification", "dynamic-strategy", "multi-strategy"]
---

## Overview
Adaptive retrieval classifies queries into types (factual, analytical, opinion, contextual) and applies different retrieval strategies optimized for each type. This dynamic approach ensures that each query receives the most appropriate treatment for optimal results.

## Problem Statement
One-size-fits-all retrieval has inherent limitations:
- **Query Diversity**: Different query types require different retrieval approaches
- **Factual Queries**: Need precision and specific information
- **Analytical Queries**: Require comprehensive, diverse information
- **Opinion Queries**: Benefit from multiple viewpoints and perspectives
- **Contextual Queries**: Depend on user-specific context and history

## Key Concepts
- **Query Classification**: Categorizing queries by their nature and intent
- **Strategy Selection**: Choosing optimal retrieval method per query type
- **Factual Strategy**: Query enhancement with precise ranking
- **Analytical Strategy**: Sub-query generation for comprehensive coverage
- **Opinion Strategy**: Viewpoint identification and diversity selection
- **Contextual Strategy**: User context integration

## Implementation Guide

### Step 1: Implement Query Classifier
Use an LLM to classify queries into types.

**Why**: Accurate classification is the foundation of adaptive retrieval—the right strategy depends on correctly identifying the query type.

Direct the LLM to classify queries into categories: factual, analytical, opinion, or contextual.

### Step 2: Implement Factual Retrieval Strategy
Enhance queries for precision and rank results by relevance.

**Why**: Factual queries benefit from query enhancement that adds relevant terminology and precise ranking that identifies the most authoritative sources.

Rewrite the query to be more specific, retrieve more candidates, and re-rank by relevance to the original query.

### Step 3: Implement Analytical Retrieval Strategy
Generate sub-queries and ensure diversity in results.

**Why**: Analytical queries need coverage of multiple aspects. Sub-query decomposition and diversity selection ensure comprehensive information gathering.

Break down the query into sub-questions, retrieve for each, and select a diverse set of results.

### Step 4: Implement Opinion Retrieval Strategy
Identify viewpoints and select diverse opinions.

**Why**: Opinion queries require multiple perspectives. Viewpoint identification ensures retrieval represents different stances on the topic.

Identify distinct viewpoints on the topic, retrieve for each viewpoint, and select diverse opinions.

### Step 5: Implement Contextual Retrieval Strategy
Incorporate user context into the query.

**Why**: Contextual queries depend on user-specific information. Incorporating context ensures retrieval matches the user's situation and needs.

Reformulate the query to include user context, then retrieve and rank results considering both relevance and context.

### Step 6: Build Adaptive Retriever
Combine all strategies into a unified system.

**Why**: A unified adaptive retriever provides a single interface that automatically selects the optimal strategy for each query.

Route queries to the appropriate strategy based on classification, then execute retrieval using the selected method.

For implementation patterns, see [LangChain router architecture](https://docs.langchain.com/oss/python/langchain/multi-agent/router), [LlamaIndex RouterQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/), and the [Self-RAG paper](https://arxiv.org/abs/2310.11511) for related concepts.

## When to Use This Skill
- Building RAG systems handling diverse query types
- When users ask factual, analytical, and opinion-based questions
- For applications where user context matters (personalized systems)
- When you have the flexibility to implement multiple retrieval strategies
- For domains with clear query type patterns (medical, legal, technical)

## When NOT to Use This Skill
- For systems with uniform query types (e.g., only factual)
- When implementation simplicity is prioritized over optimization
- For latency-critical applications (classification adds overhead)
- When single strategy already provides excellent results
- For very small document collections where strategy differences are minimal

## Related Skills
- [Query Transformation Strategies](./query-transformation-strategies.md) - Query enhancement methods
- [Self-RAG](./self-rag.md) - Reflective retrieval decisions
- [HyDE](./hyde-hypothetical-document-embeddings.md) - Query expansion technique

## Metrics & Success Criteria
- **Classification Accuracy**: High accuracy in identifying query types (> 85%)
- **Strategy Effectiveness**: Each strategy outperforms generic retrieval for its query type
- **Overall Quality**: Improved retrieval quality across diverse queries
- **Latency**: Acceptable overhead for classification and strategy selection (< 200ms)
- **Adaptiveness**: System dynamically responds to different query characteristics
