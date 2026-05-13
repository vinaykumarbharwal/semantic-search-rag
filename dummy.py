import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration management."""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # App Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    APP_ENV = os.getenv("APP_ENV", "development")
    
    # Path Settings
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
    MODELS_DIR = BASE_DIR / os.getenv("MODELS_DIR", "models")
    INDEX_PATH = BASE_DIR / os.getenv("INDEX_PATH", "models/faiss_index")
    
    # RAG Settings
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 512))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 64))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", 5))

# Create directories if they don't exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.MODELS_DIR, exist_ok=True)
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration management."""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # App Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    APP_ENV = os.getenv("APP_ENV", "development")
    
    # Path Settings
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
    MODELS_DIR = BASE_DIR / os.getenv("MODELS_DIR", "models")
    INDEX_PATH = BASE_DIR / os.getenv("INDEX_PATH", "models/faiss_index")
    
    # RAG Settings
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 512))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 64))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", 5))

# Create directories if they don't exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.MODELS_DIR, exist_ok=True)
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration management."""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # App Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    APP_ENV = os.getenv("APP_ENV", "development")
    
    # Path Settings
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
    MODELS_DIR = BASE_DIR / os.getenv("MODELS_DIR", "models")
    INDEX_PATH = BASE_DIR / os.getenv("INDEX_PATH", "models/faiss_index")
    
    # RAG Settings
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 512))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 64))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", 5))

# Create directories if they don't exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.MODELS_DIR, exist_ok=True)
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration management."""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # App Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    APP_ENV = os.getenv("APP_ENV", "development")
    
    # Path Settings
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")
    MODELS_DIR = BASE_DIR / os.getenv("MODELS_DIR", "models")
    INDEX_PATH = BASE_DIR / os.getenv("INDEX_PATH", "models/faiss_index")
    
    # RAG Settings
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 512))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 64))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", 5))

# Create directories if they don't exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.MODELS_DIR, exist_ok=True)
