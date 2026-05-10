---
name: production-rag-deployment
title: "Production RAG Deployment"
description: "Serve, scale, and safely roll out a RAG pipeline with health checks, caching, and canary releases."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "deployment"
tags: ["serving", "scaling", "canary", "observability"]
---

## Overview
This skill covers turning a working RAG pipeline into a reliable production service: exposing it behind an API, scaling retrieval and generation independently, caching hot paths, and rolling out changes without breaking users.

## Problem Statement
Prototype RAG code assumes one user, a warm index, and unlimited time. In production it faces concurrency, cold starts, provider timeouts, and cost limits. Without serving discipline, latency spikes, failures cascade, and a bad deploy hits every user at once.

## Key Concepts
- **Independent scaling**: Retrieval and LLM generation have different resource profiles and scale separately.
- **Caching**: Reusing embeddings and answers for repeated or similar queries.
- **Graceful degradation**: Falling back to a simpler path when a component fails.
- **Canary rollout**: Shipping a change to a small traffic slice before full release.

## Implementation Guide

### Step 1: Expose the Pipeline Behind a Service
Wrap retrieval and generation in an API with timeouts, retries, and health checks for each dependency.

**Why**: Explicit timeouts and health checks stop a slow vector store or LLM from stalling the whole request path.

### Step 2: Scale and Cache the Hot Paths
Scale the retrieval and generation tiers independently and cache embeddings and frequent answers.

**Why**: Retrieval and generation bottleneck differently, and caching removes repeated cost and latency on common queries.

### Step 3: Roll Out with Canaries and Fallbacks
Release changes to a small traffic slice first and define a degraded path when a component is unavailable.

**Why**: Canary releases and fallbacks contain the blast radius of a bad deploy or a failing dependency.

For infrastructure patterns, see the [Qdrant Cloud documentation](https://qdrant.tech/documentation/cloud/) and the [Ray Serve LLM guide](https://docs.ray.io/en/latest/serve/llm/serving-llms.html).

## When to Use This Skill
- Taking a validated RAG pipeline to real users and traffic
- The service must stay responsive under concurrency and failures
- You need safe, reversible rollouts of pipeline changes

## When NOT to Use This Skill
- The system is still an experiment with no live traffic
- A fully managed RAG platform already handles serving
- The current problem is offline quality, not serving reliability

## Related Skills
- [Index Versioning and Reindexing](../index-versioning-and-reindexing/SKILL.md) - Evolve the index safely
- [Qdrant for Production RAG](../../vector-databases/qdrant-for-production-rag/SKILL.md) - Store-side scaling
- [Optimize Retrieval Latency](../../performance-optimization/optimize-retrieval-latency/SKILL.md) - Tune the hot path
- [RAG Evaluation Frameworks](../../evaluation-metrics/rag-evaluation-frameworks/SKILL.md) - Gate deploys on quality

## Metrics & Success Criteria
- **Latency**: P95 stays within budget under expected concurrency
- **Availability**: Component failures degrade gracefully instead of cascading
- **Cache Hit Rate**: Repeated queries avoid redundant compute
- **Rollout Safety**: Bad releases are caught in canary before full traffic
