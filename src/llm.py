from typing import Optional, List
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from src.config import Config
from src.logger import logger

class LLMClient:
    """Client for Groq LLM provider."""
    
    def __init__(self, model_name: str = None):
        self.provider = "groq"
        self.model_name = model_name or "llama-3.1-8b-instant"
        
        logger.info(f"Initializing LLMClient | Provider: Groq | Model: {self.model_name}")
        
        if not Config.GROQ_API_KEY:
            logger.error("Groq API Key not found in environment.")
            
        self.llm = ChatGroq(
            model=self.model_name,
            groq_api_key=Config.GROQ_API_KEY,
            temperature=0
        )

    def generate(self, messages: List[BaseMessage]) -> str:
        """Generates a response from the LLM."""
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            logger.error(f"Error during LLM generation with model {self.model_name}: {str(e)}")
            return "I'm sorry, but I encountered an error while processing your request."

    def get_llm(self):
        """Returns the underlying LangChain LLM object."""
        return self.llm
