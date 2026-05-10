# RAG Skills Index

Total Skills: 38

---

## Browse by Category

### Chunking

- [Choosing a Chunking Framework](skills/chunking/choosing-a-chunking-framework/SKILL.md)
  - *Chunking quality depends as much on the framework as on the strategy itself.*
- [Contextual Chunk Headers](skills/chunking/contextual-chunk-headers/SKILL.md)
  - *Contextual chunk headers (CCH) enhance retrieval by prepending higher-level context (document title, section headers, summaries) to each chunk before embedding.*
- [Hierarchical Chunking](skills/chunking/hierarchical-chunking/SKILL.md)
  - *Hierarchical chunking creates multi-level chunk structures that preserve document hierarchies (chapters, sections, subsections).*
- [Semantic Chunking](skills/chunking/semantic-chunking/SKILL.md)
  - *Semantic chunking divides documents into segments based on natural language boundaries and semantic meaning rather than fixed character counts.*
- [Chunking](skills/chunking/SKILL.md)
  - *Use this parent skill when the main RAG problem is how to split source material into retrievable units.*
- [Sliding Window Chunking](skills/chunking/sliding-window-chunking/SKILL.md)
  - *Sliding window chunking creates overlapping chunks where each chunk shares content with adjacent chunks.*

### Data Type Handling

- [RAG for Code Documentation](skills/data-type-handling/rag-for-code-documentation/SKILL.md)
  - *RAG for code documentation requires specialized handling due to code's structured nature, syntax-specific patterns, and the importance of preserving function signatures, imports, and contextual relationships.*
- [RAG for Multimodal Content](skills/data-type-handling/rag-for-multimodal-content/SKILL.md)
  - *Multimodal RAG extends retrieval to include images, videos, audio, and mixed media content alongside text.*
- [Data Type Handling](skills/data-type-handling/SKILL.md)
  - *Use this parent skill when source material is not plain prose or when different data types need different parsing, metadata, chunking, and retrieval strategies.*

### Deployment

- [Index Versioning and Reindexing](skills/deployment/index-versioning-and-reindexing/SKILL.md)
  - *This skill covers evolving the index behind a live RAG system: rebuilding embeddings after a model or chunking change, migrating between embedding models, and versioning indexes so changes are reversible and queries never go dark.*
- [Production RAG Deployment](skills/deployment/production-rag-deployment/SKILL.md)
  - *This skill covers turning a working RAG pipeline into a reliable production service: exposing it behind an API, scaling retrieval and generation independently, caching hot paths, and rolling out changes without breaking users.*
- [Deployment](skills/deployment/SKILL.md)
  - *Use this parent skill when the RAG system works in development but must be made reliable in production.*

### Evaluation Metrics

- [Generation Evaluation Metrics](skills/evaluation-metrics/generation-evaluation-metrics/SKILL.md)
  - *Generation evaluation measures the answer itself: whether it is grounded in the retrieved context, addresses the question, and is factually correct.*
- [RAG Evaluation Frameworks](skills/evaluation-metrics/rag-evaluation-frameworks/SKILL.md)
  - *This skill covers the tooling layer of RAG evaluation: which framework to adopt, how to structure a golden set, and how to run evaluation automatically on every change so quality regressions are blocked before they ship.*
- [Retrieval Evaluation Metrics](skills/evaluation-metrics/retrieval-evaluation-metrics/SKILL.md)
  - *Retrieval evaluation measures whether the pipeline fetched the right chunks before the LLM ever sees them.*
- [Evaluation Metrics](skills/evaluation-metrics/SKILL.md)
  - *Use this parent skill when the main RAG problem is measuring quality, detecting regressions, or proving that a change actually helped.*

### Performance Optimization

- [Optimize Retrieval Latency](skills/performance-optimization/optimize-retrieval-latency/SKILL.md)
  - *Optimizing RAG retrieval latency is critical for production applications where user experience depends on fast response times.*
- [Performance Optimization](skills/performance-optimization/SKILL.md)
  - *Use this parent skill when the RAG system works functionally but is too slow, expensive, or unstable under expected traffic.*

### Rag Agents

- [Agentic RAG Routing](skills/rag-agents/agentic-rag-routing/SKILL.md)
  - *Agentic routing puts a decision step in front of retrieval: the agent classifies the query and chooses whether to retrieve, which source or index to hit, and which tool to call.*
- [Multi-Agent RAG Orchestration](skills/rag-agents/multi-agent-rag-orchestration/SKILL.md)
  - *Multi-agent orchestration splits a complex question across specialized agents, such as a planner, one or more retrievers, and a synthesizer.*
- [RAG Agents](skills/rag-agents/SKILL.md)
  - *Use this parent skill when a single retrieve-then-generate pass is not enough and the system must decide what to retrieve, which tools to call, or how to split work across agents.*

### Retrieval Strategies

- [Adaptive Retrieval](skills/retrieval-strategies/adaptive-retrieval/SKILL.md)
  - *Adaptive retrieval classifies queries into types (factual, analytical, opinion, contextual) and applies different retrieval strategies optimized for each type.*
- [Context Enrichment Window](skills/retrieval-strategies/context-enrichment-window/SKILL.md)
  - *Context enrichment window expands retrieved chunks by including neighboring text from the original document.*
- [CRAG - Corrective RAG](skills/retrieval-strategies/crag-corrective-rag/SKILL.md)
  - *Corrective RAG (CRAG) extends standard retrieval by dynamically evaluating document relevance and correcting the retrieval process when needed.*
- [Explainable Retrieval with Citations](skills/retrieval-strategies/explainable-retrieval/SKILL.md)
  - *Explainable retrieval adds citations, source attribution, and traceability to RAG systems.*
- [Graph RAG - Knowledge Graph Retrieval](skills/retrieval-strategies/graph-rag/SKILL.md)
  - *Graph RAG enhances traditional retrieval by constructing knowledge graphs from documents, identifying communities of related entities, and using these structures to improve retrieval.*
- [Hybrid Search: BM25 + Dense](skills/retrieval-strategies/hybrid-search-bm25-dense/SKILL.md)
  - *Hybrid search combines BM25 (keyword search) with dense vector embeddings (semantic search) to leverage both exact term matching and semantic understanding.*
- [HyDE - Hypothetical Document Embeddings](skills/retrieval-strategies/hyde-hypothetical-document-embeddings/SKILL.md)
  - *HyDE (Hypothetical Document Embeddings) is a query expansion technique that generates a hypothetical document answering the user's query, then uses this synthetic document as the query for vector search.*
- [HyPE - Hypothetical Prompt Embeddings](skills/retrieval-strategies/hype-hypothetical-prompt-embeddings/SKILL.md)
  - *HyPE (Hypothetical Prompt Embeddings) transforms retrieval from query-document matching to question-question matching by generating multiple hypothetical questions for each document chunk during the indexing phase.*
- [Multi-Pass Retrieval with Reranking](skills/retrieval-strategies/multi-pass-retrieval-with-reranking/SKILL.md)
  - *Multi-pass retrieval with reranking is a two-stage approach that first retrieves a broad set of candidates using fast bi-encoder search, then refines them using a more accurate but slower cross-encoder reranker.*
- [Query Transformation Strategies](skills/retrieval-strategies/query-transformation-strategies/SKILL.md)
  - *Query transformation strategies modify or expand user queries before retrieval to bridge the gap between natural language queries and document representations.*
- [RAPTOR - Hierarchical Abstractive Retrieval](skills/retrieval-strategies/raptor-hierarchical-retrieval/SKILL.md)
  - *RAPTOR (Recursive Abstractive Processing and Tree-Organized Retrieval) creates a hierarchical tree of document summaries, allowing retrieval at multiple levels of abstraction.*
- [Self-RAG - Self-Reflective Retrieval](skills/retrieval-strategies/self-rag/SKILL.md)
  - *Self-RAG is a reflective framework that decides whether to retrieve information, evaluates the relevance of retrieved documents, assesses response support, and rates output utility.*
- [Retrieval Strategies](skills/retrieval-strategies/SKILL.md)
  - *Use this parent skill when the main RAG problem is search quality, ranking, recall, context selection, or evidence traceability.*

### Vector Databases

- [Choosing Vector Database by Data Type](skills/vector-databases/choosing-vector-db-by-datatype/SKILL.md)
  - *Selecting the right vector database depends heavily on your data type (text, images, code, multimodal) and use case requirements.*
- [Qdrant for Production RAG](skills/vector-databases/qdrant-for-production-rag/SKILL.md)
  - *Productionizing a RAG system with Qdrant requires considerations beyond basic setup: horizontal scaling, high availability, performance optimization, monitoring, and cost management.*
- [Qdrant Setup for RAG](skills/vector-databases/qdrant-setup-rag/SKILL.md)
  - *Qdrant is an open-source vector similarity search engine designed for high-performance RAG applications.*
- [Vector Databases](skills/vector-databases/SKILL.md)
  - *Use this parent skill when the main RAG problem is choosing, configuring, or operating the vector storage layer.*

## All Skills

| Title | Category | Tags |
|-------|----------|------|
| [Adaptive Retrieval](skills/retrieval-strategies/adaptive-retrieval/SKILL.md) | retrieval-strategies | adaptive, query-classification, dynamic-strategy (+1) |
| [Agentic RAG Routing](skills/rag-agents/agentic-rag-routing/SKILL.md) | rag-agents | routing, tool-use, query-classification (+1) |
| [CRAG - Corrective RAG](skills/retrieval-strategies/crag-corrective-rag/SKILL.md) | retrieval-strategies | crag, corrective, web-search (+2) |
| [Choosing Vector Database by Data Type](skills/vector-databases/choosing-vector-db-by-datatype/SKILL.md) | vector-databases | selection, text, multimodal (+2) |
| [Choosing a Chunking Framework](skills/chunking/choosing-a-chunking-framework/SKILL.md) | chunking | framework-selection, chonkie, langchain (+3) |
| [Chunking](skills/chunking/SKILL.md) | chunking | chunking, routing, rag (+1) |
| [Context Enrichment Window](skills/retrieval-strategies/context-enrichment-window/SKILL.md) | retrieval-strategies | context-enrichment, surrounding-context, window (+1) |
| [Contextual Chunk Headers](skills/chunking/contextual-chunk-headers/SKILL.md) | chunking | contextual-headers, metadata, chunk-enhancement (+1) |
| [Data Type Handling](skills/data-type-handling/SKILL.md) | data-type-handling | data-types, code, multimodal (+1) |
| [Deployment](skills/deployment/SKILL.md) | deployment | deployment, production, reindexing (+1) |
| [Evaluation Metrics](skills/evaluation-metrics/SKILL.md) | evaluation-metrics | evaluation, metrics, ragas (+1) |
| [Explainable Retrieval with Citations](skills/retrieval-strategies/explainable-retrieval/SKILL.md) | retrieval-strategies | explainability, citations, traceability (+1) |
| [Generation Evaluation Metrics](skills/evaluation-metrics/generation-evaluation-metrics/SKILL.md) | evaluation-metrics | generation, faithfulness, llm-as-judge (+1) |
| [Graph RAG - Knowledge Graph Retrieval](skills/retrieval-strategies/graph-rag/SKILL.md) | retrieval-strategies | graph-rag, knowledge-graph, entity-extraction (+1) |
| [Hierarchical Chunking](skills/chunking/hierarchical-chunking/SKILL.md) | chunking | nested, multi-level, document-structure (+1) |
| [HyDE - Hypothetical Document Embeddings](skills/retrieval-strategies/hyde-hypothetical-document-embeddings/SKILL.md) | retrieval-strategies | hyde, query-expansion, llm-generation (+1) |
| [HyPE - Hypothetical Prompt Embeddings](skills/retrieval-strategies/hype-hypothetical-prompt-embeddings/SKILL.md) | retrieval-strategies | hype, precomputed-queries, indexing-time (+1) |
| [Hybrid Search: BM25 + Dense](skills/retrieval-strategies/hybrid-search-bm25-dense/SKILL.md) | retrieval-strategies | hybrid, bm25, dense (+2) |
| [Index Versioning and Reindexing](skills/deployment/index-versioning-and-reindexing/SKILL.md) | deployment | reindexing, versioning, embedding-migration (+1) |
| [Multi-Agent RAG Orchestration](skills/rag-agents/multi-agent-rag-orchestration/SKILL.md) | rag-agents | multi-agent, orchestration, planner (+1) |
| [Multi-Pass Retrieval with Reranking](skills/retrieval-strategies/multi-pass-retrieval-with-reranking/SKILL.md) | retrieval-strategies | reranking, cross-encoder, two-stage (+1) |
| [Optimize Retrieval Latency](skills/performance-optimization/optimize-retrieval-latency/SKILL.md) | performance-optimization | latency, performance, caching (+2) |
| [Performance Optimization](skills/performance-optimization/SKILL.md) | performance-optimization | latency, performance, caching (+1) |
| [Production RAG Deployment](skills/deployment/production-rag-deployment/SKILL.md) | deployment | serving, scaling, canary (+1) |
| [Qdrant Setup for RAG](skills/vector-databases/qdrant-setup-rag/SKILL.md) | vector-databases | qdrant, setup, ingestion (+1) |
| [Qdrant for Production RAG](skills/vector-databases/qdrant-for-production-rag/SKILL.md) | vector-databases | production, scaling, optimization (+1) |
| [Query Transformation Strategies](skills/retrieval-strategies/query-transformation-strategies/SKILL.md) | retrieval-strategies | query-expansion, step-back, sub-query (+1) |
| [RAG Agents](skills/rag-agents/SKILL.md) | rag-agents | agents, agentic-rag, orchestration (+1) |
| [RAG Evaluation Frameworks](skills/evaluation-metrics/rag-evaluation-frameworks/SKILL.md) | evaluation-metrics | ragas, deepeval, trulens (+2) |
| [RAG for Code Documentation](skills/data-type-handling/rag-for-code-documentation/SKILL.md) | data-type-handling | code, programming, syntax (+2) |
| [RAG for Multimodal Content](skills/data-type-handling/rag-for-multimodal-content/SKILL.md) | data-type-handling | multimodal, images, text (+2) |
| [RAPTOR - Hierarchical Abstractive Retrieval](skills/retrieval-strategies/raptor-hierarchical-retrieval/SKILL.md) | retrieval-strategies | raptor, hierarchical, clustering (+2) |
| [Retrieval Evaluation Metrics](skills/evaluation-metrics/retrieval-evaluation-metrics/SKILL.md) | evaluation-metrics | retrieval, recall, ndcg (+2) |
| [Retrieval Strategies](skills/retrieval-strategies/SKILL.md) | retrieval-strategies | retrieval, ranking, hybrid-search (+1) |
| [Self-RAG - Self-Reflective Retrieval](skills/retrieval-strategies/self-rag/SKILL.md) | retrieval-strategies | self-rag, reflection, retrieval-decision (+1) |
| [Semantic Chunking](skills/chunking/semantic-chunking/SKILL.md) | chunking | semantic, nlp, sentence-boundary (+1) |
| [Sliding Window Chunking](skills/chunking/sliding-window-chunking/SKILL.md) | chunking | overlap, context-preservation, window (+1) |
| [Vector Databases](skills/vector-databases/SKILL.md) | vector-databases | vector-database, qdrant, metadata (+1) |
