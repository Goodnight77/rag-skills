---
name: contextual-chunk-headers
title: "Contextual Chunk Headers"
description: "Add higher-level context to chunks by prepending headers before embedding for better retrieval."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "chunking"
tags: ["contextual-headers", "metadata", "chunk-enhancement", "document-structure"]
---

## Overview
Contextual chunk headers (CCH) enhance retrieval by prepending higher-level context (document title, section headers, summaries) to each chunk before embedding. This gives embeddings a more accurate representation of content and meaning, significantly improving retrieval quality and reducing irrelevant results.

## Problem Statement
Individual chunks often lack sufficient context:
- **Implicit References**: Chunks use pronouns and implicit references that aren't clear in isolation
- **Missing Context**: Chunks only make sense in the context of their section or document
- **Misleading Isolation**: Read alone, chunks can be misleading or incomplete
- **Poor Retrieval**: Queries that reference subjects or themes aren't matched effectively
- **LLM Misinterpretation**: LLMs struggle to understand decontextualized chunks

## Key Concepts
- **Chunk Header**: Higher-level context prepended to chunk content
- **Document-Level Context**: Document title or summary as header context
- **Section-Level Context**: Hierarchy of section and subsection titles
- **Pre-Embedding Concatenation**: Combining header and chunk before embedding
- **Context Preservation**: Carrying headers through to retrieval and presentation

## Implementation Guide

### Step 1: Generate Document-Level Context
Extract or generate document titles and summaries for use in chunk headers.

**Why**: Document-level context provides the most important higher-level information for understanding any chunk within that document.

Use an LLM to generate a descriptive document title if one doesn't exist, or extract titles from document structure.

### Step 2: Extract Section Hierarchy
Parse document structure to capture section and subsection titles.

**Why**: Section hierarchy provides granular context that helps retrieve information about specific topics and themes within the document.

Parse the document structure (markdown headings, HTML tags, etc.) to build a hierarchical representation of sections.

### Step 3: Create Chunk Headers
Combine document and section context into comprehensive headers.

**Why**: Combined context provides both broad document understanding and specific section information, giving embeddings the best possible representation.

For each chunk, create a header combining document title and the section path that contains the chunk.

### Step 4: Prepend Headers to Chunks
Combine headers with chunk content before embedding.

**Why**: Embeddings represent the combined header+chunk content, capturing both local meaning and global context in the same vector space.

When indexing each chunk, include the header as a prefix to the chunk content.

### Step 5: Embed with Headers
Use the header-enhanced chunks for embedding and indexing.

**Why**: Embedding with headers ensures that retrieval considers both local content and broader context, leading to more relevant matches.

Index the enhanced chunks using your preferred embedding model and vector database.

### Step 6: Present Results with Headers
Include headers when presenting retrieved chunks to users or LLMs.

**Why**: Presenting headers provides necessary context for understanding retrieved chunks, reducing misinterpretation and improving answer quality.

When returning retrieved content, include the original header for context.

### Step 7: Build Complete CCH Pipeline
Combine all components into a cohesive chunking and retrieval system.

**Why**: A complete pipeline ensures that contextual headers are consistently applied through chunking, embedding, retrieval, and presentation.

For implementation patterns, see [LangChain RecursiveCharacterTextSplitter](https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter), [LlamaIndex node parser usage](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/), [Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval), and [dsRAG AutoContext](https://github.com/D-Star-AI/dsRAG).

## When to Use This Skill
- Building RAG systems with structured documents (articles, reports, documentation)
- When chunks frequently refer to their subject via pronouns or implicit references
- For documents with clear section hierarchy or structure
- When retrieval quality suffers from decontextualized chunks
- For applications where LLMs need to understand chunk context

## When NOT to Use This Skill
- For unstructured documents without clear hierarchy or titles
- When chunk headers would be redundant or too long
- For very short documents where the entire text is already coherent
- When storage overhead is a major concern (headers increase chunk size)
- For domains where document structure is meaningless (code snippets, logs)

## Related Skills
- [Semantic Chunking](../semantic-chunking/SKILL.md) - Context-aware chunking approach
- [Hierarchical Chunking](../hierarchical-chunking/SKILL.md) - Structure-based chunking
- [Context Enrichment Window](../../retrieval-strategies/context-enrichment-window/SKILL.md) - Post-retrieval context

## Metrics & Success Criteria
- **Retrieval Precision**: Increased rate of correct retrieval for subject-based queries
- **Context Completeness**: Retrieved chunks provide sufficient context for understanding
- **Header Effectiveness**: Headers improve embedding representation quality
- **Answer Quality**: Reduced hallucinations from decontextualized chunks
- **Storage Overhead**: Acceptable increase in chunk size due to headers
