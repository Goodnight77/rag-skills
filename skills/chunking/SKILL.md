---
name: chunking
title: "Chunking"
description: "Route RAG chunking decisions across semantic, hierarchical, sliding-window, contextual-header, and framework-selection strategies."
category: "chunking"
tags: ["chunking", "routing", "rag", "preprocessing"]
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Chunking

## Overview
Use this parent skill when the main RAG problem is how to split source material into retrievable units. Route to the child skill that best matches the document shape, retrieval failure, and production constraints.

## Problem Statement
Poor chunking causes retrieval misses, fragmented answers, duplicated context, and weak citations. RAG systems need chunking strategies that preserve meaning while staying efficient for indexing and retrieval.

## Key Concepts
- **Semantic boundaries**: Split where ideas naturally change.
- **Hierarchy**: Preserve document, section, and subsection relationships.
- **Overlap**: Add controlled neighboring context across chunk boundaries.
- **Context headers**: Attach inherited titles and metadata to chunks.

## Implementation Guide

### Step 1: Identify the Corpus Shape
Use semantic chunking for prose, hierarchical chunking for structured documents, and code-specific guidance for APIs or source repositories.

### Step 2: Match the Retrieval Failure
Use sliding windows when answers cross boundaries, contextual headers when chunks lack source context, and semantic chunking when fixed windows split ideas.

### Step 3: Validate Chunk Quality
Measure retrieval recall, answer groundedness, duplicate context rate, and citation usefulness before changing embeddings or vector databases.

## When to Use This Skill
- Choosing a chunking strategy for a new RAG pipeline
- Debugging poor recall caused by fragmented source content
- Improving citations and source traceability

## When NOT to Use This Skill
- The bottleneck is ranking after retrieval
- The issue is vector database operations or deployment
- Source documents are already chunked and validated

## Related Skills
- [Semantic Chunking](semantic-chunking/SKILL.md)
- [Hierarchical Chunking](hierarchical-chunking/SKILL.md)
- [Sliding Window Chunking](sliding-window-chunking/SKILL.md)
- [Contextual Chunk Headers](contextual-chunk-headers/SKILL.md)
- [Choosing a Chunking Framework](choosing-a-chunking-framework/SKILL.md)

## Metrics & Success Criteria
- Higher recall on chunk-boundary questions
- Lower duplicate or irrelevant context in prompts
- Better source citations and more coherent retrieved passages
