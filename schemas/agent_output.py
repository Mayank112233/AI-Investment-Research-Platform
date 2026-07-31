"""
Agent Output Schema
"""

from pydantic import BaseModel


class AgentOutput(BaseModel):
    """
    Standard output returned by every AI Agent.
    """

    agent_name: str

    success: bool

    result: dict

    execution_time: float