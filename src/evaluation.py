from typing import List, Dict
import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)
from src.rag import RAGService
from src.logger import logger

class RAGASEvaluator:
    """Handles automated evaluation of the RAG system using RAGAS."""
    
    def __init__(self, rag_service: RAGService):
        self.rag_service = rag_service
        self.metrics = [
            faithfulness,
            answer_relevancy,
            context_recall,
            context_precision,
        ]

    def evaluate_questions(self, test_dataset: List[Dict[str, str]]):
        """
        Runs evaluation on a list of test questions.
        Expected format: [{"question": "...", "ground_truth": "..."}]
        """
        data = {
            "question": [],
            "answer": [],
            "contexts": [],
            "ground_truth": []
        }

        logger.info(f"Starting RAGAS evaluation on {len(test_dataset)} questions...")

        for item in test_dataset:
            question = item["question"]
            ground_truth = item["ground_truth"]
            
            # Run RAG
            result = self.rag_service.answer_question(question)
            
            data["question"].append(question)
            data["answer"].append(result["answer"])
            data["contexts"].append([s["excerpt"] for s in result["sources"]])
            data["ground_truth"].append(ground_truth)

        # Convert to HuggingFace Dataset
        dataset = Dataset.from_dict(data)

        # Run Evaluation
        result = evaluate(
            dataset,
            metrics=self.metrics
        )

        logger.info("Evaluation completed.")
        return result

if __name__ == "__main__":
    # Example usage / mock test
    from src.retrieval import FAISSIndexManager, RetrievalService
    from src.embeddings import EmbeddingService
    from src.llm import LLMClient
    
    # Setup services
    emb = EmbeddingService()
    idx = FAISSIndexManager(emb)
    idx.load_index()
    ret = RetrievalService(idx)
    llm = LLMClient()
    rag = RAGService(ret, llm)
    
    evaluator = RAGASEvaluator(rag)
    
    # Sample Test Set
    test_set = [
        {
            "question": "What are the core pillars of the design system?",
            "ground_truth": "Developer Credibility, Enterprise Authority, and Conversion Clarity."
        }
    ]
    
    scores = evaluator.evaluate_questions(test_set)
    print("\n--- RAGAS Evaluation Scores ---")
    print(scores)

