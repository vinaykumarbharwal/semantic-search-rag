from typing import Optional, List
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from src.config import Config
from src.logger import logger

class LLMClient:
    """Pluggable client for different LLM providers (OpenAI, Anthropic)."""
    
    def __init__(self, provider: str = "openai", model_name: str = None):
        self.provider = provider.lower()
        self.model_name = model_name
        
        # Hardcoded fallback for OpenAI to prevent 404s with gpt-4-turbo-preview
        if self.provider == "openai" and not self.model_name:
            self.model_name = "gpt-3.5-turbo"
            
        logger.info(f"Initializing LLMClient | Provider: {self.provider} | Model: {self.model_name}")
        
        if self.provider == "openai":
            if not Config.OPENAI_API_KEY:
                logger.error("OpenAI API Key not found in environment.")
            self.llm = ChatOpenAI(
                model=self.model_name,
                api_key=Config.OPENAI_API_KEY,
                temperature=0
            )
        elif self.provider == "anthropic":
            if not Config.ANTHROPIC_API_KEY:
                logger.error("Anthropic API Key not found in environment.")
            self.llm = ChatAnthropic(
                model=self.model_name or "claude-3-opus-20240229",
                anthropic_api_key=Config.ANTHROPIC_API_KEY,
                temperature=0
            )
        elif self.provider == "groq":
            if not Config.GROQ_API_KEY:
                logger.error("Groq API Key not found in environment.")
            self.llm = ChatGroq(
                model=self.model_name or "llama-3.1-8b-instant",
                groq_api_key=Config.GROQ_API_KEY,
                temperature=0
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")

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
