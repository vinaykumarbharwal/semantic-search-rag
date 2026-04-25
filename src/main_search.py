from src.embeddings import EmbeddingService
from src.retrieval import FAISSIndexManager, RetrievalService
from src.logger import logger

def test_search(query: str):
    """Test script to perform a semantic search."""
    
    # 1. Initialize services
    embedding_service = EmbeddingService()
    index_manager = FAISSIndexManager(embedding_service)
    
    # 2. Load the existing index
    if not index_manager.load_index():
        logger.error("Failed to load index. Please run ingestion first.")
        return

    # 3. Perform search
    retriever = RetrievalService(index_manager)
    results = retriever.search_with_scores(query)
    
    # 4. Display results
    print(f"\n--- Search Results for: '{query}' ---")
    for doc, score in results:
        print(f"\n[Score: {score:.4f}] [Source: {doc.metadata.get('file_name')}] [Page: {doc.metadata.get('page')}]")
        print(f"Content: {doc.page_content[:200]}...")

if __name__ == "__main__":
    import sys
    test_query = sys.argv[1] if len(sys.argv) > 1 else "What is semantic search?"
    test_search(test_query)
