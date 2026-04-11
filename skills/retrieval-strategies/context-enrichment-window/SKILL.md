---
name: context-enrichment-window
title: "Context Enrichment Window"
description: "Add surrounding chunks to retrieved results to provide more coherent and complete context."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["context-enrichment", "surrounding-context", "window", "coherence"]
---

## Overview
Context enrichment window expands retrieved chunks by including neighboring text from the original document. This provides more coherent and contextually rich results, mitigating the tendency of vector search to return isolated text fragments.

## Problem Statement
Vector-based retrieval often returns isolated fragments:
- **Mid-Sentence Cuts**: Chunks may start or end in the middle of thoughts
- **Missing Context**: Relevant information may be in adjacent chunks
- **Incoherence**: Isolated fragments lack narrative flow
- **Incomplete Information**: Critical context for understanding may be missing
- **Fragmented Answers**: LLMs struggle to generate coherent responses from disjointed pieces

## Key Concepts
- **Surrounding Context**: Text immediately before and after a retrieved chunk
- **Window Size**: Number of chunks to include on each side
- **Chunk Indexing**: Maintaining original document order and positions
- **Context Expansion**: Appending surrounding chunks to retrieved results
- **Overlap Handling**: Managing overlapping regions between consecutive chunks

## Implementation Guide

### Step 1: Implement Chunk Indexing
Store chunk indices and document positions during the indexing phase.

**Why**: To retrieve surrounding chunks, you need to know where each chunk sits in the original document. Indexing maintains this positional information.

Assign a sequential index to each chunk during the chunking process and store the index as metadata.

### Step 2: Store Chunks with Positional Metadata
Include chunk indices and position information in the vector database.

**Why**: Vector databases need to store positional metadata alongside content to enable context enrichment after retrieval.

Add index, start position, and end position as metadata fields for each chunk in your vector database.

### Step 3: Implement Context Window Retrieval
For each retrieved chunk, fetch surrounding chunks by index.

**Why**: Adding surrounding context provides the narrative flow and information needed to understand the retrieved fragment properly.

Retrieve chunks at indices ±N around each retrieved chunk, where N is the window size.

### Step 4: Implement Overlap Handling
Properly combine overlapping chunks without duplication.

**Why**: Chunk overlap means surrounding chunks share text with the target chunk. Proper combination avoids duplication and maintains coherence.

When concatenating chunks, account for overlap by including each character only once.

### Step 5: Implement Adaptive Window Sizing
Adjust window size based on chunk characteristics.

**Why**: Not all chunks need the same context size. Adaptive sizing balances completeness with efficiency.

Use larger windows for shorter chunks and smaller windows for longer chunks.

### Step 6: Build Complete Context Enrichment Pipeline
Combine all components into a cohesive retrieval system.

**Why**: A complete pipeline with configurable parameters allows for optimization and experimentation with different window strategies.

For implementation patterns, see [LlamaIndex SentenceWindowNodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/), [LangChain ContextualCompressionRetriever](https://reference.langchain.com/python/langchain-classic/retrievers/contextual_compression/ContextualCompressionRetriever), and the [RecursiveCharacterTextSplitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter) for chunking strategies.

## When to Use This Skill
- Building RAG systems where narrative coherence matters
- When documents have natural flow or story structure
- For Q&A systems that need complete context for answers
- When retrieved chunks are frequently mid-sentence or mid-thought
- For domains where understanding depends on surrounding information

## When NOT to Use This Skill
- For collections where chunks are already self-contained (FAQ entries)
- When using extremely large windows that negate chunking benefits
- For systems where retrieval must be as fast as possible (enrichment adds overhead)
- When chunk overlap is already very large (50%+)
- For keyword-only retrieval where position doesn't matter

## Related Skills
- [Semantic Chunking](../../chunking/semantic-chunking/SKILL.md) - Better initial chunking
- [Hierarchical Chunking](../../chunking/hierarchical-chunking/SKILL.md) - Structure-based approach
- [Sliding Window Chunking](../../chunking/sliding-window-chunking/SKILL.md) - Overlap-based chunking

## Metrics & Success Criteria
- **Context Coherence**: Retrieved content represents complete, self-contained information
- **Answer Quality**: Improved coherence in generated responses
- **Coverage**: No significant information lost in chunk boundaries
- **Token Efficiency**: Enriched chunks balanced between too small and too large
- **Latency**: Acceptable overhead for enrichment (typically < 100ms)
