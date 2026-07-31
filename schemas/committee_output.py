"""
Committee Decision Output Schema
"""

from pydantic import BaseModel, Field


class CommitteeDecisionOutput(BaseModel):
    """
    Final investment committee decision.
    """

    decision: str = Field(
        ...,
        description="Final investment decision (BUY, HOLD, SELL)."
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=100,
        description="Confidence score between 0 and 100."
    )

    investment_thesis: str = Field(
        ...,
        description="Primary reasoning supporting the decision."
    )

    supporting_factors: list[str] = Field(
        ...,
        description="Key factors supporting the decision."
    )

    major_concerns: list[str] = Field(
        ...,
        description="Primary concerns or risks."
    )

    decision_conditions: list[str] = Field(
        ...,
        description="Events that could change the committee's decision."
    )

    executive_summary: str = Field(
        ...,
        description="Concise summary for executives."
    )
    