from typing import List, Optional, Tuple
import os
from sentence_transformers import CrossEncoder
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from src.config import Config
from src.logger import logger
from src.embeddings import EmbeddingService

class FAISSIndexManager:
    """Manages creation, loading, and persistence of FAISS indices."""
    
    def __init__(self, embedding_service: EmbeddingService):
        self.embedding_service = embedding_service
        self.vector_store: Optional[FAISS] = None

    def create_index(self, documents: List[Document]):
        """Creates a new FAISS index from a list of documents."""
        logger.info(f"Creating new FAISS index with {len(documents)} documents...")
        try:
            self.vector_store = FAISS.from_documents(
                documents, 
                self.embedding_service.get_embedding_function()
            )
            logger.info("FAISS index created successfully.")
        except Exception as e:
            logger.error(f"Error creating FAISS index: {str(e)}")
            raise

    def save_index(self, path: str = None):
        """Persists the FAISS index to disk."""
        save_path = path or str(Config.INDEX_PATH)
        if not self.vector_store:
            logger.error("No vector store found to save.")
            return
        
        try:
            self.vector_store.save_local(save_path)
            logger.info(f"FAISS index saved to {save_path}")
        except Exception as e:
            logger.error(f"Error saving FAISS index: {str(e)}")

    def load_index(self, path: str = None):
        """Loads a FAISS index from disk."""
        load_path = path or str(Config.INDEX_PATH)
        logger.info(f"Loading FAISS index from {load_path}...")
        
        if not os.path.exists(load_path):
            logger.warning(f"Index path {load_path} does not exist.")
            return False
            
        try:
            self.vector_store = FAISS.load_local(
                load_path, 
                self.embedding_service.get_embedding_function(),
                allow_dangerous_deserialization=True # Required for local loading
            )
            logger.info("FAISS index loaded successfully.")
            return True
        except Exception as e:
            logger.error(f"Error loading FAISS index: {str(e)}")
            return False

    def add_documents(self, documents: List[Document]):
        """Adds more documents to an existing FAISS index."""
        if not self.vector_store:
            logger.info("No existing index. Creating new one.")
            self.create_index(documents)
        else:
            logger.info(f"Adding {len(documents)} documents to existing index...")
            self.vector_store.add_documents(documents)
            logger.info("Documents added successfully.")

    def get_vector_store(self) -> Optional[FAISS]:
        """Returns the FAISS vector store instance."""
        return self.vector_store

class RetrievalService:
    """High-level service for handling semantic search and retrieval."""
    
    def __init__(self, index_manager: FAISSIndexManager):
        self.index_manager = index_manager

    def search(self, query: str, k: int = None) -> List[Document]:
        """Performs similarity search on the FAISS index."""
        k = k or Config.RETRIEVAL_K
        vector_store = self.index_manager.get_vector_store()
        
        if not vector_store:
            logger.warning("Search attempted but vector store is not initialized.")
            return []
            
        logger.info(f"Performing semantic search for: '{query}' (k={k})")
        try:
            results = vector_store.similarity_search(query, k=k)
            logger.info(f"Found {len(results)} relevant documents.")
            return results
        except Exception as e:
            logger.error(f"Error during search: {str(e)}")
            return []

    def search_with_scores(self, query: str, k: int = None):
        """Performs search and returns documents with their similarity scores."""
        k = k or Config.RETRIEVAL_K
        vector_store = self.index_manager.get_vector_store()
        
        if not vector_store:
            return []
            
        try:
            # results is a list of (Document, score)
            results = vector_store.similarity_search_with_score(query, k=k)
            return results
        except Exception as e:
            logger.error(f"Error during search with scores: {str(e)}")
            return []

    def search_with_reranking(self, query: str, k: int = 10, rerank_k: int = 5) -> List[Document]:
        """Performs search followed by cross-encoder reranking."""
        # 1. Initial Retrieval (Fetch more than needed)
        initial_results = self.search(query, k=k)
        if not initial_results:
            return []

        # 2. Rerank
        reranker = Reranker()
        reranked_docs = reranker.rerank(query, initial_results, top_n=rerank_k)
        
        return reranked_docs

class Reranker:
    """Uses a Cross-Encoder to re-score and re-order retrieved documents."""
    
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        logger.info(f"Initializing Reranker with model: {model_name}")
        try:
            self.model = CrossEncoder(model_name)
        except Exception as e:
            logger.error(f"Failed to load Reranker model: {str(e)}")
            self.model = None

    def rerank(self, query: str, documents: List[Document], top_n: int = 5) -> List[Document]:
        """Reranks documents based on their relevance to the query."""
        if not self.model or not documents:
            return documents[:top_n]

        # Prepare pairs for cross-encoder: [(query, doc1), (query, doc2), ...]
        pairs = [[query, doc.page_content] for doc in documents]
        
        # Get relevance scores
        scores = self.model.predict(pairs)
        
        # Sort documents by score descending
        scored_docs = sorted(zip(scores, documents), key=lambda x: x[0], reverse=True)
        
        logger.info(f"Reranked {len(documents)} documents. Top score: {scored_docs[0][0]:.4f}")
        
        return [doc for score, doc in scored_docs[:top_n]]
