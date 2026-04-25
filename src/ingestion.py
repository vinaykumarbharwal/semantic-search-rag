from typing import List, Optional
from pathlib import Path
from datetime import datetime
import uuid
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.logger import logger

class DocumentLoader:
    """Unified loader for various document formats."""
    
    @staticmethod
    def load_document(file_path: str) -> List[Document]:
        """Loads a document based on its file extension."""
        path = Path(file_path)
        extension = path.suffix.lower()
        
        try:
            if extension == ".pdf":
                loader = PyPDFLoader(file_path)
            elif extension == ".txt":
                loader = TextLoader(file_path, encoding="utf-8")
            elif extension == ".md":
                loader = UnstructuredMarkdownLoader(file_path)
            else:
                logger.warning(f"Unsupported file format: {extension}. Skipping {file_path}")
                return []
            
            documents = loader.load()
            logger.info(f"Successfully loaded {len(documents)} pages/documents from {file_path}")
            return documents
            
        except Exception as e:
            logger.error(f"Error loading document {file_path}: {str(e)}")
            return []

    @staticmethod
    def load_directory(directory_path: str) -> List[Document]:
        """Loads all supported documents from a directory."""
        path = Path(directory_path)
        all_documents = []
        
        supported_extensions = [".pdf", ".txt", ".md"]
        
        for file in path.iterdir():
            if file.suffix.lower() in supported_extensions:
                all_documents.extend(DocumentLoader.load_document(str(file)))
        
        logger.info(f"Total documents loaded from directory {directory_path}: {len(all_documents)}")
        return all_documents

class TextChunker:
    """Handles splitting documents into smaller, overlapping chunks."""
    
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 64):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Using RecursiveCharacterTextSplitter as a robust default, 
        # but configured for token-like behavior if needed.
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len, # Character count by default, but can be switched to token count
            add_start_index=True,
        )
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Splits a list of documents into chunks."""
        chunks = self.splitter.split_documents(documents)
        
        # Enrich metadata for each chunk
        enriched_chunks = MetadataExtractor.enrich_chunks(chunks)
        
        logger.info(f"Split {len(documents)} documents into {len(enriched_chunks)} enriched chunks.")
        return enriched_chunks

class MetadataExtractor:
    """Enriches document chunks with additional metadata."""
    
    @staticmethod
    def enrich_chunks(chunks: List[Document]) -> List[Document]:
        """Adds timestamps, UUIDs, and cleans up source paths in chunks."""
        timestamp = datetime.utcnow().isoformat()
        
        for chunk in chunks:
            # Ensure source is just the filename, not the full path
            if "source" in chunk.metadata:
                chunk.metadata["file_name"] = Path(chunk.metadata["source"]).name
            
            # Add ingestion timestamp
            chunk.metadata["ingested_at"] = timestamp
            
            # Add a unique chunk ID
            chunk.metadata["chunk_id"] = str(uuid.uuid4())
            
            # Ensure page exists (default to 0 if not present)
            if "page" not in chunk.metadata:
                chunk.metadata["page"] = 0
                
        return chunks
