from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.config import Config
from src.logger import logger

class EmbeddingService:
    """Service to handle text embedding generation."""
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or Config.EMBEDDING_MODEL
        logger.info(f"Initializing EmbeddingService with model: {self.model_name}")
        
        try:
            self.embeddings = HuggingFaceEmbeddings(
                model_name=self.model_name,
                cache_folder=str(Config.MODELS_DIR)
            )
            logger.info("Embedding model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load embedding model: {str(e)}")
            raise

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generates embeddings for a list of strings."""
        return self.embeddings.embed_documents(texts)

    def embed_query(self, text: str) -> List[float]:
        """Generates an embedding for a single query string."""
        return self.embeddings.embed_query(text)

    def get_embedding_function(self):
        """Returns the underlying LangChain embedding object."""
        return self.embeddings

