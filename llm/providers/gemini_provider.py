"""
Gemini Provider

Implements the BaseLLM interface using Google Gemini.
"""

import google.generativeai as genai

from core.config import Config
from llm.base import BaseLLM


class GeminiProvider(BaseLLM):
    """
    Gemini implementation of BaseLLM.
    """

    def __init__(self):

        genai.configure(
            api_key=Config.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.3,
    ) -> str:

        if system_prompt:
            prompt = (
                f"System Instruction:\n"
                f"{system_prompt}\n\n"
                f"User:\n{prompt}"
            )

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": temperature,
            },
        )

        return response.text