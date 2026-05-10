---
name: evaluation-metrics
title: "Evaluation Metrics"
description: "Route RAG evaluation work across retrieval metrics, generation quality, and end-to-end evaluation frameworks."
category: "evaluation-metrics"
tags: ["evaluation", "metrics", "ragas", "routing"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Evaluation Metrics

## Overview
Use this parent skill when the main RAG problem is measuring quality, detecting regressions, or proving that a change actually helped. Route to the child skill that matches whether the failure is in retrieval, in generation, or in the evaluation harness itself.

## Problem Statement
Teams ship RAG changes with no baseline, tune on vibes, and cannot tell whether a new chunker, embedding model, or prompt made things better or worse. Without metrics, retrieval and generation regressions ship silently and are only caught by users.

## Key Concepts
- **Retrieval metrics**: Whether the right chunks were fetched (recall@k, precision@k, MRR, nDCG, context precision/recall).
- **Generation metrics**: Whether the answer is grounded and useful (faithfulness, answer relevancy, correctness).
- **Golden set**: A labeled question-and-answer set used as the fixed baseline for comparison.
- **Regression harness**: An automated evaluation run on every change, wired into CI.

## Implementation Guide

### Step 1: Isolate the Layer That Fails
Measure retrieval and generation separately. Bad answers from good context are a generation problem; good answers are impossible from bad context.

### Step 2: Pick Metrics for That Layer
Use retrieval metrics when the right chunks are missing or mis-ranked, and generation metrics when context is good but answers are wrong, unsupported, or off-topic.

### Step 3: Automate as a Regression Gate
Build a golden set, run the metrics on every change, and block merges that regress the baseline instead of evaluating manually.

## When to Use This Skill
- Choosing which metrics to track for a new or existing RAG pipeline
- Proving whether a chunking, embedding, or prompt change helped
- Setting up an automated evaluation gate before deployment

## When NOT to Use This Skill
- The pipeline is not yet built and there is nothing to measure
- The bottleneck is a known implementation bug, not quality measurement
- You already have a metrics suite and the problem is retrieval or generation design

## Related Skills
- [Retrieval Evaluation Metrics](retrieval-evaluation-metrics/SKILL.md)
- [Generation Evaluation Metrics](generation-evaluation-metrics/SKILL.md)
- [RAG Evaluation Frameworks](rag-evaluation-frameworks/SKILL.md)
- [Self-RAG](../retrieval-strategies/self-rag/SKILL.md)

## Metrics & Success Criteria
- Every RAG change is compared against a fixed golden-set baseline
- Retrieval and generation quality are tracked as separate numbers
- Regressions are caught in CI instead of by users
