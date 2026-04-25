from src.config import Config
from src.logger import logger
from src.ingestion import DocumentLoader, TextChunker
from src.embeddings import EmbeddingService
from src.retrieval import FAISSIndexManager

class IngestionPipeline:
    """Orchestrates the full ingestion process from files to vector index."""
    
    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker(
            chunk_size=Config.CHUNK_SIZE, 
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        self.embedding_service = EmbeddingService()
        self.index_manager = FAISSIndexManager(self.embedding_service)

    def run_pipeline(self, directory_path: str = None):
        """Executes the full ingestion workflow."""
        dir_path = directory_path or str(Config.DATA_DIR)
        logger.info(f"Starting ingestion pipeline for directory: {dir_path}")
        
        # 1. Load Documents
        raw_docs = self.loader.load_directory(dir_path)
        if not raw_docs:
            logger.warning("No documents found to process.")
            return
        
        # 2. Chunk Documents & Enrich Metadata
        chunks = self.chunker.split_documents(raw_docs)
        
        # 3. Create or Update FAISS Index
        # For v1, we rebuild the index; for production, we could load and add.
        self.index_manager.create_index(chunks)
        
        # 4. Persist to disk
        self.index_manager.save_index()
        
        logger.info("Ingestion pipeline completed successfully.")

if __name__ == "__main__":
    # Allow running the script directly for testing
    pipeline = IngestionPipeline()
    pipeline.run_pipeline()

