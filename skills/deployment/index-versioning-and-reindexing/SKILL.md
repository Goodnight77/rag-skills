---
name: index-versioning-and-reindexing
title: "Index Versioning and Reindexing"
description: "Version the vector index and reindex or migrate embeddings without downtime or quality regressions."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "deployment"
tags: ["reindexing", "versioning", "embedding-migration", "blue-green"]
---

## Overview
This skill covers evolving the index behind a live RAG system: rebuilding embeddings after a model or chunking change, migrating between embedding models, and versioning indexes so changes are reversible and queries never go dark.

## Problem Statement
The index is not static. Embedding models improve, chunking strategies change, and documents update. Reindexing in place takes search offline and, if the new build is worse, there is no way back. Mixing vectors from two embedding models silently corrupts similarity scores.

## Key Concepts
- **Immutable index version**: Each build is a named artifact, never edited in place.
- **Alias or pointer swap**: Traffic moves between versions by flipping one pointer.
- **Embedding migration**: Switching models requires re-embedding all vectors, not mixing.
- **Blue-green reindex**: Build the new index alongside the old, then cut over.

## Implementation Guide

### Step 1: Build the New Index Alongside the Old
Create the new version as a separate collection or index while the current one keeps serving traffic.

**Why**: Building beside the live index means queries never hit a half-built or empty collection.

### Step 2: Validate Before Cutover
Run the evaluation golden set against the new index and compare scores to the current baseline before switching.

**Why**: Comparing against a baseline catches a regression before it reaches users instead of after.

### Step 3: Swap by Alias and Keep Rollback Ready
Cut over by repointing an alias to the new version and retain the previous version until the new one is proven.

**Why**: An alias swap makes both cutover and rollback near-instant and low-risk.

Never serve queries from a mix of two embedding models: re-embed the whole corpus when the model changes. See the [Qdrant aliases guide](https://qdrant.tech/documentation/concepts/collections/#collection-aliases) and [Qdrant snapshots](https://qdrant.tech/documentation/concepts/snapshots/).

## When to Use This Skill
- Changing the embedding model, chunking strategy, or index schema in production
- Documents update often and the index must stay fresh
- You need reversible, zero-downtime index changes

## When NOT to Use This Skill
- The corpus is static and never re-embedded
- A managed service handles reindexing and versioning for you
- The system is a prototype where downtime is acceptable

## Related Skills
- [Production RAG Deployment](../production-rag-deployment/SKILL.md) - Serve the versioned index
- [Qdrant for Production RAG](../../vector-databases/qdrant-for-production-rag/SKILL.md) - Collection and alias operations
- [Retrieval Evaluation Metrics](../../evaluation-metrics/retrieval-evaluation-metrics/SKILL.md) - Validate before cutover
- [Choosing Vector DB by Datatype](../../vector-databases/choosing-vector-db-by-datatype/SKILL.md) - Store selection

## Metrics & Success Criteria
- **Zero Downtime**: Queries keep serving throughout reindexing
- **Reversibility**: Rollback to the prior version is fast and tested
- **No Model Mixing**: All live vectors come from a single embedding model
- **Validated Cutover**: New index meets or beats the baseline before swap
