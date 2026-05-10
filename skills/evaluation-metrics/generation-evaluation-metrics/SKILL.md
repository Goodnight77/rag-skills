---
name: generation-evaluation-metrics
title: "Generation Evaluation Metrics"
description: "Score RAG answers for faithfulness, answer relevancy, and correctness using LLM-as-judge methods."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "evaluation-metrics"
tags: ["generation", "faithfulness", "llm-as-judge", "hallucination"]
---

## Overview
Generation evaluation measures the answer itself: whether it is grounded in the retrieved context, addresses the question, and is factually correct. These metrics catch hallucination and drift that retrieval metrics cannot see.

## Problem Statement
A pipeline can retrieve perfect context and still produce a wrong, unsupported, or off-topic answer. Exact-match and BLEU-style scores fail on open-ended answers, so teams need semantic and grounding-aware evaluation instead.

## Key Concepts
- **Faithfulness**: Whether every claim in the answer is supported by the retrieved context.
- **Answer relevancy**: Whether the answer actually addresses the question asked.
- **Correctness**: Whether the answer agrees with a reference or ground-truth answer.
- **LLM-as-judge**: Using a strong model with a rubric to score answers at scale.
- **Hallucination rate**: Share of answers containing claims not grounded in context.

## Implementation Guide

### Step 1: Separate Grounding from Correctness
Score faithfulness against the retrieved context and correctness against a reference answer as two different numbers.

**Why**: An answer can be faithful to bad context yet wrong, or correct yet unsupported; conflating them hides both failure modes.

### Step 2: Use LLM-as-Judge with a Fixed Rubric
Define an explicit rubric and score with a strong judge model, requesting a short justification alongside each score.

**Why**: A fixed rubric and recorded rationale make LLM judgments repeatable and auditable instead of arbitrary.

### Step 3: Calibrate the Judge Against Humans
Spot-check a sample of judge scores against human labels and adjust the rubric until they agree.

**Why**: An uncalibrated judge produces confident but misleading numbers; calibration keeps automated scores trustworthy.

For rubrics and implementations, see [RAGAS generation metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/), [DeepEval metrics](https://docs.confident-ai.com/docs/metrics-introduction), and the [G-Eval paper](https://arxiv.org/abs/2303.16634).

## When to Use This Skill
- Detecting hallucination and ungrounded claims in answers
- Comparing prompts, models, or generation settings on answer quality
- Adding an answer-quality gate on top of retrieval metrics

## When NOT to Use This Skill
- The bottleneck is retrieval and context is already known to be poor
- Answers are short exact facts where deterministic matching is enough
- No reference answers or grounding context exist to judge against

## Related Skills
- [Retrieval Evaluation Metrics](../retrieval-evaluation-metrics/SKILL.md) - Score the context, not the answer
- [RAG Evaluation Frameworks](../rag-evaluation-frameworks/SKILL.md) - Tools that compute these metrics
- [Self-RAG](../../retrieval-strategies/self-rag/SKILL.md) - Self-assessed grounding at runtime
- [Explainable Retrieval with Citations](../../retrieval-strategies/explainable-retrieval/SKILL.md) - Traceable grounding

## Metrics & Success Criteria
- **Faithfulness**: High share of answer claims traceable to retrieved context
- **Answer Relevancy**: Answers consistently address the question asked
- **Correctness**: Strong agreement with reference answers on the golden set
- **Judge Calibration**: LLM-as-judge scores align with sampled human labels
