---
title: "Semantic Chunking"
description: "Use semantic boundaries and embedding similarity to chunk text for higher-relevance retrieval."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "chunking"
tags: ["semantic", "nlp", "sentence-boundary", "context-preservation"]
---

## Overview
Semantic chunking divides documents into segments based on natural language boundaries and semantic meaning rather than fixed character counts. This approach preserves context integrity and improves retrieval relevance by keeping related ideas together.

## Problem Statement
Fixed-size chunking (e.g., 1000 tokens) often cuts through mid-sentence, mid-paragraph, or mid-concept, resulting in:
- Fragments that lose semantic meaning
- Context bleeding across unrelated chunks
- Poor retrieval relevance for semantic search
- Difficulty for LLMs to understand isolated fragments

## Key Concepts
- **Semantic Boundaries**: Natural break points in text (paragraphs, sections, sentences)
- **Context Preservation**: Keeping related ideas and arguments together
- **Sentence Boundary Detection**: Using NLP tools to identify proper sentence ends
- **Paragraph Cohesion**: Identifying when a new thought or argument begins
- **Overlapping Windows**: Small overlaps to preserve context between adjacent chunks

## Implementation Guide

### Step 1: Detect Sentence Boundaries
Use sentence boundary detection rather than simple period splitting. This handles abbreviations, decimal numbers, and other edge cases.

**Why**: Simple period/regex splitting fails on "Dr. Smith", "3.14", "U.S.A.", etc.

### Step 2: Group Sentences into Semantic Units
Group sentences into chunks based on semantic cohesion rather than fixed counts.

**Why**: Similarity-based chunking adapts to document density—dense technical sections get smaller chunks, narrative sections get larger ones.

### Step 3: Apply Structure-Based Chunking
Leverage document structure (headings, markdown, HTML tags) to identify natural sections.

**Why**: Document structure often encodes semantic boundaries (chapters, sections, subsections).

### Step 4: Implement Adaptive Sizing
Adjust chunk sizes based on content characteristics (code blocks, lists, tables).

**Why**: Different content types need different chunking strategies for optimal retrieval.

For practical implementations, compare [Sentence-BERT](https://arxiv.org/abs/1908.10084), [LlamaIndex semantic chunking](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/), [LangChain RecursiveCharacterTextSplitter](https://api.python.langchain.com/en/latest/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html), and [spaCy sentence segmentation](https://spacy.io/usage/linguistic-features#sentence-segmentation).

## When to Use This Skill
- Documents with clear semantic structure (articles, reports, documentation)
- When retrieval quality is more important than fixed-size guarantees
- For narrative or explanatory content where context matters
- When using semantic search (vector embeddings) for retrieval
- For Q&A systems that need coherent context for answers

## When NOT to Use This Skill
- Code repositories where line-level precision matters
- Log files or structured data with fixed formats
- When you need exact token count guarantees (e.g., for API limits)
- Streaming data where chunk boundaries can't be deferred
- When using exact keyword matching (BM25) where chunk size matters less

## Related Skills
- [Hierarchical Chunking](./hierarchical-chunking.md) - For nested document structures
- [Sliding Window Chunking](./sliding-window-chunking.md) - For overlapping context preservation
- [Hybrid Search BM25 Dense](../retrieval-strategies/hybrid-search-bm25-dense.md) - Combining search methods

## Metrics & Success Criteria
- **Retrieval Relevance**: Retrieved chunks should contain complete, self-contained information
- **Context Preservation**: Related concepts remain in same chunk
- **Coverage**: No significant information lost in chunk boundaries
- **Token Efficiency**: Chunks balanced between too small (lossy) and too large (noisy)
- **Semantic Coherence**: Chunks represent coherent thoughts or sections
