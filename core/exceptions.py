"""
Custom application exceptions.
"""


class AppException(Exception):
    """Base exception."""

    pass


class ConfigurationError(AppException):
    """Configuration errors."""

    pass


class ToolExecutionError(AppException):
    """Tool execution errors."""

    pass


class AgentExecutionError(AppException):
    """Agent execution errors."""

    pass