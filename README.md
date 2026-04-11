# Rag-skills

<p>
  <code>agent routing</code> <code>RAG skills</code> <code>markdown</code>
</p>

A modular collection of best-practice guides and skill definitions for building Retrieval-Augmented Generation (RAG) systems. Designed for AI coding agents, agent frameworks, and teams that want a structured way to route RAG work to the right strategy.

## Overview

RAG-skills consolidates actionable skills that help AI agents and builders improve RAG performance, choose appropriate vector databases, implement effective chunking strategies, optimize retrieval quality, and orchestrate multi-step RAG workflows.

## Installation

### Claude Code

Add this repository as a Claude Code plugin marketplace:

```text
/plugin marketplace add Goodnight77/rag-skills
```

Then install the RAG skills plugin:

```text
/plugin install rag-skills@rag-skills
```

Restart Claude Code after installation.

### Skills CLI

Install with the Skills CLI:

```bash
npx skills add Goodnight77/rag-skills
```

This installs the root [`SKILL.md`](SKILL.md) plus the native skill tree under
[`skills/`](skills/). Claude Code can discover category skills such as
`/chunking` and specific skills such as `/semantic-chunking`.

### Manual Usage

You can also clone the repository and reference the Markdown skills directly:

```bash
git clone https://github.com/Goodnight77/rag-skills.git
```

Then point your agent or coding assistant to the `skills/` directory.

> Note: This repository follows the Claude Code/Qdrant-style structure: category routers live at paths like `skills/chunking/SKILL.md`, and specific skills live at paths like `skills/chunking/semantic-chunking/SKILL.md`.

## Skills by Decision Area

This repo is organized as a routing layer for RAG work. Agents can use the category and metadata in each skill file to decide which path to follow for a given problem, instead of treating the repo like a generic reference manual.

### Chunking
Use these when the main problem is how to split source material into retrievable units.
- [Semantic Chunking](skills/chunking/semantic-chunking/SKILL.md) - Chunk documents based on semantic boundaries
- [Hierarchical Chunking](skills/chunking/hierarchical-chunking/SKILL.md) - Multi-level chunking for nested structures
- [Sliding Window Chunking](skills/chunking/sliding-window-chunking/SKILL.md) - Overlap-based chunking for context preservation
- [Contextual Chunk Headers](skills/chunking/contextual-chunk-headers/SKILL.md) - Adding higher-level context to chunks

### Vector Databases
Use these when the main problem is choosing or operating the storage layer for embeddings and metadata.
- [Qdrant Setup for RAG](skills/vector-databases/qdrant-setup-rag/SKILL.md) - Setting up Qdrant for RAG
- [Qdrant for Production RAG](skills/vector-databases/qdrant-for-production-rag/SKILL.md) - Scaling RAG with Qdrant
- [Choosing Vector DB by Datatype](skills/vector-databases/choosing-vector-db-by-datatype/SKILL.md) - Database selection guide

### Retrieval Strategies
Use these when the main problem is search quality, ranking, recall, or combining search methods.
- [Hybrid Search BM25 Dense](skills/retrieval-strategies/hybrid-search-bm25-dense/SKILL.md) - Combining keyword and semantic search
- [Multi-Pass Retrieval with Reranking](skills/retrieval-strategies/multi-pass-retrieval-with-reranking/SKILL.md) - Two-pass retrieval with cross-encoder reranking
- [Query Transformation Strategies](skills/retrieval-strategies/query-transformation-strategies/SKILL.md) - Query rewriting, step-back prompting, sub-query decomposition
- [HyDE - Hypothetical Document Embeddings](skills/retrieval-strategies/hyde-hypothetical-document-embeddings/SKILL.md) - Query expansion with LLM-generated documents
- [HyPE - Hypothetical Prompt Embeddings](skills/retrieval-strategies/hype-hypothetical-prompt-embeddings/SKILL.md) - Precomputed question embeddings at indexing time
- [Self-RAG](skills/retrieval-strategies/self-rag/SKILL.md) - Self-reflective retrieval with relevance evaluation
- [RAPTOR - Hierarchical Retrieval](skills/retrieval-strategies/raptor-hierarchical-retrieval/SKILL.md) - Multi-level tree of document summaries
- [Context Enrichment Window](skills/retrieval-strategies/context-enrichment-window/SKILL.md) - Adding surrounding chunks to retrieved results
- [Adaptive Retrieval](skills/retrieval-strategies/adaptive-retrieval/SKILL.md) - Dynamic strategy selection based on query type
- [Explainable Retrieval with Citations](skills/retrieval-strategies/explainable-retrieval/SKILL.md) - Traceability and source attribution
- [CRAG - Corrective RAG](skills/retrieval-strategies/crag-corrective-rag/SKILL.md) - Dynamic correction with web search
- [Graph RAG](skills/retrieval-strategies/graph-rag/SKILL.md) - Knowledge graph-based retrieval

### Data Type Handling
Use these when the source content is code, APIs, diagrams, tables, or mixed media.
- [RAG for Code Documentation](skills/data-type-handling/rag-for-code-documentation/SKILL.md) - Special handling for code and technical docs
- [RAG for Multimodal Content](skills/data-type-handling/rag-for-multimodal-content/SKILL.md) - Images, tables, and mixed media

### Performance Optimization
Use these when the problem is latency, throughput, cache behavior, or production efficiency.
- [Optimize Retrieval Latency](skills/performance-optimization/optimize-retrieval-latency/SKILL.md) - Caching, indexing, and query optimization

### RAG Agents
Use these when the problem is orchestration, delegation, or multi-step workflows.
- *See [Examples](#examples) for multi-agent workflows*

### Deployment
Use these when the problem is production rollout, reliability, or operationalization.
- *See [Production RAG Setup](#examples)*

### Evaluation Metrics
Use these when the problem is measurement, regression detection, or retrieval benchmarking.
- *Coming soon*

## Quick Start

### For AI Agents

Read the frontmatter metadata, then route to the skill that best matches the user’s problem. Treat the repo as a decision tree for RAG tasks: chunking, retrieval, vector store choice, embeddings, performance, and workflow orchestration.

### For Framework Integration

Build a lightweight index from the markdown frontmatter and use it to filter by category, tags, and task type. The goal is not to mirror all content in code, but to point an agent to the right skill or external implementation quickly.

Keep examples in the repo lightweight and point readers to external implementations instead of embedding long code samples.

## Examples

Complete walkthroughs and reference implementations:

- [Foundational RAG Pipeline Example](examples/foundational-rag-pipeline.md) - A guided RAG build path for agents and builders
- [Multi-Agent RAG](examples/multi-agent-rag.md) - An orchestration pattern for specialized agents
- [Production RAG Setup](examples/production-rag-setup.md) - A deployment-oriented route for production systems

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Steps

1. Fork the repository
2. Create a new skill file using [templates/skill-template.md](templates/skill-template.md)
3. Ensure your skill follows the required structure
4. Run validation: `python scripts/validate-skills.py`
5. Submit a pull request

## Skill File Format

Each skill follows a consistent structure with a short illustrative snippet, not a full implementation. See the template in [templates/skill-template.md](templates/skill-template.md).

## Scripts

- `validate-skills.py` — Validate all skill files for format compliance
- `generate-index.py` — Generate browsable INDEX.md and SKILLS.json

## Project Status

This is an active open-source project. Skills are continuously added and updated as RAG best practices evolve.

Current statistics:
- **Native Skills**: 28
- **Guide Skills**: 23
- **Category Router Skills**: 5
- **Categories**: 5
- **Examples**: 3

*Run `python scripts/generate-index.py` for current statistics.*

## Acknowledgments

Built for the RAG community. Special thanks to contributors and the open-source RAG ecosystem.


## License

MIT License — see [LICENSE](LICENSE) for details.
