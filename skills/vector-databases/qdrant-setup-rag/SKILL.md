---
name: qdrant-setup-rag
title: "Qdrant Setup for RAG"
description: "Set up Qdrant for RAG with collections, payload filtering, and batch ingestion."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "vector-databases"
tags: ["qdrant", "setup", "ingestion", "filtering"]
---

## Overview
Qdrant is an open-source vector similarity search engine designed for high-performance RAG applications. This skill covers setting up Qdrant, creating collections with proper indexing, implementing filtering with metadata, and managing document ingestion.

## Problem Statement
Setting up a vector database for RAG involves multiple considerations:
- Choosing the right distance metric for your embedding model
- Configuring optimal index parameters for performance vs. recall
- Structuring metadata for effective filtering
- Handling batch ingestion efficiently
- Managing collection schema changes

## Key Concepts
- **Distance Metric**: Cosine similarity, dot product, or Euclidean distance for vector comparisons
- **Index Type**: HNSW (Hierarchical Navigable Small World) for approximate nearest neighbors
- **Payload Filtering**: Querying vectors based on associated metadata
- **Collection Schema**: Defining vector dimensions and payload structure
- **Batch Operations**: Efficient bulk insertion of vectors

## Implementation Guide

### Step 1: Install and Initialize Qdrant
Set up Qdrant locally or connect to a cloud instance.

**Why**: Docker provides an isolated environment with persistence, while the cloud option offers managed scalability.

### Step 2: Create a Collection
Configure collection parameters based on your embedding model and use case.

**Why**: Proper configuration at creation time avoids expensive re-indexing later. COSINE is default for normalized embeddings.

### Step 3: Design Metadata Schema
Structure your payloads (metadata) for effective filtering.

**Why**: Well-structured metadata enables powerful filtering queries and helps organize retrieval results.

### Step 4: Ingest Documents
Upload documents with their embeddings and metadata.

**Why**: Batch operations significantly improve ingestion performance compared to individual uploads.

### Step 5: Implement Filtering Queries
Query with metadata filters for targeted retrieval.

**Why**: Filtering enables domain-specific retrieval (e.g., "search only in documentation" or "search only code examples").

### Step 6: Monitor and Maintain
Set up monitoring for collection health.

**Why**: Monitoring helps identify performance issues and scaling needs before they impact users.

See the [Qdrant documentation](https://qdrant.tech/documentation/), [Qdrant filtering](https://qdrant.tech/documentation/concepts/filtering/), [Qdrant Python client](https://github.com/qdrant/qdrant-client), and the [HNSW paper](https://arxiv.org/abs/1603.09320) for production-ready setup patterns.

## When to Use This Skill
- Building a new RAG application from scratch
- Setting up a local vector database for development
- Migrating from another vector database to Qdrant
- When you need open-source with no vendor lock-in

## When NOT to Use This Skill
- When you need managed, zero-ops solution (consider Qdrant Cloud)
- For very small datasets (< 1000 vectors) where a simple list might suffice
- When you need specialized features like multi-vector indexing (consider other DBs)

## Related Skills
- [Qdrant for Production RAG](../qdrant-for-production-rag/SKILL.md) - Scaling for production
- [Choosing Vector DB by Datatype](../choosing-vector-db-by-datatype/SKILL.md) - Database selection guide
- [Optimize Retrieval Latency](../../performance-optimization/optimize-retrieval-latency/SKILL.md) - Performance tuning

## Metrics & Success Criteria
- **Setup Time**: < 10 minutes to get a working collection
- **Ingestion Speed**: > 10,000 vectors/minute on modest hardware
- **Query Latency**: < 50ms for queries on 1M vectors
- **Indexing**: Automatic HNSW indexing within reasonable time
- **Recall**: > 0.95 for 10 nearest neighbors
