class RAGPrompts:
    """Central store for RAG prompt templates."""
    
    SYSTEM_PROMPT = """You are an intelligent knowledge assistant. Your task is to answer the user's question using ONLY the provided context chunks.

STRICT RULES:
1. Use ONLY the provided context to answer. If the answer is not in the context, say: "I'm sorry, but I don't have enough information in my context to answer that."
2. DO NOT use your own external knowledge.
3. For every claim you make, cite the source using the format [Source: filename, Page: X].
4. Keep your answer concise and professional.
5. If multiple sources discuss the same point, cite all of them.

CONTEXT:
{context}
"""

    HUMAN_PROMPT = "Question: {question}"

    @staticmethod
    def format_system_prompt(context: str) -> str:
        """Formats the system prompt with the retrieved context."""
        return RAGPrompts.SYSTEM_PROMPT.format(context=context)

    @staticmethod
    def format_human_prompt(question: str) -> str:
        """Formats the human prompt with the user question."""
        return RAGPrompts.HUMAN_PROMPT.format(question=question)
