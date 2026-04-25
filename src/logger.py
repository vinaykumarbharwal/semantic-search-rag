import logging
import sys
from pathlib import Path

def setup_logger(name: str = "rag_system", log_level: str = "INFO") -> logging.Logger:
    """Sets up a standardized logger for the application."""
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Avoid duplicate handlers
    if not logger.handlers:
        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        
        # Formatter: [Timestamp] [Level] [Module] - Message
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        
    return logger

# Default logger instance
logger = setup_logger()
