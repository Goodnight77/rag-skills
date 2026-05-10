**Project Brief: RAG Skills Repository**

You are building an open-source repository called "rag-skills" that serves as a modular collection of best-practice guides and skill definitions for coding agents, AI frameworks (like Vercel Agent Skills, Claude Code, etc.), and developers building Retrieval-Augmented Generation pipelines.

**Repository Purpose:**
This repo consolidates actionable skills and guides that help developers and AI coding agents improve RAG performance, choose appropriate vector databases and data stores for specific use cases, implement effective chunking strategies, optimize retrieval quality, and orchestrate multi-step RAG workflows. Skills are written as markdown files that can be indexed, parsed, and executed by agents or used as reference documentation by humans.

**Repository Structure:**
Create the following directory layout:

```
rag-skills/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── skills/
│ ├── chunking/
│ ├── vector-databases/
│ ├── retrieval-strategies/
│ ├── data-type-handling/
│ ├── performance-optimization/
│ ├── evaluation-metrics/
│ ├── rag-agents/
│ └── deployment/
├── examples/
│ ├── beginner-rag-pipeline.md
│ ├── multi-agent-rag.md
│ └── production-rag-setup.md
├── templates/
│ ├── skill-template.md
│ └── workflow-template.md
└── scripts/
├── validate-skills.py
└── generate-index.py
```

**Skill File Format:**
Each markdown skill file should follow this structure:

```
---
title: "Skill Name"
category: "chunking|vector-databases|retrieval-strategies|data-type-handling|performance-optimization|evaluation-metrics|rag-agents|deployment"
level: "beginner|intermediate|advanced"
tags: ["tag1", "tag2", "tag3"]
author: "Author Name"
last_updated: "YYYY-MM-DD"
---

## Overview
[2-3 sentence description of what this skill covers and why it matters for RAG systems]

## Problem Statement
[Describe the specific challenge this skill addresses]

## Key Concepts
- **Concept 1**: Brief explanation
- **Concept 2**: Brief explanation
- **Concept 3**: Brief explanation

## Implementation Guide

### Step 1: [Step Name]
[Detailed explanation with reasoning]

### Step 2: [Step Name]
[Detailed explanation with reasoning]

### Step 3: [Step Name]
[Detailed explanation with reasoning]

## Code Example
\`\`\`python
# Practical, runnable example
\`\`\`

## When to Use This Skill
- Use case 1
- Use case 2
- Use case 3

## When NOT to Use This Skill
- Anti-pattern 1
- Anti-pattern 2

## Related Skills
- [Related Skill 1](../category/skill-name/SKILL.md)
- [Related Skill 2](../category/skill-name/SKILL.md)

## References
- [Reference 1](#)
- [Reference 2](#)

## Metrics & Success Criteria
- Success indicator 1
- Success indicator 2
```

**Initial Skills to Create:**

Create at least 12 foundational skill files across categories:

**Chunking Category (3 skills):**
1. `semantic-chunking.md` - Chunk documents based on semantic boundaries, not just size
2. `hierarchical-chunking.md` - Multi-level chunking for nested document structures
3. `sliding-window-chunking.md` - Overlap-based chunking to preserve context

**Vector Databases Category (3 skills):**
1. `qdrant-setup-rag.md` - Setting up Qdrant for RAG with filtering and metadata
2. `qdrant-for-production-rag.md` - Scaling RAG with Qdrant in production environments
3`choosing-vector-db-by-datatype.md` - Which vector DB for text vs. multimodal vs. code

**Retrieval Strategies Category (2 skills):**
1. `hybrid-search-bm25-dense.md` - Combining keyword and semantic search
2. `multi-pass-retrieval-with-reranking.md` - Two-pass retrieval with cross-encoder reranking

**Data Type Handling Category (2 skills):**
1. `rag-for-code-documentation.md` - Special handling for code snippets, APIs, and technical docs
2. `rag-for-multimodal-content.md` - Images, tables, and mixed media in RAG systems

**Performance Optimization Category (1 skill):**
1. `optimize-retrieval-latency.md` - Caching, indexing, and query optimization strategies

**Root README.md:**
The README should:
- Explain the purpose and vision of the repo
- Show how to browse skills by category and difficulty level
- Include a quick-start guide for integrating skills into Claude Code, Vercel Agent Skills, or other frameworks
- Show how to use skills programmatically (parsing metadata, executing workflows)
- Link to CONTRIBUTING guidelines for adding new skills

**Contributing Guidelines (CONTRIBUTING.md):**
Specify:
- How to submit new skills
- Skill review criteria (clarity, accuracy, completeness, code examples)
- Naming conventions for skill files
- How to test and validate skills before submission
- Credit and attribution guidelines

**Goal:**
After completion, the repo should be a well-organized, agent-friendly, and human-readable resource that:
1. Agents can parse and understand to improve their own RAG implementations
2. Developers can browse and reference when building RAG systems
3. Teams can integrate into their AI frameworks or skill marketplaces
4. Can be extended with new skills and updated as RAG best practices evolve



**Important Note on Code Examples:**
Do not write extensive code implementations in the markdown files. 
Instead, each skill should reference real-world implementations by 
searching for existing open-source projects, libraries, and tutorials 
that demonstrate the concept. For each skill, research and include 
links to three to five high-quality external resources—GitHub repos, 
blog posts, or documentation—that show practical implementations. Use 
brief pseudocode or one-liner examples only to illustrate the concept, 
then point readers to the actual implementation in those referenced projects.
This keeps the skills lightweight, discovery-focused, and ensures users 
engage with battle-tested code from the community.