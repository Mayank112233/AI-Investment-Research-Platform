"""
LLM Provider Factory

Creates the appropriate LLM provider.
"""

from llm.providers.openai_provider import OpenAIProvider
from llm.providers.gemini_provider import GeminiProvider
from llm.providers.ollama_provider import OllamaProvider


class ProviderFactory:
    """
    Factory class for creating LLM providers.
    """

    @staticmethod
    def create(provider: str):

        provider = provider.lower()

        if provider == "openai":
            return OpenAIProvider()

        elif provider == "gemini":
            return GeminiProvider()

        elif provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )