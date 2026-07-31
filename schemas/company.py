"""
Company Data Model

This schema represents a publicly listed company.
"""

from pydantic import BaseModel


class Company(BaseModel):
    """
    Company information returned by the Company Search Tool.
    """

    name: str

    ticker: str

    industry: str

    sector: str

    country: str

    exchange: str