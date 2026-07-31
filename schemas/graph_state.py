"""
LangGraph State Schema
"""

from typing import Optional

from pydantic import BaseModel


class GraphState(BaseModel):
    """
    Shared state passed between LangGraph nodes.
    """

    company: Optional[str] = None

    ticker: Optional[str] = None

    industry: Optional[str] = None

    investment_horizon: Optional[str] = None

    risk_level: Optional[str] = None

    recommendation: Optional[str] = None

    confidence: Optional[float] = None