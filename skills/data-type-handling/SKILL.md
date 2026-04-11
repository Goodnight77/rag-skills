---
name: data-type-handling
title: "Data Type Handling"
description: "Route RAG handling for code documentation, APIs, images, tables, diagrams, and multimodal content."
category: "data-type-handling"
tags: ["data-types", "code", "multimodal", "rag"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Data Type Handling

## Overview
Use this parent skill when source material is not plain prose or when different data types need different parsing, metadata, chunking, and retrieval strategies.

## Problem Statement
Code, APIs, tables, images, diagrams, and mixed media lose important meaning when treated as generic text. RAG systems need data-specific handling to preserve symbols, structure, and visual context.

## Key Concepts
- **Code structure**: Preserve symbols, paths, APIs, and examples.
- **Multimodal extraction**: Convert images, diagrams, and tables into retrievable representations.
- **Metadata alignment**: Keep source references consistent across modalities.
- **Specialized retrieval**: Match query type to the right content representation.

## Implementation Guide

### Step 1: Classify Source Content
Identify whether the corpus is code-heavy, image-heavy, table-heavy, or mixed.

### Step 2: Preserve Native Structure
Use parsers and metadata that retain symbols, captions, headers, page numbers, and source locations.

### Step 3: Choose Retrieval Representations
Index text, summaries, captions, code symbols, table schemas, or multimodal embeddings as appropriate.

## When to Use This Skill
- Building RAG for technical documentation or code repositories
- Indexing PDFs, diagrams, screenshots, or tables
- Combining text and non-text evidence in answers

## When NOT to Use This Skill
- The corpus is simple prose
- The main issue is vector database operations
- The main issue is production latency

## Related Skills
- [RAG for Code Documentation](rag-for-code-documentation/SKILL.md)
- [RAG for Multimodal Content](rag-for-multimodal-content/SKILL.md)

## Metrics & Success Criteria
- Accurate retrieval of symbols, captions, tables, and source references
- Lower hallucination on code or visual questions
- Clear traceability back to original artifacts
