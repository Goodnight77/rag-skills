---
name: graph-rag
title: "Graph RAG - Knowledge Graph Retrieval"
description: "Use knowledge graphs to connect related information across documents for enhanced retrieval."
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
category: "retrieval-strategies"
tags: ["graph-rag", "knowledge-graph", "entity-extraction", "community-detection"]
---

## Overview
Graph RAG enhances traditional retrieval by constructing knowledge graphs from documents, identifying communities of related entities, and using these structures to improve retrieval. This approach excels at connecting disparate information and providing holistic understanding across large document collections.

## Problem Statement
Traditional chunk-based retrieval has limitations:
- **Fragmented Information**: Related concepts split across different chunks
- **No Context Connections**: Retrieval can't connect information from separate sources
- **Limited Global Understanding**: Difficulty synthesizing information across entire corpus
- **Missing Relationships**: Entity relationships not captured in flat retrieval
- **Poor Sensemaking**: Struggles with tasks requiring global understanding

## Key Concepts
- **Entity Extraction**: Identifying key entities (people, places, concepts) from text
- **Relationship Extraction**: Finding connections between extracted entities
- **Graph Construction**: Building knowledge graphs with entities as nodes and relationships as edges
- **Community Detection**: Clustering related entities to find thematic groups
- **Community Summarization**: Creating summaries for each community for efficient retrieval
- **Local and Global Retrieval**: Supporting both specific and comprehensive queries

## Implementation Guide

### Step 1: Extract Entities and Relationships
Use an LLM to identify entities and their relationships from document chunks.

**Why**: Entity extraction transforms unstructured text into structured knowledge, enabling graph-based retrieval that understands connections between concepts.

Direct the LLM to extract entities (people, places, concepts, etc.) and the relationships between them.

### Step 2: Construct Knowledge Graph
Build a graph from extracted entities and relationships.

**Why**: A knowledge graph provides a structured representation of how entities connect across the document collection, enabling retrieval that traverses these connections.

Create nodes for entities and edges for relationships, building a graph structure that can be queried and traversed.

### Step 3: Detect Communities
Apply community detection algorithms to identify clusters of related entities.

**Why**: Communities represent thematic groupings in the graph—entities that are closely connected form natural clusters that can be summarized together.

Use community detection algorithms (e.g., Leiden, Louvain) to find clusters of highly connected entities.

### Step 4: Summarize Communities
Generate summaries for each community to provide context for retrieval.

**Why**: Community summaries condense related information into manageable pieces, enabling efficient retrieval while preserving thematic connections.

For each community, summarize the relevant documents and entity information into concise overviews.

### Step 5: Implement Local Retrieval
Query using community summaries for specific, focused answers.

**Why**: Local retrieval provides precise, contextually relevant answers by matching queries to the most appropriate community summaries.

Match queries to community summaries and retrieve documents from the most relevant communities.

### Step 6: Implement Global Retrieval
Synthesize information across all communities for comprehensive answers.

**Why**: Global retrieval is needed for queries that require understanding across multiple communities or the entire corpus.

Generate preliminary answers from each community and synthesize into a comprehensive response.

### Step 7: Build Complete Graph RAG Pipeline
Combine all components into a cohesive system.

**Why**: A complete pipeline with both local and global retrieval modes ensures optimal performance for both specific and comprehensive queries.

For implementation patterns, see [Microsoft GraphRAG](https://microsoft.github.io/graphrag/), the [GraphRAG documentation](https://microsoft.github.io/graphrag/), and [networkx community detection](https://networkx.org/documentation/stable/reference/algorithms/community.html) for implementation details.

## When to Use This Skill
- Building RAG systems for large document collections with interconnected concepts
- When queries require connecting information from disparate sources
- For applications requiring global understanding and sensemaking
- For domains with clear entity relationships (biographies, technical domains)
- When traditional chunk-based retrieval misses important connections

## When NOT to Use This Skill
- For small document collections where chunk retrieval is sufficient
- When indexing cost and time are major constraints
- For documents with weak entity relationships (unstructured narratives)
- For simple fact-finding queries that don't require synthesis
- When implementation complexity must be minimized

## Related Skills
- [RAPTOR](../raptor-hierarchical-retrieval/SKILL.md) - Alternative hierarchical approach
- [Explainable Retrieval](../explainable-retrieval/SKILL.md) - Citation and traceability
- [Adaptive Retrieval](../adaptive-retrieval/SKILL.md) - Dynamic query processing

## Metrics & Success Criteria
- **Global Understanding**: Improved performance on sensemaking tasks
- **Connection Discovery**: Ability to connect related information across sources
- **Query Coverage**: Better results for both specific and comprehensive queries
- **Graph Quality**: Meaningful entity and relationship extraction
- **Summary Effectiveness**: Community summaries capture essential information
