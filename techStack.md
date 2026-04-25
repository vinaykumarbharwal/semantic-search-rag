# Tech Stack — Semantic Search (RAG System)

---

## 🧠 Core AI / ML

| Component | Technology |
|-----------|-----------|
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) or OpenAI Embeddings |
| LLM (Generation) | GPT (via API) or open-source models (Llama / Mistral) |
| Architecture | Retrieval-Augmented Generation (RAG) |

---

## 🔎 Retrieval & Vector Search

| Component | Technology |
|-----------|-----------|
| Vector Database | FAISS (Facebook AI Similarity Search) |
| Similarity Search | Cosine Similarity / Inner Product |
| Indexing | Flat / IVF (for scalability) |

---

## 📄 Data Processing

| Component | Technology |
|-----------|-----------|
| Text Extraction | PyPDF / LangChain Document Loaders |
| Preprocessing | NLTK / spaCy |
| Chunking | LangChain Text Splitters |

---

## 🔗 Backend / API

| Component | Technology |
|-----------|-----------|
| Framework | FastAPI |
| Server | Uvicorn |
| API Type | REST (query → response) |

---

## 🧩 Orchestration (RAG Pipeline)

**Framework:** LangChain / LlamaIndex

Handles:
- Document ingestion
- Embedding pipeline
- Retrieval + LLM integration

---

## 💾 Storage

| Component | Technology |
|-----------|-----------|
| Vector Store | FAISS (local) |
| Metadata Storage | SQLite / JSON |

---

## 🎨 Frontend (Optional)

| Option | Technology |
|--------|-----------|
| Full UI | React / HTML + CSS |
| Quick Demo | Streamlit |

---

## ☁️ Deployment

| Component | Platform |
|-----------|---------|
| Backend Hosting | Render / Railway |
| Frontend Hosting | Vercel / Netlify |
| Model Hosting (optional) | Hugging Face |

---

## 📊 Monitoring & Evaluation

| Aspect | Details |
|--------|---------|
| Metrics | Retrieval accuracy, latency |
| Evaluation | Precision@K, Recall@K |

---

## 🗺️ Architecture Overview

```
User Query
    │
    ▼
FastAPI (REST API)
    │
    ▼
LangChain / LlamaIndex Orchestration
    │
    ├──► Embedding Model (Sentence Transformers / OpenAI)
    │         │
    │         ▼
    │    Query Vector
    │         │
    │         ▼
    ├──► FAISS Vector Store ──► Top-K Relevant Chunks
    │
    ▼
LLM (GPT / Llama / Mistral)
    │
    ▼
Generated Response
    │
    ▼
Frontend (React / Streamlit)
```