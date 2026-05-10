---
name: rag-agents
title: "RAG Agents"
description: "Route agentic RAG work across query routing, tool-use retrieval, and multi-agent orchestration."
category: "rag-agents"
tags: ["agents", "agentic-rag", "orchestration", "routing"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# RAG Agents

## Overview
Use this parent skill when a single retrieve-then-generate pass is not enough and the system must decide what to retrieve, which tools to call, or how to split work across agents. Route to the child skill that matches whether the problem is routing decisions or multi-agent orchestration.

## Problem Statement
Static RAG pipelines answer every query the same way: one retrieval, one generation. Complex questions need conditional retrieval, multiple sources, tool calls, or decomposition into subtasks. Bolting this onto a linear pipeline produces brittle, hard-to-debug systems.

## Key Concepts
- **Routing**: Deciding whether and where to retrieve before answering.
- **Tool use**: Treating retrievers, search, and calculators as callable tools.
- **Decomposition**: Breaking a complex query into ordered subtasks.
- **Orchestration**: Coordinating specialized agents and merging their outputs.

## Implementation Guide

### Step 1: Decide If You Need an Agent at All
Add agentic control only when queries genuinely vary in required steps or sources. A fixed pipeline is cheaper and easier to evaluate.

### Step 2: Start with Routing, Not Multi-Agent
Add a router that chooses retrieval strategy or tool per query before reaching for multiple coordinated agents.

### Step 3: Introduce Orchestration Only When Justified
Move to planner and worker agents when subtasks are genuinely independent or need specialized handling, and keep each agent narrowly scoped.

## When to Use This Skill
- Queries need conditional retrieval, multiple sources, or tool calls
- A single retrieval pass produces incomplete or shallow answers
- Work naturally decomposes into specialized subtasks

## When NOT to Use This Skill
- A fixed retrieve-then-generate pipeline already answers well
- Latency and cost budgets cannot absorb extra LLM calls
- The real bottleneck is retrieval quality, not control flow

## Related Skills
- [Agentic RAG Routing](agentic-rag-routing/SKILL.md)
- [Multi-Agent RAG Orchestration](multi-agent-rag-orchestration/SKILL.md)
- [Adaptive Retrieval](../retrieval-strategies/adaptive-retrieval/SKILL.md)
- [Self-RAG](../retrieval-strategies/self-rag/SKILL.md)

## Metrics & Success Criteria
- Agentic control measurably improves answers over a fixed pipeline
- Each added LLM call earns its latency and cost
- Routing and agent decisions are traceable and debuggable
