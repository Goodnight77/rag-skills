---
name: deployment
title: "Deployment"
description: "Route production RAG rollout work across serving, scaling, index versioning, and safe reindexing."
category: "deployment"
tags: ["deployment", "production", "reindexing", "routing"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Deployment

## Overview
Use this parent skill when the RAG system works in development but must be made reliable in production. Route to the child skill that matches whether the problem is serving and scaling the pipeline or evolving the index without downtime.

## Problem Statement
RAG systems that pass local tests still fail in production from cold indexes, unbounded latency under load, and risky full reindexes that take the search layer offline. Prototype code rarely handles versioning, rollout, or drift, so quality quietly decays after launch.

## Key Concepts
- **Serving**: Exposing retrieval and generation behind a scalable, observable service.
- **Index versioning**: Treating the vector index as a versioned, swappable artifact.
- **Zero-downtime reindex**: Rebuilding embeddings without interrupting queries.
- **Drift**: Slow quality decay as data and usage move away from the baseline.

## Implementation Guide

### Step 1: Make the Pipeline a Service
Put retrieval and generation behind an API with health checks, timeouts, and observability before scaling anything.

### Step 2: Version the Index
Treat each index build as a named, immutable artifact so you can roll forward or back by swapping a pointer.

### Step 3: Plan Reindexing and Rollback Up Front
Design embedding-model migrations and reindexing as alias swaps with a fast rollback, not as in-place rebuilds.

## When to Use This Skill
- Moving a working RAG prototype into production
- The system needs to scale, stay observable, and roll back safely
- An embedding-model or schema change requires reindexing live data

## When NOT to Use This Skill
- The system is still a local prototype under active design
- The bottleneck is retrieval or generation quality, not operations
- A managed platform already covers serving, scaling, and reindexing

## Related Skills
- [Production RAG Deployment](production-rag-deployment/SKILL.md)
- [Index Versioning and Reindexing](index-versioning-and-reindexing/SKILL.md)
- [Qdrant for Production RAG](../vector-databases/qdrant-for-production-rag/SKILL.md)
- [Optimize Retrieval Latency](../performance-optimization/optimize-retrieval-latency/SKILL.md)

## Metrics & Success Criteria
- The pipeline is served with health checks, timeouts, and monitoring
- Indexes are versioned and swappable without downtime
- Reindexing and rollback are rehearsed, not improvised
