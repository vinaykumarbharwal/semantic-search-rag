# Product Requirements Document
## Embedding-Based Semantic Search with RAG
### Intelligent Document Retrieval & Question-Answering System

> **Version:** 1.0 — Initial Release | **Status:** Draft — Under Review | **Date:** April 2026

---

## Document Information

| Field | Details |
|---|---|
| **Project Name** | Embedding-Based Semantic Search with RAG |
| **Document Version** | v1.0 — Initial Release |
| **Status** | Draft — Under Review |
| **Author(s)** | GenAI Platform Team |
| **Stakeholders** | Engineering, Product, Data Science, DevOps |
| **Created Date** | April 2026 |
| **Last Updated** | April 25, 2026 |
| **Target Release** | Q3 2026 |

---

## 1. Executive Summary

This document defines the product requirements for an **Embedding-Based Semantic Search and Retrieval-Augmented Generation (RAG)** system — an AI-powered knowledge retrieval platform that understands the meaning behind user queries rather than simply matching keywords.

Inspired by search experiences at LinkedIn, Slack, and Notion, this system ingests large document collections (PDFs, articles, knowledge bases), converts them into dense vector embeddings using transformer models, indexes them in a FAISS vector database, and delivers semantically relevant results paired with LLM-generated answers.

The system establishes a production-grade GenAI pipeline suitable for AI/ML and enterprise roles in 2025–2026, demonstrating mastery of embeddings, vector search, RAG architecture, and FastAPI deployment.

---

## 2. Problem Statement

### 2.1 Current Limitations

Traditional keyword-based search systems suffer from fundamental limitations that prevent them from serving the needs of knowledge-intensive workflows:

- **Vocabulary mismatch:** A query for "car pricing" misses documents discussing "automobile cost" or "vehicle valuation."
- **No contextual understanding:** Systems cannot distinguish between "apple the fruit" and "Apple the company" without heavy manual tagging.
- **Poor handling of natural language:** Boolean search cannot process conversational or multi-concept queries.
- **Inability to synthesize answers:** Results are raw documents — users must read and extract answers manually.
- **Scalability issues:** As document volumes grow, precision of keyword search drops without expensive re-indexing.

### 2.2 Opportunity

Modern transformer-based embedding models and vector databases now make it possible to build search systems that understand semantic meaning at scale. Combined with retrieval-augmented generation, these systems can not only find relevant documents but synthesize accurate, context-aware answers — transforming passive document retrieval into an active knowledge assistant.

---

## 3. Goals & Non-Goals

### 3.1 Goals

- Build a semantic search engine using vector embeddings that outperforms keyword matching on real document corpora.
- Implement a complete RAG pipeline: ingestion → chunking → embedding → retrieval → generation.
- Provide a FastAPI-based REST API exposable to downstream applications and frontends.
- Support multiple document formats (PDF, TXT, Markdown, HTML, DOCX) via a unified ingestion pipeline.
- Deliver sub-second retrieval for corpora up to 1 million document chunks.
- Produce an architecture that can be extended with reranking, hybrid search, and multi-modal inputs.

### 3.2 Non-Goals (v1.0)

- Real-time document ingestion (streaming ingestion to be added in v1.2).
- Multi-tenant access control and document-level permissions (planned for v2.0).
- Native mobile client — the API will serve a web frontend only.
- Fine-tuning custom embedding models — the system uses pre-trained models with optional adapters.
- Support for audio or video document types.

---

## 4. Target Users & Personas

### 👤 Persona 1: The Knowledge Worker
- **Role:** Analyst, Researcher, Support Engineer
- **Need:** Quickly find answers from a large internal document base without reading hundreds of pages.
- **Pain Point:** Current search returns documents, not answers. Multi-document synthesis is manual and slow.

### 👤 Persona 2: The Developer / AI Engineer
- **Role:** ML Engineer, Backend Developer, GenAI Practitioner
- **Need:** A reference implementation of a production RAG system to adapt for internal tooling or portfolio projects.
- **Pain Point:** Fragmented tutorials don't cover end-to-end pipeline, API design, and evaluation together.

### 👤 Persona 3: The Product Team
- **Role:** Product Manager, CTO, Technical Lead
- **Need:** Evaluate GenAI-powered search as a replacement for legacy enterprise search tooling.
- **Pain Point:** No clear benchmark between semantic and keyword approaches in their specific domain.

---

## 5. System Architecture

### 5.1 High-Level Architecture

The system operates across three subsystems — an offline ingestion pipeline and an online query pipeline.

```
┌─────────────────────────────────────────────────────────────┐
│                    INGESTION PIPELINE                        │
│  Document Loader → Text Extractor → Chunker →               │
│  Embedding Model → FAISS Index                              │
│  Formats: PDF, TXT, MD, DOCX, HTML                          │
│  Chunk size: 512 tokens | Overlap: 64 tokens                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    RETRIEVAL ENGINE                          │
│  Query → Embed Query → FAISS Top-K Search →                 │
│  Reranker (optional) → Context Window                       │
│  k=5 (default) | Similarity: Cosine                        │
│  Index: IndexFlatL2 / IVF for large corpora                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                 GENERATION LAYER (RAG)                       │
│  Retrieved Chunks → Prompt Template →                       │
│  LLM (Claude / GPT-4 / Llama) → Answer + Sources           │
│  Context-aware answering | Source citations | Confidence    │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Technology Stack

| Layer | Technology | Rationale |
|---|---|---|
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`, `BAAI/bge-large`) | State-of-the-art open-source models, low latency, multilingual support |
| **Vector Store** | FAISS (Facebook AI Similarity Search) | Battle-tested, GPU/CPU support, billion-scale indexing, no infrastructure dependency |
| **LLM** | Anthropic Claude / OpenAI GPT-4 / Llama 3 (via Ollama) | Pluggable backend; Claude preferred for RAG due to 200K context window |
| **API Layer** | FastAPI + Uvicorn | Async, type-safe, auto-generated OpenAPI docs, production-grade performance |
| **Doc Parsing** | PyMuPDF, python-docx, BeautifulSoup | Robust multi-format extraction with metadata preservation |
| **Reranking** | Cross-encoder (`ms-marco-MiniLM-L-6-v2`) | Precision-boosting reranking without additional infrastructure |
| **Orchestration** | LangChain / LlamaIndex (optional) | RAG chain composition, memory, and tool integration |
| **Storage** | PostgreSQL + pgvector (metadata) / S3 (raw docs) | Durable metadata store with optional pgvector for hybrid search |
| **Monitoring** | Prometheus + Grafana / LangSmith | Latency, retrieval quality, and LLM cost observability |
| **Containerization** | Docker + Docker Compose | Reproducible local and cloud deployment |

---

## 6. Feature Requirements

### 6.1 Feature List with Priority

| Feature | Description | Priority |
|---|---|:---:|
| Document Ingestion API | Upload and process PDF, TXT, DOCX, MD, HTML files via REST endpoint | **P0** |
| Text Chunking | Configurable chunking with token-based sliding window and overlap | **P0** |
| Embedding Generation | Batch embedding using Sentence Transformers; GPU acceleration support | **P0** |
| FAISS Indexing | Persistent index with incremental upsert and full rebuild options | **P0** |
| Semantic Search API | Top-K similarity search with cosine scoring and source metadata | **P0** |
| RAG Answer Generation | Prompt assembly from retrieved chunks + LLM call + source citation | **P0** |
| Multi-format Parsing | Unified parser supporting PDF, DOCX, HTML, Markdown | **P0** |
| REST API (FastAPI) | Full OpenAPI spec with `/ingest`, `/search`, `/ask`, `/health` endpoints | **P0** |
| Reranking Layer | Cross-encoder reranking of top-K candidates to improve precision | **P1** |
| Hybrid Search | Combine BM25 keyword + dense retrieval for improved recall | **P1** |
| Metadata Filtering | Pre-filter FAISS results by doc type, date, author, tags | **P1** |
| Streaming Responses | Server-sent events for real-time token streaming from LLM | **P1** |
| Evaluation Suite | Automated RAGAS metrics: faithfulness, answer relevancy, context recall | **P1** |
| Web UI (Demo) | Minimal Streamlit or React frontend for demo and testing | **P2** |
| Multi-LLM Support | Pluggable LLM backend: Claude, OpenAI, Ollama, Cohere | **P2** |
| Document Management | List, delete, and re-index individual documents via API | **P2** |
| Conversation History | Multi-turn Q&A with session memory for follow-up queries | **P2** |

> **Priority Key:** P0 = Must-have (launch blocker) | P1 = Should-have (v1 quality) | P2 = Nice-to-have (post-launch)

---

## 7. API Specification

### `POST /api/v1/ingest`
Upload one or more documents for ingestion into the vector index.

```
Request:  multipart/form-data — file(s), optional metadata JSON
Response: { doc_id, chunks_created, embedding_time_ms, status }
```

### `GET /api/v1/search`
Perform semantic search and return top-K document chunks with similarity scores.

```
Params:   q (query string), k (int, default 5), filter (JSON metadata filter)
Response: { results: [ { chunk, doc_id, score, metadata } ], latency_ms }
```

### `POST /api/v1/ask`
RAG endpoint — retrieve relevant chunks and generate an answer via LLM.

```
Body:     { question, k, session_id (optional), stream (bool) }
Response: { answer, sources: [ { doc_id, excerpt, score } ], tokens_used, latency_ms }
```

### `GET /api/v1/health`
Health check for index status, embedding model load, and LLM connectivity.

```
Response: { status, index_size, model, llm_backend, uptime_s }
```

---

## 8. Non-Functional Requirements

### 8.1 Performance
- Search latency (P95): **< 200ms** for corpora up to 500K chunks on CPU; < 50ms on GPU.
- RAG end-to-end latency (P95): **< 3 seconds** (exclusive of LLM streaming first-token time).
- Ingestion throughput: **>= 500 documents/minute** on a 4-core instance.
- Index capacity: Support up to **10M vectors** without reindexing via IVF partitioning.

### 8.2 Reliability
- API availability SLA: **99.5% uptime** (excluding planned maintenance).
- FAISS index persisted to disk after every ingestion batch; crash recovery within 30 seconds.
- Graceful degradation: If LLM is unavailable, `/search` continues to serve retrieval results.

### 8.3 Security
- All API endpoints protected by API key authentication (Bearer token) in production.
- No raw document content stored in plaintext in the vector metadata store.
- LLM API keys stored in environment variables; never logged or returned in responses.
- Rate limiting: **60 requests/min per API key** on `/ask` to prevent LLM cost abuse.

### 8.4 Scalability
- Stateless FastAPI workers — horizontal scaling via Docker Compose replicas or Kubernetes pods.
- FAISS index shared via NFS or pre-loaded into each worker at startup.
- Batch embedding jobs decoupled from the API via an async task queue (Celery + Redis).

---

## 9. Success Metrics & KPIs

| Metric | Target | Measurement Method |
|---|:---:|---|
| Retrieval Recall@5 | >= 85% | RAGAS framework on held-out QA dataset |
| Answer Faithfulness | >= 90% | RAGAS faithfulness score (hallucination rate) |
| Answer Relevancy | >= 80% | RAGAS answer relevancy metric |
| Search Latency P95 | < 200ms | Prometheus histogram on `/search` endpoint |
| RAG Latency P95 | < 3,000ms | End-to-end timing in LangSmith traces |
| MRR (Mean Reciprocal Rank) | >= 0.75 | Offline evaluation on annotated query set |
| LLM Cost per Query | < $0.01 | Token usage tracking per `/ask` call |
| Ingestion Success Rate | >= 99% | % of uploaded docs successfully indexed |

---

## 10. Roadmap & Milestones

| Phase | Duration | Key Deliverables |
|---|:---:|---|
| **Phase 0: Foundation** | Week 1–2 | Project scaffold, dev environment, CI/CD pipeline, Docker setup, FAISS hello-world |
| **Phase 1: Ingestion** | Week 3–4 | Document loader, chunker, batch embedding pipeline, FAISS index builder and persistence |
| **Phase 2: Retrieval** | Week 5–6 | Semantic search API, top-K FAISS query, metadata filtering, basic reranker integration |
| **Phase 3: RAG** | Week 7–8 | Prompt templates, LLM integration (Claude + OpenAI), `/ask` endpoint, source citations |
| **Phase 4: Quality** | Week 9–10 | RAGAS evaluation suite, benchmark dataset, latency optimization, hybrid BM25+dense search |
| **Phase 5: Hardening** | Week 11–12 | Auth, rate limiting, logging, Prometheus metrics, Grafana dashboard, load testing |
| **Phase 6: Demo & Docs** | Week 13 | Streamlit demo UI, README, API docs, architecture diagram, portfolio writeup |

---

## 11. Risks & Mitigations

| Risk | Severity | Mitigation Strategy |
|---|:---:|---|
| LLM API rate limits or cost overrun | 🔴 High | Request queuing, caching for repeated queries, hard token budget caps per session |
| Embedding model quality insufficient for domain | 🔴 High | Benchmark 3+ models on domain data; support fine-tuned adapter injection in v1.1 |
| FAISS index corruption on crash | 🟡 Medium | WAL-style incremental saves + periodic full snapshots to S3; crash recovery tested in CI |
| Chunking strategy loses cross-chunk context | 🟡 Medium | Overlapping windows + parent-document retrieval; tune chunk size per corpus |
| Hallucination in LLM-generated answers | 🔴 High | Strict RAG prompt: "answer only from context"; faithfulness scoring via RAGAS in CI gate |
| Slow ingestion for large corpora (>100K docs) | 🟡 Medium | Async Celery workers + GPU batch embedding; IVF index for approximate search at scale |
| Data privacy / PII in uploaded documents | 🟡 Medium | PII detection pre-processing step; encryption at rest; access logging |

---

## 12. Dependencies & Assumptions

### 12.1 External Dependencies
- **Anthropic Claude API or OpenAI API:** Active account with sufficient quota for development and testing.
- **Hugging Face Hub:** Access to download Sentence Transformer and cross-encoder model weights.
- **FAISS:** v1.7+ compiled with GPU support (CUDA 11+) for production; CPU-only for dev.
- **Docker:** v24+ and Docker Compose v2+ for local orchestration.

### 12.2 Assumptions
- Development team has Python 3.10+ and basic familiarity with transformer architectures.
- A test document corpus (>1,000 documents) is available for benchmarking by Phase 4.
- GPU instance (T4 or A10G) is available on cloud infrastructure for embedding benchmarks.
- The system will be deployed on a single-region cloud instance for v1.0.

---

## Appendix: Glossary

| Term | Definition |
|---|---|
| **RAG** | Retrieval-Augmented Generation: combining retrieval of relevant documents with LLM-based generation to produce grounded answers. |
| **Embedding** | A dense numeric vector representation of text that encodes semantic meaning. Similar texts have vectors that are close in high-dimensional space. |
| **FAISS** | Facebook AI Similarity Search: a library for efficient similarity search and clustering of dense vectors. |
| **Chunking** | The process of splitting large documents into smaller overlapping segments suitable for embedding and retrieval. |
| **Top-K Retrieval** | Returning the K most semantically similar document chunks to a given query based on vector distance. |
| **Reranking** | A second-pass scoring step using a cross-encoder model to reorder retrieved results by relevance. |
| **RAGAS** | RAG Assessment framework: automated evaluation of RAG systems measuring faithfulness, relevancy, and context recall. |
| **BM25** | Best Match 25: a keyword-based ranking function used in hybrid search alongside dense embeddings. |
| **IVF Index** | Inverted File Index: a FAISS index type using clustering for approximate nearest neighbour search at billion scale. |
| **LangChain** | A Python framework for composing LLM-powered applications including RAG pipelines and agents. |

---

*End of Document — Embedding-Based Semantic Search with RAG | v1.0 | April 2026*
*Confidential — Internal Use Only*