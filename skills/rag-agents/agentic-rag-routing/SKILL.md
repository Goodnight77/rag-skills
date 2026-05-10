---
name: agentic-rag-routing
title: "Agentic RAG Routing"
description: "Route each query to the right retrieval strategy, data source, or tool with an LLM-driven router."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "rag-agents"
tags: ["routing", "tool-use", "query-classification", "agentic-rag"]
---

## Overview
Agentic routing puts a decision step in front of retrieval: the agent classifies the query and chooses whether to retrieve, which source or index to hit, and which tool to call. This turns a one-size-fits-all pipeline into one that adapts per query.

## Problem Statement
Different queries need different handling. A definitional question, a multi-hop question, and a live-data question all fail under a single fixed retrieval path. Without routing, the pipeline over-retrieves for simple queries and under-serves complex ones.

## Key Concepts
- **Retrieval decision**: Whether the query needs retrieval at all.
- **Source routing**: Selecting the right index, collection, or tool for the query.
- **Query classification**: Mapping a query to a handling strategy.
- **Fallback**: A safe default path when the router is unsure.

## Implementation Guide

### Step 1: Define the Route Space
Enumerate the concrete routes available, such as no-retrieval, vector search, keyword search, web search, or a structured-data tool.

**Why**: A router can only choose from routes you have defined; an open-ended router is unpredictable and hard to evaluate.

### Step 2: Classify the Query
Use an LLM or a lightweight classifier to map each query to a route, returning a structured decision rather than free text.

**Why**: Structured routing decisions are testable and can be logged, replayed, and evaluated.

### Step 3: Add Fallback and Guardrails
Define a default route for low-confidence decisions and cap how many tools or hops a single query may trigger.

**Why**: Guardrails prevent runaway tool loops and keep latency and cost bounded.

For patterns, see the [LangGraph agentic RAG guide](https://docs.langchain.com/oss/python/langgraph/agentic-rag) and the [LlamaIndex router query engine](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/).

## When to Use This Skill
- Queries span multiple sources, formats, or freshness needs
- Some queries need no retrieval and others need several hops
- You want per-query control before adding full multi-agent orchestration

## When NOT to Use This Skill
- All queries are answered well by one retrieval path
- The extra classification call breaks the latency budget
- There is only one data source and no tool choice to make

## Related Skills
- [Adaptive Retrieval](../../retrieval-strategies/adaptive-retrieval/SKILL.md) - Strategy selection by query type
- [Self-RAG](../../retrieval-strategies/self-rag/SKILL.md) - Retrieval decisions at generation time
- [CRAG - Corrective RAG](../../retrieval-strategies/crag-corrective-rag/SKILL.md) - Fallback search on weak retrieval
- [Multi-Agent RAG Orchestration](../multi-agent-rag-orchestration/SKILL.md) - When routing is not enough

## Metrics & Success Criteria
- **Route Accuracy**: Queries reach the correct handling path
- **No-Retrieve Savings**: Simple queries skip unnecessary retrieval
- **Bounded Cost**: Tool and hop counts stay within limits
- **Fallback Rate**: Low-confidence routing stays rare and safe
