---
title: "Foundational RAG Pipeline Example"
category: "rag-agents"
level: "beginner"
tags: ["tutorial", "quickstart", "pipeline"]
author: "rag-skills"
last_updated: "2026-04-05"
---

## Overview
This example shows how to build a foundational RAG (Retrieval-Augmented Generation) pipeline from scratch. It demonstrates the core retrieval-and-generation flow that other skills in this repo build on.

## Prerequisites
- Python 3.9+
- Basic understanding of LLMs and vector databases

## What You'll Build
A simple Q&A bot that:
1. Ingests documents into a vector database
2. Retrieves relevant passages based on user queries
3. Generates answers using retrieved context

## Step 1: Set Up the Environment

```bash
# Create a virtual environment
python -m venv rag_env
source rag_env/bin/activate  # On Windows: rag_env\Scripts\activate

# Install dependencies
pip install openai qdrant-client sentence-transformers python-dotenv
```

Create a `.env` file with your API keys:

```bash
OPENAI_API_KEY=your-openai-api-key
```

## Step 2: Create the Document Processor

```python
# document_processor.py
from typing import List, Dict
from pathlib import Path

class DocumentProcessor:
    """Process documents for RAG ingestion."""

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def load_documents(self, directory: str) -> List[Dict]:
        """Load text files from a directory."""
        documents = []
        path = Path(directory)

        for file in path.glob("*.txt"):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                documents.append({
                    "id": file.stem,
                    "content": content,
                    "source": str(file)
                })

        return documents

    def chunk_document(self, doc: Dict) -> List[Dict]:
        """Split a document into chunks."""
        content = doc["content"]
        chunks = []

        for i in range(0, len(content), self.chunk_size - self.overlap):
            chunk_text = content[i:i + self.chunk_size]
            if chunk_text:
                chunks.append({
                    "id": f"{doc['id']}_chunk_{len(chunks)}",
                    "content": chunk_text,
                    "source": doc["source"]
                })

        return chunks

# Usage
processor = DocumentProcessor(chunk_size=500, overlap=50)
documents = processor.load_documents("./documents")

# Chunk all documents
all_chunks = []
for doc in documents:
    all_chunks.extend(processor.chunk_document(doc))
```

## Step 3: Set Up the Vector Database

```python
# vector_store.py
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class VectorStore:
    """Manage vector database for RAG."""

    def __init__(self, url: str = "http://localhost:6333"):
        self.client = QdrantClient(url=url)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def create_collection(self, collection_name: str):
        """Create a collection for storing documents."""
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=self.model.get_sentence_embedding_dimension(),
                distance=Distance.COSINE
            )
        )

    def ingest_chunks(self, collection_name: str, chunks: List[Dict]):
        """Add document chunks to the vector database."""
        points = []

        for i, chunk in enumerate(chunks):
            # Generate embedding
            embedding = self.model.encode(chunk["content"])

            # Create point
            point = PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={
                    "content": chunk["content"],
                    "source": chunk.get("source"),
                    "chunk_id": chunk["id"]
                }
            )
            points.append(point)

        # Upload points
        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

        print(f"Ingested {len(points)} chunks")

    def search(self, collection_name: str, query: str, top_k: int = 3):
        """Search for relevant chunks."""
        # Generate query embedding
        query_embedding = self.model.encode(query)

        # Search
        results = self.client.search(
            collection_name=collection_name,
            query_vector=query_embedding.tolist(),
            limit=top_k,
            with_payload=True
        )

        return [
            {
                "content": r.payload["content"],
                "score": r.score
            }
            for r in results
        ]

# Usage
store = VectorStore()

# Create collection (skip if already exists)
try:
    store.create_collection("my_rag_docs")
except:
    print("Collection already exists")

# Ingest documents
store.ingest_chunks("my_rag_docs", all_chunks)
```

## Step 4: Create the RAG Pipeline

```python
# rag_pipeline.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class RAGPipeline:
    """Simple RAG pipeline."""

    def __init__(self, vector_store, collection_name: str):
        self.vector_store = vector_store
        self.collection_name = collection_name
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def query(self, question: str, top_k: int = 3) -> str:
        """Answer a question using retrieved context."""
        # Retrieve relevant chunks
        chunks = self.vector_store.search(self.collection_name, question, top_k)

        # Build context
        context = "\n\n".join([
            f"[Chunk {i+1}] {c['content']}"
            for i, c in enumerate(chunks)
        ])

        # Generate answer
        prompt = f"""Answer the question based on the context below.

Context:
{context}

Question: {question}

Answer:"""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content

# Usage
pipeline = RAGPipeline(store, "my_rag_docs")

# Ask a question
answer = pipeline.query("What is RAG?")
print(f"Answer: {answer}")
```

## Step 5: Complete Example

```python
# main.py - Putting it all together
from document_processor import DocumentProcessor
from vector_store import VectorStore
from rag_pipeline import RAGPipeline

# Initialize
processor = DocumentProcessor()
store = VectorStore()

# Load and chunk documents
documents = processor.load_documents("./documents")
all_chunks = []
for doc in documents:
    all_chunks.extend(processor.chunk_document(doc))

# Create collection and ingest
try:
    store.create_collection("my_rag_docs")
except:
    pass

store.ingest_chunks("my_rag_docs", all_chunks)

# Create RAG pipeline
pipeline = RAGPipeline(store, "my_rag_docs")

# Interactive loop
print("RAG Q&A Bot (type 'quit' to exit)")
print("-" * 50)

while True:
    question = input("\nYour question: ")

    if question.lower() in ['quit', 'exit', 'q']:
        break

    answer = pipeline.query(question)
    print(f"\nAnswer: {answer}")
```

## Running the Example

1. Create sample documents in a `documents/` directory:

```bash
mkdir documents
echo "RAG stands for Retrieval-Augmented Generation. It's a technique that combines retrieval systems with language models to improve accuracy." > documents/rag_intro.txt
echo "Vector databases store document embeddings for efficient semantic search. Popular options include Qdrant, Pinecone, and Weaviate." > documents/vector_dbs.txt
echo "Embedding models convert text to vector representations. Models like SentenceTransformers and OpenAI's text-embedding-ada-002 are commonly used." > documents/embeddings.txt
```

2. Run the pipeline:

```bash
python main.py
```

## Expected Output

```
RAG Q&A Bot (type 'quit' to exit)
--------------------------------------------------

Your question: What is RAG?

Answer: RAG stands for Retrieval-Augmented Generation. It's a technique that combines retrieval systems with language models to improve accuracy.

Your question: quit
```

## Next Steps

- Improve chunking with semantic boundaries
- Add metadata filtering
- Implement hybrid search (keyword + semantic)
- Add citation sources to answers

## Related Skills

- [Semantic Chunking](../skills/chunking/semantic-chunking.md) - Start with chunking that preserves meaning
- [Qdrant Setup for RAG](../skills/vector-databases/qdrant-setup-rag.md) - Use a vector store with metadata filtering
- [Hybrid Search BM25 Dense](../skills/retrieval-strategies/hybrid-search-bm25-dense.md) - Improve retrieval quality with hybrid search
