"""
Portfolio Recommendation Output Schema
"""

from typing import List

from pydantic import BaseModel, Field


class PortfolioRecommendationOutput(BaseModel):
    """
    Final portfolio recommendation generated from
    the committee decision.
    """

    allocation_percentage: float = Field(
        ...,
        ge=0,
        le=100,
        description="Suggested allocation percentage."
    )

    recommendation: str = Field(
        ...,
        description="BUY, HOLD or SELL."
    )

    entry_strategy: str = Field(
        ...,
        description="Recommended entry strategy."
    )

    exit_strategy: str = Field(
        ...,
        description="Suggested exit strategy."
    )

    holding_period: str = Field(
        ...,
        description="Recommended holding period."
    )

    monitoring_frequency: str = Field(
        ...,
        description="How frequently the investment should be reviewed."
    )

    key_actions: List[str] = Field(
        ...,
        description="Immediate actions for the investor."
    )

    risk_management: List[str] = Field(
        ...,
        description="Risk management recommendations."
    )

    summary: str = Field(
        ...,
        description="Executive portfolio recommendation."
    )