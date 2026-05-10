---
name: multi-agent-rag-orchestration
title: "Multi-Agent RAG Orchestration"
description: "Coordinate planner and specialist agents to decompose, retrieve, and synthesize complex RAG answers."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "rag-agents"
tags: ["multi-agent", "orchestration", "planner", "decomposition"]
---

## Overview
Multi-agent orchestration splits a complex question across specialized agents, such as a planner, one or more retrievers, and a synthesizer. Each agent owns a narrow job, and a coordinator sequences them and merges the results into a single grounded answer.

## Problem Statement
Some questions require several independent lookups, cross-source reasoning, or distinct skills that a single prompt handles poorly. Cramming everything into one agent produces long, unfocused prompts and answers that quietly drop parts of the question.

## Key Concepts
- **Planner**: Decomposes the query into ordered or parallel subtasks.
- **Specialist agents**: Narrowly scoped workers, such as per-source retrievers.
- **Coordinator**: Sequences agents, handles failures, and enforces limits.
- **Synthesizer**: Merges partial results into one grounded, cited answer.

## Implementation Guide

### Step 1: Decompose the Query
Have a planner break the question into subtasks that can be handled independently, with explicit dependencies where order matters.

**Why**: Clear decomposition prevents subtasks from overlapping or dropping parts of the original question.

### Step 2: Assign Narrow Specialist Agents
Give each subtask to an agent with a single responsibility and only the tools it needs.

**Why**: Narrow scope keeps prompts short, decisions debuggable, and behavior predictable.

### Step 3: Synthesize and Attribute
Merge partial answers in a synthesis step that resolves conflicts and preserves source citations.

**Why**: A dedicated synthesis step avoids contradictory fragments and keeps the final answer traceable.

For a worked pattern, see the [Multi-Agent RAG example](../../../examples/multi-agent-rag.md) and the [LangGraph multi-agent guide](https://docs.langchain.com/oss/python/langgraph/multi-agent).

## When to Use This Skill
- Questions need several independent lookups or cross-source reasoning
- Subtasks require distinct skills or tools that one agent handles poorly
- You need parallelism across retrievers to cut wall-clock latency

## When NOT to Use This Skill
- Single-agent routing already answers the query well
- The added coordination cost and latency are not justified
- Subtasks are tightly coupled and cannot be cleanly separated

## Related Skills
- [Agentic RAG Routing](../agentic-rag-routing/SKILL.md) - Try routing before orchestration
- [Explainable Retrieval with Citations](../../retrieval-strategies/explainable-retrieval/SKILL.md) - Attribution during synthesis
- [Graph RAG](../../retrieval-strategies/graph-rag/SKILL.md) - Cross-entity reasoning
- [RAG Evaluation Frameworks](../../evaluation-metrics/rag-evaluation-frameworks/SKILL.md) - Evaluate the whole system

## Metrics & Success Criteria
- **Decomposition Quality**: Subtasks fully cover the original question
- **Answer Completeness**: Multi-part questions are answered in full
- **Latency**: Parallel agents keep end-to-end time acceptable
- **Traceability**: Each answer segment maps back to a source
