"""
Ollama Provider

Implements the BaseLLM interface using Ollama.
"""

import ollama

from llm.base import BaseLLM


class OllamaProvider(BaseLLM):
    """
    Ollama implementation of BaseLLM.
    """

    def __init__(self):

        self.model = "llama3.2:3b"

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.3,
    ) -> str:

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = ollama.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": temperature,
            },
        )

        return response["message"]["content"]