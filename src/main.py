from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
from src.config import Config
from src.logger import logger
from src.embeddings import EmbeddingService
from src.retrieval import FAISSIndexManager, RetrievalService
from src.llm import LLMClient
from src.rag import RAGService
from src.pipeline import IngestionPipeline
import time
import os

app = FastAPI(
    title="Semantic Search RAG API",
    description="Intelligent Document Retrieval & Question-Answering System",
    version="1.0.0"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Start time for uptime calculation
START_TIME = time.time()

@app.get("/")
async def root():
    """Redirects to the API documentation."""
    return RedirectResponse(url="/docs")

@app.get("/api/v1/health")
async def health_check():
    """Returns the health status of the API and its components."""
    
    # Check Index Status
    try:
        embedding_service = EmbeddingService()
        index_manager = FAISSIndexManager(embedding_service)
        index_exists = index_manager.load_index()
        index_status = "ready" if index_exists else "not_initialized"
    except Exception as e:
        logger.error(f"Health check failed for index: {str(e)}")
        index_status = "error"

    return {
        "status": "healthy",
        "uptime_seconds": int(time.time() - START_TIME),
        "version": "1.0.0",
        "components": {
            "index": index_status,
            "embedding_model": Config.EMBEDDING_MODEL,
            "llm_backend": "configured" if Config.GROQ_API_KEY else "missing_keys"
        }
    }

@app.post("/api/v1/ingest")
async def ingest_documents(background_tasks: BackgroundTasks, files: List[UploadFile] = File(...)):
    """Uploads and processes documents into the vector index."""
    
    saved_files = []
    for file in files:
        file_path = Config.DATA_DIR / file.filename
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_files.append(file.filename)
            logger.info(f"File saved to: {file_path}")
        except Exception as e:
            logger.error(f"Failed to save file {file.filename}: {str(e)}")

    # Trigger ingestion pipeline in the background
    pipeline = IngestionPipeline()
    background_tasks.add_task(pipeline.run_pipeline)

    return {
        "message": f"Successfully uploaded {len(saved_files)} files. Ingestion started in background.",
        "files": saved_files,
        "status": "processing"
    }

@app.get("/api/v1/search")
async def search(q: str, k: int = 5):
    """Performs semantic search and returns top-K chunks with scores."""
    
    start_time = time.time()
    try:
        embedding_service = EmbeddingService()
        index_manager = FAISSIndexManager(embedding_service)
        
        if not index_manager.load_index():
            return {"error": "Index not found. Please ingest documents first.", "results": []}

        retriever = RetrievalService(index_manager)
        results = retriever.search_with_scores(q, k=k)
        
        formatted_results = [
            {
                "chunk": doc.page_content,
                "score": float(score),
                "metadata": doc.metadata
            }
            for doc, score in results
        ]

        return {
            "query": q,
            "results": formatted_results,
            "latency_ms": int((time.time() - start_time) * 1000)
        }
    except Exception as e:
        logger.error(f"Search endpoint error: {str(e)}")
        return {"error": str(e), "results": []}

@app.post("/api/v1/ask")
async def ask(question: str, k: int = 5):
    """RAG endpoint - retrieve context and generate an answer."""
    
    start_time = time.time()
    try:
        # 1. Initialize Services
        embedding_service = EmbeddingService()
        index_manager = FAISSIndexManager(embedding_service)
        
        if not index_manager.load_index():
            return {"error": "Index not found. Please ingest documents first."}

        retriever = RetrievalService(index_manager)
        llm_client = LLMClient()
        rag_service = RAGService(retriever, llm_client)
        
        # 2. Get Answer
        result = rag_service.answer_question(question, k=k)
        
        # 3. Add Latency
        result["latency_ms"] = int((time.time() - start_time) * 1000)
        
        return result
    except Exception as e:
        logger.error(f"RAG endpoint error: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

