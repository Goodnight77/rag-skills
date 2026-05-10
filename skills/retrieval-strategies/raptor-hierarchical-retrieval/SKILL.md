---
name: raptor-hierarchical-retrieval
title: "RAPTOR - Hierarchical Abstractive Retrieval"
description: "Use hierarchical clustering and summarization to create multi-level document trees for improved retrieval."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["raptor", "hierarchical", "clustering", "summarization", "tree-structure"]
---

## Overview
RAPTOR (Recursive Abstractive Processing and Tree-Organized Retrieval) creates a hierarchical tree of document summaries, allowing retrieval at multiple levels of abstraction. This approach balances broad overviews with specific details, enabling more nuanced information retrieval from large document collections.

## Problem Statement
Large document collections present retrieval challenges:
- **Granularity Mismatch**: Queries may need broad context or specific details, but single-level retrieval can't adapt
- **Information Overload**: Retrieving from all documents returns too much content
- **Coherence Loss**: Retrieved fragments lack connection to broader themes
- **Scalability Issues**: Linear search becomes inefficient with growing collections
- **Context Gaps**: Missing connections between related concepts across documents

## Key Concepts
- **Tree Building**: Creating hierarchical summaries through clustering and abstraction
- **Level-wise Abstraction**: Each level represents increasingly condensed information
- **Cluster Summarization**: Grouping similar documents and creating summaries
- **Multi-level Retrieval**: Querying across multiple abstraction levels
- **Parent-Child Links**: Maintaining connections between summaries and source documents

## Implementation Guide

### Step 1: Document Embedding and Clustering
Embed all documents and cluster them by semantic similarity.

**Why**: Clustering groups related documents together, enabling summary creation that captures themes across multiple documents rather than individual pieces.

Use your preferred embedding model to create vector representations, then apply clustering algorithms (e.g., Gaussian Mixture Models, k-means).

### Step 2: Cluster Summarization
Generate summaries for each cluster of documents.

**Why**: Summaries capture the key information from multiple documents, creating a higher-level abstraction that preserves important themes while reducing volume.

For each cluster, concatenate the documents and use an LLM to generate a concise summary.

### Step 3: Build Tree Hierarchically
Recursively apply embedding, clustering, and summarization to build multiple levels.

**Why**: Multiple levels of abstraction allow the system to retrieve at appropriate granularity - broad context from high levels, specific details from low levels.

Apply the same process to the summaries created in the previous level, building up the tree until reaching a single root summary or maximum levels.

### Step 4: Build Multi-Level Vector Index
Index all documents and summaries at all levels.

**Why**: A unified vector index allows efficient similarity search across all abstraction levels, enabling the retriever to select the most appropriate level for each query.

Embed and index all content from all tree levels with metadata indicating the level and origin.

### Step 5: Implement Multi-Level Retrieval
Query across all levels and combine results intelligently.

**Why**: Multi-level retrieval ensures both broad context and specific details are considered. Combining results from different levels provides comprehensive information.

Retrieve from multiple levels and balance the results to ensure both breadth and depth in the retrieved information.

### Step 6: Implement Contextual Compression
Extract only relevant parts from retrieved content.

**Why**: High-level summaries may contain more information than needed for a specific query. Contextual compression focuses on the most relevant portions.

Use an LLM or compression technique to extract the most relevant portions of retrieved content for the specific query.

### Step 7: Build Complete RAPTOR Pipeline
Combine all components into a cohesive system.

**Why**: A complete pipeline with timing and explanation allows optimization, debugging, and production deployment.

For implementation patterns, see the [RAPTOR paper](https://arxiv.org/abs/2401.18059), [LlamaIndex RAPTOR pack](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/), and [scikit-learn clustering documentation](https://scikit-learn.org/stable/modules/clustering.html).

## When to Use This Skill
- Building RAG systems with large document collections (100+ documents)
- When queries vary from broad overviews to specific details
- For domains where thematic organization is important (academic papers, research)
- When you need to maintain both specificity and breadth in retrieval
- For applications requiring traceability from summaries to source documents

## When NOT to Use This Skill
- For small document collections where single-level search is sufficient
- When document updates are frequent (tree rebuilding is expensive)
- For applications requiring only specific factual answers
- When latency must be minimized (multi-level retrieval adds overhead)
- For real-time document ingestion scenarios

## Related Skills
- [Hierarchical Chunking](../../chunking/hierarchical-chunking/SKILL.md) - Document-level hierarchy
- [Multi-Pass Retrieval with Reranking](../multi-pass-retrieval-with-reranking/SKILL.md) - Result refinement
- [Graph RAG](../graph-rag/SKILL.md) - Relationship-based retrieval

## Metrics & Success Criteria
- **Scalability**: Efficient handling of growing document collections
- **Retrieval Quality**: Improved NDCG through balanced level selection
- **Query Coverage**: Better results across both broad and specific queries
- **Index Build Time**: Acceptable time for tree construction
- **Traceability**: Reliable parent-child linking for source verification
