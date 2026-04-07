---
title: "HyDE - Hypothetical Document Embeddings"
description: "Use LLM-generated hypothetical documents to bridge the query-document gap and improve retrieval relevance."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["hyde", "query-expansion", "llm-generation", "semantic-gap"]
---

## Overview
HyDE (Hypothetical Document Embeddings) is a query expansion technique that generates a hypothetical document answering the user's query, then uses this synthetic document as the query for vector search. This bridges the semantic gap between short queries and longer, more detailed document representations.

## Problem Statement
Traditional RAG systems face a fundamental mismatch:
- **Query Style**: User queries are short, informal, and question-oriented
- **Document Style**: Indexed documents are long, formal, and answer-oriented
- **Embedding Space Gap**: These different styles occupy different regions in embedding space
- **Direct Matching Failure**: Query-document direct similarity often produces poor matches

## Key Concepts
- **Hypothetical Document**: An LLM-generated synthetic document that answers the query
- **Query-Document Style Gap**: The difference between query and document writing styles
- **Embedding Similarity**: Matching generated answer to actual answers in the corpus
- **Answer-Answer Matching**: Transforming the problem from query-document to answer-answer matching
- **Document-Aware Generation**: Hypothetical documents sized to match typical chunk lengths

## Implementation Guide

### Step 1: Implement Hypothetical Document Generation
Use an LLM to generate a detailed document answering the user's query.

**Why**: The generated hypothetical document shares characteristics (length, style, content structure) with actual documents in your corpus, enabling better similarity matching in embedding space.

Direct the LLM to create a comprehensive answer that matches the typical length and style of documents in your collection.

### Step 2: Configure Document-Aware Generation
Match the hypothetical document size to your average chunk size.

**Why**: Documents of similar length will have more comparable embedding representations. Mismatched lengths can create distance artifacts unrelated to semantic meaning.

Target a specific character count or token count that matches your chunking strategy (typically 400-1000 characters).

### Step 3: Perform Vector Search with Hypothetical Document
Use the generated document as the query for similarity search instead of the original query.

**Why**: The hypothetical document is in the same style and semantic space as your indexed documents, allowing the vector database to find semantically similar content more effectively.

Replace the original query with the generated hypothetical document when performing vector similarity search.

### Step 4: Implement Result Filtering
Filter retrieved documents for actual relevance to the original query.

**Why**: While HyDE improves retrieval, some results may be semantically similar but factually irrelevant. Relevance filtering ensures quality.

Evaluate retrieved documents against the original query (not the hypothetical one) to filter out irrelevant matches.

### Step 5: Build Complete HyDE Pipeline
Combine generation, retrieval, and filtering into a cohesive system.

**Why**: A complete pipeline with timing and explanation allows optimization, debugging, and production deployment.

For implementation patterns, see the [HyDE paper](https://arxiv.org/abs/2212.10596), [LlamaIndex HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/), and [LangChain HyDE reference](https://reference.langchain.com/python/langchain-classic/chains/hyde).

## When to Use This Skill
- Building RAG systems where queries are short and documents are long
- When query-document style mismatch causes poor retrieval
- For domains where questions and answers have different linguistic patterns
- When using semantic search with vector embeddings
- When traditional query expansion with synonyms doesn't suffice

## When NOT to Use This Skill
- When queries and documents already have similar styles (e.g., FAQ systems)
- For extremely latency-sensitive applications (adds LLM call per query)
- When using keyword-based retrieval (BM25) that doesn't benefit from style alignment
- When the cost of LLM generation outweighs relevance improvements
- For very small document collections where direct matching works well

## Related Skills
- [HyPE](./hype-hypothetical-prompt-embeddings.md) - Precomputed alternative
- [Query Transformation Strategies](./query-transformation-strategies.md) - Other expansion methods
- [Multi-Pass Retrieval with Reranking](./multi-pass-retrieval-with-reranking.md) - Post-retrieval refinement

## Metrics & Success Criteria
- **Retrieval Relevance**: NDCG@10 improvement > 15% over baseline
- **Style Alignment**: Hypothetical documents match corpus style characteristics
- **Latency**: End-to-end latency < 1s for typical queries
- **Cost**: LLM generation cost balanced against relevance gains
- **Answer Quality**: Final answers show improved factual accuracy
