"""
Abstract Base Tool

Every tool in the project must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all tools.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique name of the tool.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Description of what the tool does.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool.
        """
        pass