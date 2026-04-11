---
name: vector-databases
title: "Vector Databases"
description: "Route RAG vector database decisions across Qdrant setup, production operations, and datastore selection by data type."
category: "vector-databases"
tags: ["vector-database", "qdrant", "metadata", "rag"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Vector Databases

## Overview
Use this parent skill when the main RAG problem is choosing, configuring, or operating the vector storage layer. Route to the child skill that matches setup, production, or datastore-selection needs.

## Problem Statement
Vector database mistakes often show up as slow queries, weak filtering, poor metadata modeling, or expensive production operations. RAG systems need a storage layer that matches the data type, scale, and query pattern.

## Key Concepts
- **Collections and indexes**: Store vectors and tune search behavior.
- **Payload metadata**: Filter and route retrieval using structured fields.
- **Hybrid needs**: Combine vectors with keyword or structured search when needed.
- **Production operations**: Plan backups, monitoring, scaling, and migrations.

## Implementation Guide

### Step 1: Identify the Data Type
Separate text, code, multimodal, and metadata-heavy retrieval requirements.

### Step 2: Design Storage and Filtering
Choose collection layout, vector fields, payload indexes, and metadata conventions.

### Step 3: Plan Production Behavior
Validate latency, backup strategy, migration path, monitoring, and failure recovery.

## When to Use This Skill
- Choosing a vector database for a RAG system
- Setting up Qdrant for filtered semantic search
- Preparing Qdrant or another vector store for production

## When NOT to Use This Skill
- The main issue is chunking or document parsing
- The main issue is prompt construction
- The vector database is already chosen and the problem is reranking quality

## Related Skills
- [Qdrant Setup for RAG](qdrant-setup-rag/SKILL.md)
- [Qdrant for Production RAG](qdrant-for-production-rag/SKILL.md)
- [Choosing Vector DB by Datatype](choosing-vector-db-by-datatype/SKILL.md)

## Metrics & Success Criteria
- Correct metadata filters for target queries
- Stable latency at expected corpus size
- Clear backup, migration, and monitoring plan
