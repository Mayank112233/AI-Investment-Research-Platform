"""
Investment Report Schema
"""

from pydantic import BaseModel


class InvestmentReport(BaseModel):
    """
    Final report generated for the user.
    """

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    opportunities: list[str]

    threats: list[str]

    recommendation: str