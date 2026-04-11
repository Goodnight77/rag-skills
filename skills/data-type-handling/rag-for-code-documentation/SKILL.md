---
name: rag-for-code-documentation
title: "RAG for Code Documentation"
description: "Handle code-aware retrieval by preserving symbols, file structure, and API context."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "data-type-handling"
tags: ["code", "programming", "syntax", "api", "documentation"]
---

## Overview
RAG for code documentation requires specialized handling due to code's structured nature, syntax-specific patterns, and the importance of preserving function signatures, imports, and contextual relationships. This skill covers embedding code snippets, handling API references, and retrieving code-aware context.

## Problem Statement
Generic RAG approaches struggle with code-related queries:
- Standard chunking breaks function/class structures mid-signature
- Language models don't understand code syntax and semantics as well as natural language
- Code requires preserving structural relationships (imports, dependencies, inheritance)
- API queries need exact matches alongside semantic understanding
- Code examples need context to be useful (imports, dependencies)

## Key Concepts
- **Code-Aware Chunking**: Preserving function/class boundaries and syntactic units
- **Code-Specific Embeddings**: Models trained on code (CodeBERT, StarCoder) vs. general embeddings
- **Syntax Preservation**: Maintaining formatting, indentation, and structure
- **Context Tracking**: Following import chains and dependency relationships
- **Hybrid Search for Code**: Combining semantic search with AST-based matching

## Implementation Guide

### Step 1: Code-Aware Document Parsing
Parse code files into structured chunks that preserve syntactic units.

**Why**: AST-based parsing preserves code structure that would be lost with generic text chunking.

### Step 2: Code-Specific Embedding
Use embeddings designed for code or augment text embeddings with code-aware features.

**Why**: Code-specific embeddings capture semantic meaning in code (function relationships, patterns) that general embeddings miss.

### Step 2.5: Store Code Chunks in Vector DB
Store code chunks with rich metadata for effective retrieval.

**Why**: Rich metadata enables filtering by language, type, file path, and other code-specific attributes.

### Step 3: Implement Code-Aware Search
Search with code-specific considerations.

**Why**: Code-aware search combines semantic understanding with precise filtering for programming-specific use cases.

### Step 4: Handle API Documentation
Specialized handling for API reference queries.

**Why**: API queries often require exact matching (function/class names) rather than pure semantic search.

Practical references include the [CodeBERT paper](https://huggingface.co/papers/2002.08155), [GraphCodeBERT paper](https://huggingface.co/papers/2009.08366), [StarCoder paper](https://huggingface.co/papers/2305.06161), and [GitHub code search](https://github.com/features/code-search).

## When to Use This Skill
- Building code search or documentation assistants
- When users query code syntax, APIs, or programming concepts
- For IDE integrations and code completion systems
- When building technical documentation with code examples
- For troubleshooting programming queries

## When NOT to Use This Skill
- For natural language-only content (use general RAG)
- When code structure isn't important for retrieval
- For very simple codebases where grep suffices
- When embedding code-specific models is not feasible

## Related Skills
- [Semantic Chunking](../../chunking/semantic-chunking/SKILL.md) - For document chunks
- [Choosing Vector DB by Datatype](../../vector-databases/choosing-vector-db-by-datatype/SKILL.md) - Database selection
- [Hierarchical Chunking](../../chunking/hierarchical-chunking/SKILL.md) - For nested code structures

## Metrics & Success Criteria
- **Code Retrieval Accuracy**: Exact matches for function/class names > 90%
- **Semantic Understanding**: NDCG@10 for code-related queries > 0.7
- **Context Preservation**: Relevant imports included > 80% of time
- **Syntax Preservation**: Code formatting maintained 100%
- **Query Latency**: < 200ms for typical code queries
