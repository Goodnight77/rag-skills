---
name: rag-skills
description: Use this skill when building, debugging, or improving Retrieval-Augmented Generation systems, including chunking, vector database selection, hybrid search, reranking, multimodal RAG, code documentation RAG, retrieval latency, and production RAG architecture.
---

# RAG Skills

This skill routes RAG implementation work to the right guide in this repository.
Use it when a user asks for help designing, implementing, improving, evaluating,
or operating a Retrieval-Augmented Generation pipeline.

## How to Use This Skill

1. Identify the main RAG problem: chunking, vector storage, retrieval quality,
   data type handling, latency, evaluation, agents, or deployment.
2. Open the most relevant guide under `skills/`.
3. Follow the guide's decision criteria, implementation notes, references, and
   success metrics.
4. Prefer lightweight examples in this repo, then use the linked external
   implementations for production code patterns.

## Skill Routes

### Chunking

- `skills/chunking/semantic-chunking.md`: Chunk by semantic boundaries instead
  of fixed token windows.
- `skills/chunking/hierarchical-chunking.md`: Preserve document hierarchy across
  sections, headings, and nested structures.
- `skills/chunking/sliding-window-chunking.md`: Add overlap to preserve context
  near chunk boundaries.
- `skills/chunking/contextual-chunk-headers.md`: Add inherited section context
  to chunks.
- `skills/chunking/choosing-a-chunking-framework.md`: Select chunking libraries
  and frameworks.

### Vector Databases

- `skills/vector-databases/qdrant-setup-rag.md`: Set up Qdrant for RAG with
  metadata and filtering.
- `skills/vector-databases/qdrant-for-production-rag.md`: Operate Qdrant in
  production RAG systems.
- `skills/vector-databases/choosing-vector-db-by-datatype.md`: Choose a vector
  database for text, code, multimodal, and structured data.

### Retrieval Strategies

- `skills/retrieval-strategies/hybrid-search-bm25-dense.md`: Combine keyword
  and dense vector retrieval.
- `skills/retrieval-strategies/multi-pass-retrieval-with-reranking.md`: Retrieve
  broadly, then rerank with a stronger model.
- `skills/retrieval-strategies/query-transformation-strategies.md`: Rewrite,
  decompose, or expand queries before retrieval.
- `skills/retrieval-strategies/hyde-hypothetical-document-embeddings.md`: Use
  hypothetical answer documents to improve query embeddings.
- `skills/retrieval-strategies/hype-hypothetical-prompt-embeddings.md`: Index
  likely prompts or questions alongside source content.
- `skills/retrieval-strategies/self-rag.md`: Add self-reflection and retrieval
  validation to generation workflows.
- `skills/retrieval-strategies/raptor-hierarchical-retrieval.md`: Retrieve over
  hierarchical summaries and source chunks.
- `skills/retrieval-strategies/context-enrichment-window.md`: Expand retrieved
  chunks with neighboring context.
- `skills/retrieval-strategies/adaptive-retrieval.md`: Choose retrieval strategy
  dynamically based on query type.
- `skills/retrieval-strategies/explainable-retrieval.md`: Improve traceability
  with source attribution and citations.
- `skills/retrieval-strategies/crag-corrective-rag.md`: Correct weak retrieval
  with validation and fallback search.
- `skills/retrieval-strategies/graph-rag.md`: Use graph structure and entity
  relationships for retrieval.

### Data Type Handling

- `skills/data-type-handling/rag-for-code-documentation.md`: Handle code,
  APIs, examples, and technical documentation.
- `skills/data-type-handling/rag-for-multimodal-content.md`: Handle images,
  tables, diagrams, and mixed media.

### Performance Optimization

- `skills/performance-optimization/optimize-retrieval-latency.md`: Reduce
  retrieval latency with indexing, caching, and query optimization.

## Success Criteria

- The selected RAG pattern matches the user's actual bottleneck.
- Retrieval quality improves without adding unnecessary architecture.
- The implementation keeps metadata, evaluation, and production constraints in
  view from the start.
- External references are used for real implementation details instead of
  copying large code blocks into this skill.
