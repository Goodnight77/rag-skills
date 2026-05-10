---
name: retrieval-evaluation-metrics
title: "Retrieval Evaluation Metrics"
description: "Measure retrieval quality with recall, precision, MRR, nDCG, and context precision and recall."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "evaluation-metrics"
tags: ["retrieval", "recall", "ndcg", "mrr", "context-precision"]
---

## Overview
Retrieval evaluation measures whether the pipeline fetched the right chunks before the LLM ever sees them. Because generation quality is capped by retrieval quality, these metrics isolate the most common and most fixable source of bad RAG answers.

## Problem Statement
Teams judge RAG only by final answer quality, which hides where the failure is. When the right chunk is never retrieved, no prompt or model change can recover, yet the pipeline is often blamed on generation instead of retrieval.

## Key Concepts
- **Recall@k**: Fraction of relevant chunks that appear in the top k results.
- **Precision@k**: Fraction of the top k results that are actually relevant.
- **MRR (Mean Reciprocal Rank)**: Rewards putting the first relevant chunk near the top.
- **nDCG**: Rank-aware score that weights relevant results higher when ranked earlier.
- **Context precision and recall**: RAGAS-style metrics that judge whether retrieved context is relevant and complete for answering the question.

## Implementation Guide

### Step 1: Build a Labeled Query Set
Collect representative questions and mark which document chunks are relevant to each. This golden set is the ground truth every metric compares against.

**Why**: Rank-based metrics are meaningless without known-relevant targets to score against.

### Step 2: Measure Recall Before Precision
Start with recall@k across candidate k values to confirm relevant chunks are retrieved at all, then check precision and rank quality with MRR and nDCG.

**Why**: A relevant chunk that is never retrieved cannot be re-ranked into place, so recall is the ceiling for everything downstream.

### Step 3: Add Reference-Free Context Metrics
Use LLM-judged context precision and context recall when human relevance labels are scarce, to score whether retrieved context supports the reference answer.

**Why**: Manual relevance labels are expensive; reference-free metrics scale evaluation to larger query sets.

For definitions and implementations, see [RAGAS context metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/), the [RAGAS paper](https://arxiv.org/abs/2309.15217), and [scikit-learn ranking metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#ranking-metrics).

## When to Use This Skill
- Diagnosing whether bad answers come from retrieval rather than generation
- Comparing chunking strategies, embedding models, or rerankers objectively
- Setting a recall baseline before tuning downstream generation

## When NOT to Use This Skill
- Retrieved context is already known to be good and answers are still wrong
- The corpus has no relevance labels and none can be produced or approximated
- The system does not retrieve (pure generative or closed-book setups)

## Related Skills
- [Generation Evaluation Metrics](../generation-evaluation-metrics/SKILL.md) - Score the answer, not the context
- [RAG Evaluation Frameworks](../rag-evaluation-frameworks/SKILL.md) - Tools that compute these metrics
- [Multi-Pass Retrieval with Reranking](../../retrieval-strategies/multi-pass-retrieval-with-reranking/SKILL.md) - Improve rank-based scores
- [Hybrid Search BM25 Dense](../../retrieval-strategies/hybrid-search-bm25-dense/SKILL.md) - Improve recall

## Metrics & Success Criteria
- **Recall@k**: High enough that relevant context is almost always present in the top k
- **MRR / nDCG**: Relevant chunks ranked near the top, not buried
- **Context Precision**: Low share of irrelevant chunks in the final context
- **Stability**: Metrics computed on a fixed golden set for run-to-run comparison
