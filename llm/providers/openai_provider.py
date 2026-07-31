from openai import OpenAI

from core.config import Config
from llm.base import BaseLLM


class OpenAIProvider(BaseLLM):

    def __init__(self):
        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

    def generate(
        self,
        prompt: str,
        output_schema=None,
        system_prompt=None,
        temperature=0.3,
    ):

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

        if output_schema is None:

            response = self.client.chat.completions.create(
                model="gpt-4.1",
                messages=messages,
                temperature=temperature,
            )

            return response.choices[0].message.content

        response = self.client.beta.chat.completions.parse(
            model="gpt-4.1",
            messages=messages,
            response_format=output_schema,
        )

        return response.choices[0].message.parsed