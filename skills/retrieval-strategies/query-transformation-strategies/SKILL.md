---
name: query-transformation-strategies
title: "Query Transformation Strategies"
description: "Use query rewriting, step-back prompting, and sub-query decomposition to improve retrieval quality and comprehensiveness."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["query-expansion", "step-back", "sub-query", "query-rewriting"]
---

## Overview
Query transformation strategies modify or expand user queries before retrieval to bridge the gap between natural language queries and document representations. These techniques improve retrieval relevance by generating multiple query variants, each targeting different aspects of the information need.

## Problem Statement
Direct query-to-document matching has inherent limitations:
- **Ambiguity**: Natural language queries often contain unclear terms or multiple interpretations
- **Style Mismatch**: User queries differ in structure and vocabulary from indexed documents
- **Incomplete Information**: Single queries may not capture all relevant aspects of complex information needs
- **Context Insensitivity**: Direct queries don't account for broader context or domain knowledge

## Key Concepts
- **Query Rewriting**: Reformulating queries to be more specific and detailed
- **Step-back Prompting**: Generating broader, more general queries for context retrieval
- **Sub-query Decomposition**: Breaking complex queries into simpler, component questions
- **Query Expansion**: Adding related terms and concepts to the original query
- **Multi-Query Retrieval**: Executing multiple query variants and combining results

## Implementation Guide

### Step 1: Implement Query Rewriting
Use an LLM to reformulate the original query into a more detailed, specific version.

**Why**: Enhanced queries include relevant terminology, proper context, and specific aspects that the original query might miss. This improves matching with technical documents and domain-specific content.

Instruct the LLM to expand queries with relevant domain terminology, clarify ambiguous terms, and add context that would appear in target documents.

### Step 2: Implement Step-back Prompting
Generate a broader, more general version of the query to retrieve foundational context.

**Why**: Step-back queries provide background information and fundamental concepts that help ground more specific answers. This is especially valuable for technical topics where understanding basics is essential.

Generate step-back queries that capture higher-level concepts, general principles, or background knowledge related to the specific query.

### Step 3: Implement Sub-query Decomposition
Break down complex queries into 2-4 simpler sub-questions covering different aspects.

**Why**: Sub-query decomposition ensures comprehensive coverage of multi-faceted questions. Each sub-query targets a different aspect, allowing retrieval of diverse information that together provide a complete answer.

Direct the LLM to identify component questions that, when answered together, comprehensively address the original query.

### Step 4: Build Multi-Query Retrieval Pipeline
Execute multiple query variants and combine their retrieval results.

**Why**: Multi-query retrieval increases recall by retrieving documents matched by different query formulations. Combining results ensures broader coverage and higher likelihood of finding relevant information.

Retrieve documents for each query variant, then deduplicate results and re-rank by relevance to the original query.

### Step 5: Implement Result Fusion Strategy
Combine results from different query transformations using scoring and deduplication.

**Why**: Result fusion prevents redundant information and prioritizes the most relevant documents across all query variants. A weighted scoring approach balances specificity with comprehensiveness.

Use reciprocal rank fusion (RRF) or weighted scoring to combine results from different query variants.

For implementation patterns, see [LangChain routing workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [LlamaIndex Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/), and the [Step-back prompting paper](https://arxiv.org/abs/2310.06117).

## When to Use This Skill
- Building RAG systems where query ambiguity is common
- Handling complex, multi-faceted user questions
- When documents use different terminology than users
- For domains requiring both specific details and broad context
- When single-query retrieval produces incomplete or irrelevant results

## When NOT to Use This Skill
- For very simple, direct queries (single-step retrieval is faster)
- When latency must be minimized (query transformation adds LLM calls)
- When query-document alignment is already excellent
- For real-time systems with strict latency budgets
- When using datasets where queries are already well-formulated

## Related Skills
- [HyDE](../hyde-hypothetical-document-embeddings/SKILL.md) - Different query expansion approach
- [Fusion Retrieval](../hybrid-search-bm25-dense/SKILL.md) - Combining multiple retrieval signals
- [Adaptive Retrieval](../adaptive-retrieval/SKILL.md) - Dynamic query processing

## Metrics & Success Criteria
- **Retrieval Recall**: Increased recall for complex queries by 15-25%
- **Query Coverage**: Multiple query variants cover different aspects of information need
- **Result Quality**: More comprehensive and relevant document sets
- **Latency**: End-to-end latency increase < 500ms for typical queries
- **Cost Efficiency**: LLM calls balanced against relevance improvements
