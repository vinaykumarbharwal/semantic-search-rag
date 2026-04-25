from typing import List, Dict, Any
import re
import time
from langchain_core.messages import SystemMessage, HumanMessage
from src.retrieval import RetrievalService
from src.llm import LLMClient
from src.prompts import RAGPrompts
from src.logger import logger

class RAGService:
    """Orchestrates the Retrieval-Augmented Generation process."""
    
    def __init__(self, retriever: RetrievalService, llm_client: LLMClient):
        self.retriever = retriever
        self.llm_client = llm_client
        self.cache = {} # Simple in-memory cache for v1

    def answer_question(self, question: str, k: int = 5, use_cache: bool = True) -> Dict[str, Any]:
        """Runs the RAG pipeline to answer a user question."""
        
        # 0. Check Cache
        if use_cache and question in self.cache:
            logger.info(f"Cache hit for question: '{question}'")
            return self.cache[question]

        start_time = time.time()
        logger.info(f"RAG Request: '{question}'")
        
        # 1. Retrieve Context
        relevant_docs = self.retriever.search(question, k=k)
        
        if not relevant_docs:
            return {
                "answer": "I'm sorry, but I couldn't find any relevant documents to answer your question.",
                "sources": []
            }
            
        # 2. Prepare Context String
        context_str = "\n\n".join([
            f"--- Document: {doc.metadata.get('file_name')} (Page {doc.metadata.get('page')}) ---\n{doc.page_content}"
            for doc in relevant_docs
        ])
        
        # 3. Format Messages
        messages = [
            SystemMessage(content=RAGPrompts.format_system_prompt(context_str)),
            HumanMessage(content=RAGPrompts.format_human_prompt(question))
        ]
        
        # 4. Generate Answer
        logger.info("Generating answer via LLM...")
        answer = self.llm_client.generate(messages)
        
        # 5. Validate & Format Citations
        validated_answer = CitationManager.validate_citations(answer, relevant_docs)
        
        # 6. Package Sources
        sources = [
            {
                "file_name": doc.metadata.get("file_name"),
                "page": doc.metadata.get("page"),
                "excerpt": doc.page_content[:200] + "..."
            }
            for doc in relevant_docs
        ]
        
        result = {
            "answer": validated_answer,
            "sources": sources,
            "latency_ms": int((time.time() - start_time) * 1000)
        }

        # Save to Cache
        if use_cache:
            self.cache[question] = result

        return result

class CitationManager:
    """Handles post-processing and validation of source citations in LLM responses."""
    
    @staticmethod
    def validate_citations(answer: str, retrieved_docs: List[Any]) -> str:
        """
        Checks if the LLM cited the correct documents and formats them consistently.
        For now, this ensures all cited files actually exist in the retrieved set.
        """
        valid_filenames = {doc.metadata.get("file_name") for doc in retrieved_docs}
        
        # Regex to find [Source: filename, Page: X]
        citation_pattern = r"\[Source:\s*(.*?),\s*Page:\s*(\d+)\]"
        
        def replace_invalid_citations(match):
            filename = match.group(1).strip()
            if filename not in valid_filenames:
                logger.warning(f"LLM hallucinated citation for: {filename}. Removing.")
                return "" # Remove invalid citation
            return match.group(0) # Keep valid citation

        cleaned_answer = re.sub(citation_pattern, replace_invalid_citations, answer)
        return cleaned_answer.strip()
