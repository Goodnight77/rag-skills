---
name: rag-evaluation-frameworks
title: "RAG Evaluation Frameworks"
description: "Choose and wire up a RAG evaluation framework and turn it into a CI regression gate."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "evaluation-metrics"
tags: ["ragas", "deepeval", "trulens", "ci", "regression"]
---

## Overview
This skill covers the tooling layer of RAG evaluation: which framework to adopt, how to structure a golden set, and how to run evaluation automatically on every change so quality regressions are blocked before they ship.

## Problem Statement
Metrics are only useful if they run consistently. Teams compute scores once in a notebook, never automate them, and lose the baseline. Ad hoc evaluation cannot catch the slow regressions that come from data drift, prompt edits, or model swaps.

## Key Concepts
- **Evaluation framework**: A library that computes retrieval and generation metrics from a dataset of questions, contexts, and answers.
- **Golden set**: Version-controlled questions with reference answers and relevant contexts.
- **Reference-free vs reference-based**: Whether a metric needs ground-truth answers or judges quality directly.
- **Regression gate**: A CI job that fails when metrics drop below the baseline.

## Implementation Guide

### Step 1: Choose a Framework by Fit
Pick the framework that matches your stack rather than the most popular one.

**Why**: Each tool has a different data model and integration story, and switching later is costly.

Default mapping:
- Metric-first RAG scoring with minimal setup: favor [RAGAS](https://docs.ragas.io/)
- Unit-test-style assertions and CI integration: favor [DeepEval](https://docs.confident-ai.com/)
- Live instrumentation and dashboards for running apps: favor [TruLens](https://www.trulens.org/)
- Prompt and provider comparison matrices: favor [promptfoo](https://www.promptfoo.dev/)

### Step 2: Build a Versioned Golden Set
Curate representative questions with reference answers and relevant contexts, and commit it to the repository.

**Why**: A fixed, version-controlled dataset makes scores comparable across runs and contributors.

### Step 3: Wire Evaluation into CI
Run the framework on the golden set in CI and fail the build when scores regress past a threshold.

**Why**: An automated gate turns evaluation from a one-time report into a standing guardrail.

## When to Use This Skill
- Standing up a repeatable evaluation pipeline for the first time
- Adding an automated quality gate to a RAG project
- Comparing tools before committing to one evaluation stack

## When NOT to Use This Skill
- You only need the definition of a single metric, not tooling
- The project is a throwaway prototype with no regression risk
- There is no golden set and none can be created yet

## Related Skills
- [Retrieval Evaluation Metrics](../retrieval-evaluation-metrics/SKILL.md) - Metrics these tools compute
- [Generation Evaluation Metrics](../generation-evaluation-metrics/SKILL.md) - Answer-quality metrics
- [Production RAG Deployment](../../deployment/production-rag-deployment/SKILL.md) - Gate deployments on scores
- [Optimize Retrieval Latency](../../performance-optimization/optimize-retrieval-latency/SKILL.md) - Balance quality against speed

## Metrics & Success Criteria
- **Reproducibility**: Same golden set yields comparable scores across runs
- **Coverage**: Golden set spans the real query distribution
- **Automation**: Evaluation runs in CI on every relevant change
- **Actionability**: A failing gate points to the layer that regressed
