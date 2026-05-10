---
name: crag-corrective-rag
title: "CRAG - Corrective RAG"
description: "Dynamically evaluate and correct retrieval quality using relevance scores and web search."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["crag", "corrective", "web-search", "relevance-evaluation", "dynamic-correction"]
---

## Overview
Corrective RAG (CRAG) extends standard retrieval by dynamically evaluating document relevance and correcting the retrieval process when needed. It combines local knowledge bases with web search, using relevance scores to determine whether to use retrieved documents, supplement with web results, or rely entirely on external sources.

## Problem Statement
Traditional RAG systems have limitations when retrieved information is insufficient:
- **Irrelevant Retrieval**: Retrieved documents may not adequately address the query
- **Outdated Information**: Local knowledge bases may contain stale information
- **No Quality Assessment**: No mechanism to evaluate retrieval quality
- **Inflexible Sources**: Cannot supplement or replace poor local retrieval
- **Static Process**: Same retrieval approach regardless of query characteristics

## Key Concepts
- **Retrieval Evaluation**: Scoring document relevance to determine quality
- **Dynamic Correction**: Adapting retrieval strategy based on evaluation results
- **Web Search Supplementation**: Using web search when local retrieval is insufficient
- **Knowledge Refinement**: Extracting key information from documents
- **Source Selection**: Choosing between local and external knowledge based on quality

## Implementation Guide

### Step 1: Implement Retrieval Evaluation
Score each retrieved document for its relevance to the query.

**Why**: Relevance evaluation provides a quantitative measure of retrieval quality, enabling data-driven decisions about correction strategies.

Use an LLM to score each retrieved document on a scale from 0 to 1 based on how well it addresses the query.

### Step 2: Implement Decision Logic
Determine correction strategy based on relevance scores.

**Why**: Different relevance levels require different approaches - high relevance uses local content, low relevance triggers web search, ambiguous cases combine both.

- High relevance (>0.7): Use local retrieval as-is
- Low relevance (<0.3): Rely on web search
- Ambiguous (0.3-0.7): Combine local and web

### Step 3: Implement Query Rewriting for Web Search
Optimize queries for web searching when external knowledge is needed.

**Why**: Web search engines respond better to properly formatted queries. Rewriting improves web search results.

Rewrite the query to be more suitable for web search engines while maintaining the original intent.

### Step 4: Implement Knowledge Refinement
Extract key information from documents for use in response generation.

**Why**: Raw documents may contain excessive detail. Refinement extracts the most relevant information for efficient response generation.

Extract bullet points or key information from documents to focus on the most relevant content.

### Step 5: Implement Web Search Integration
Fetch and process web search results when needed.

**Why**: Web search provides up-to-date information and can supplement or replace insufficient local retrieval.

Integrate with web search APIs (e.g., DuckDuckGo, Bing) to fetch external information when local retrieval is insufficient.

### Step 6: Implement Response Generation
Generate responses using appropriate knowledge sources based on correction strategy.

**Why**: The response generator must handle different knowledge sources - local documents, web results, or combined information - with appropriate attribution.

Generate responses conditioned on the correction strategy: using local content, web results, or combined sources.

### Step 7: Build Complete CRAG Pipeline
Combine all components into a cohesive corrective system.

**Why**: A complete pipeline with evaluation, decision logic, web search, and response generation provides a robust retrieval system that adapts to information quality.

For implementation patterns, see the [CRAG paper](https://arxiv.org/abs/2401.15884), [LangChain tools documentation](https://docs.langchain.com/oss/python/langchain/tools), and the [Self-RAG paper](https://arxiv.org/abs/2310.11511) for related concepts.

## When to Use This Skill
- Building RAG systems where information quality varies significantly
- When local knowledge may be outdated or incomplete
- For applications requiring high accuracy and up-to-date information
- When web search is available as a fallback source
- For domains with rapidly changing information (news, technology, finance)

## When NOT to Use This Skill
- For systems without web search access
- When local knowledge is comprehensive and current
- For latency-critical applications (web search adds variability)
- When offline operation is required
- For domains where external sources are unreliable or restricted

## Related Skills
- [Self-RAG](../self-rag/SKILL.md) - Reflective retrieval decisions
- [Adaptive Retrieval](../adaptive-retrieval/SKILL.md) - Dynamic strategy selection
- [Query Transformation Strategies](../query-transformation-strategies/SKILL.md) - Query enhancement methods

## Metrics & Success Criteria
- **Relevance Assessment**: Accurate scoring of document relevance
- **Correction Effectiveness**: Improved response quality through dynamic correction
- **Web Search Quality**: Relevant and reliable web search results
- **Response Accuracy**: Higher factual accuracy compared to baseline
- **Latency Acceptability**: Web search overhead remains acceptable for use case
