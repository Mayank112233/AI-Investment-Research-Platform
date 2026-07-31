from abc import ABC, abstractmethod
from typing import Type
from pydantic import BaseModel


class BaseLLM(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_schema: Type[BaseModel] | None = None,
    ):
        pass