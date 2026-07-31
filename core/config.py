"""
Application configuration.

Loads all environment variables from the .env file.
"""

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


class Config:
    """Centralized application configuration."""

    APP_NAME = "AI Investment Research Agent"
    VERSION = "1.0.0"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")