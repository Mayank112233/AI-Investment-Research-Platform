"""
Application Dependencies

Creates shared services used across the application.
"""

from llm.factory import ProviderFactory
from llm.service import LLMService

from tools.registry import ToolRegistry


class DependencyContainer:
    """
    Creates shared application services.
    """

    def __init__(self):

        # --------------------------
        # LLM
        # --------------------------

        provider = ProviderFactory.create("openai")

        self.llm = LLMService(provider)

        # --------------------------
        # Registry
        # --------------------------

        self.registry = ToolRegistry()