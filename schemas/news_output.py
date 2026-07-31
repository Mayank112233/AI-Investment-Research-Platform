"""
News Analysis Output Schema

Structured output returned by the News Agent.
"""

from typing import List
from pydantic import BaseModel, Field


class NewsItem(BaseModel):
    """
    Individual news article.
    """

    title: str = Field(
        description="News headline."
    )

    summary: str = Field(
        description="Short summary of the news."
    )

    sentiment: str = Field(
        description="Positive, Neutral or Negative."
    )

    impact: str = Field(
        description="Expected impact on the company."
    )

    source: str = Field(
        description="News source."
    )


class NewsAnalysisOutput(BaseModel):
    """
    Final output of the News Agent.
    """

    overall_sentiment: str = Field(
        description="Overall market sentiment."
    )

    confidence_score: float = Field(
        ge=0,
        le=1,
        description="Confidence score."
    )

    key_events: List[str] = Field(
        description="Most important events."
    )

    opportunities: List[str] = Field(
        description="Potential opportunities."
    )

    risks: List[str] = Field(
        description="Potential risks."
    )

    articles: List[NewsItem] = Field(
        description="Processed news articles."
    )

    final_summary: str = Field(
        description="Overall conclusion."
    )