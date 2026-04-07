---
title: "Sliding Window Chunking"
description: "Use overlapping windows to preserve context across chunk boundaries while controlling retrieval size."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "chunking"
tags: ["overlap", "context-preservation", "window", "boundary"]
---

## Overview
Sliding window chunking creates overlapping chunks where each chunk shares content with adjacent chunks. This preserves context at chunk boundaries, ensuring that information split across chunks remains accessible through multiple retrieval paths.

## Problem Statement
Non-overlapping chunking creates hard boundaries that can break important context:
- Critical information appears exactly at a chunk boundary
- Concepts spanning multiple chunks become fragmented
- Retrieval may miss relevant content because it's split across boundaries
- LLMs lose context when only one fragment is provided

## Key Concepts
- **Overlap Percentage**: The proportion of shared content between adjacent chunks (typically 10-25%)
- **Window Size**: The total size of each chunk including overlap
- **Stride**: The distance between chunk start points (window size - overlap)
- **Context Preservation**: Ensuring relevant context exists on both sides of boundaries
- **Multiple Retrieval Paths**: Same content accessible from different chunks

## Implementation Guide

### Step 1: Determine Overlap Parameters
Calculate appropriate overlap based on your use case and chunk size.

**Why**: The overlap ratio determines how much context is preserved—too little loses context, too much creates redundancy.

### Step 2: Implement Sliding Window Chunking
Create chunks with configurable overlap.

**Why**: Boundary adjustment prevents chunks from ending mid-sentence while maintaining the sliding window pattern.

### Step 3: Add Chunk Metadata
Track overlap information for retrieval-time decisions.

**Why**: Metadata allows retrieval systems to identify and deduplicate overlapping content.

### Step 4: Implement Smart Retrieval
Handle overlapping results intelligently.

**Why**: Smart retrieval prevents redundant information while preserving the benefits of overlapping chunks.

### Step 5: Token-Aware Sliding Window
Implement sliding window based on tokens rather than characters.

**Why**: Token-aware chunking is more accurate for LLMs and respects their actual token limits.

Useful implementations include [LangChain RecursiveCharacterTextSplitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter), the [OpenAI tiktoken cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb), [tiktoken](https://github.com/openai/tiktoken), and [Sentence Transformers rerankers](https://www.sbert.net/examples/cross_encoder/training/rerankers/README.html).

## When to Use This Skill
- Documents where context at boundaries is important
- When using semantic search where retrieval might match content near boundaries
- For narrative or sequential content where flow matters
- When building systems that benefit from multiple retrieval paths
- For technical documentation where definitions/examples might span chunks

## When NOT to Use This Skill
- When storage costs are critical (overlap increases storage 20-30%)
- When exact deduplication is required (overlap makes this harder)
- For structured data with clear boundaries (JSON, CSV)
- When using exact keyword search where overlap doesn't help

## Related Skills
- [Semantic Chunking](./semantic-chunking.md) - For content-aware boundaries
- [Hierarchical Chunking](./hierarchical-chunking.md) - For nested structures
- [Hybrid Search BM25 Dense](../retrieval-strategies/hybrid-search-bm25-dense.md) - For combining search methods

## Metrics & Success Criteria
- **Boundary Coverage**: Critical terms appear in at least one chunk (not lost at boundaries)
- **Storage Overhead**: Overlap increases storage by expected ratio (e.g., 20%)
- **Retrieval Recall**: Same content accessible through multiple chunks
- **Context Preservation**: Retrieved chunks contain sufficient surrounding context
- **Deduplication Quality**: Can identify and handle overlapping content effectively
