"""
News Input Schemas

Defines the structured input used by the News Agent.
"""

from typing import List

from pydantic import BaseModel

from schemas.news_output import NewsItem


class NewsAnalysisInput(BaseModel):
    """
    Input collected before sending to the LLM.
    """

    company_name: str

    ticker: str

    articles: List[NewsItem]

    events: List[str]