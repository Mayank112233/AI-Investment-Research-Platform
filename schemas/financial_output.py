"""
Financial Agent Output Schema
"""

from typing import List
from pydantic import BaseModel


class FinancialAnalysisOutput(BaseModel):
    """
    Structured output produced by the Financial Agent.
    """

    summary: str

    strengths: List[str]

    risks: List[str]

    valuation: str

    recommendation: str

    confidence_score: float