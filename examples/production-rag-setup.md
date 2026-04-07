---
title: "Production RAG Setup"
category: "rag-agents"
level: "advanced"
tags: ["production", "deployment", "monitoring", "scaling"]
author: "rag-skills"
last_updated: "2026-04-07"
---

## Overview
This example outlines what a production RAG deployment should contain without inlining a full application, Docker stack, and infrastructure repo into this repository. Use it as an operations blueprint and pair it with external implementation references for actual deployment work.

## Goal
Move from a prototype RAG system to a reliable service with:
1. Isolated ingestion and query paths
2. Monitoring and alerting
3. Caching and rate control
4. Backup and recovery procedures
5. Capacity planning and operational guardrails

## Reference Architecture

```text
Clients
  -> API Gateway / Auth Layer
    -> Query Service
    -> Ingestion Service
    -> Cache
    -> Vector Database
    -> Metadata Store
    -> Monitoring / Logging / Alerting
```

## Core Components

### Query Service
- Accepts user queries
- Retrieves context and generates answers
- Applies rate limits, timeouts, and request tracing

### Ingestion Service
- Runs independently from live query traffic
- Handles parsing, chunking, embedding, and indexing
- Supports retries, queueing, and backfills

### Vector Database
- Stores embeddings and retrieval metadata
- Must support the filtering and scale profile required by the application

### Metadata Store
- Tracks document provenance, ingestion jobs, tenants, and audit data
- Keeps operational state out of the vector store where appropriate

### Cache Layer
- Reduces repeated retrieval and generation cost
- Should be applied deliberately to repeated or high-volume query patterns

### Observability Stack
- Metrics for latency, retrieval quality proxies, cache hit rate, and error rate
- Structured logs for ingestion and query flows
- Alerts for regression and outage conditions

## Deployment Workflow

### Stage 1: Harden the Prototype
- Separate ingestion from query serving
- Add health checks and request logging
- Externalize configuration and secrets

### Stage 2: Add Operational Controls
- Introduce caching
- Add retries with backoff for external dependencies
- Put queueing around expensive or long-running ingestion jobs

### Stage 3: Add Monitoring
- Track query latency, retrieval latency, token cost, ingestion throughput, and error rate
- Instrument the vector store and model dependencies
- Establish dashboards before scaling traffic

### Stage 4: Scale Deliberately
- Benchmark ingestion and query paths separately
- Scale only the saturated component
- Revisit chunking, top-k, reranking, and caching before throwing hardware at the problem

## Pseudocode

```text
receive request
authenticate and rate-limit
check cache if appropriate
retrieve candidate chunks
optionally rerank
generate grounded answer
log metrics and traces
return answer with sources

run ingestion asynchronously:
  parse source
  chunk content
  embed chunks
  write to vector store
  update metadata and status
```

## Production Checklist
- Health checks exist for every critical service
- Ingestion failures are retryable and observable
- Query requests have timeouts and correlation IDs
- Secrets are not stored in repo files
- Logs are structured and searchable
- Dashboards exist for latency, throughput, and failures
- Backups and restore tests are documented
- Evaluation datasets exist for regression testing
- Capacity limits and scaling thresholds are defined

## Common Failure Modes
- Ingestion and query traffic share the same constrained resources
- There is no clean metadata model for document lifecycle or provenance
- Metrics exist for API uptime but not for retrieval quality regressions
- Cache is added blindly and serves stale or low-value results
- Teams scale infra before fixing poor chunking or retrieval design

## External Implementations
- [Qdrant production guide](https://qdrant.tech/documentation/guides/production/)
- [FastAPI deployment concepts](https://fastapi.tiangolo.com/deployment/)
- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/)
- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)

## Related Skills
- [Qdrant for Production RAG](../skills/vector-databases/qdrant-for-production-rag.md)
- [Optimize Retrieval Latency](../skills/performance-optimization/optimize-retrieval-latency.md)
- [Multi-Agent RAG](./multi-agent-rag.md)
