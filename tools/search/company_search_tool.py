"""
Company Search Tool

Fetches company profile information using Yahoo Finance.
"""

import yfinance as yf

from schemas.company import Company
from tools.base_tool import BaseTool


class CompanySearchTool(BaseTool):

    @property
    def name(self):
        return "company_search"

    @property
    def description(self):
        return "Search company information."

    def execute(self, company: str) -> Company:

        ticker = yf.Ticker(company)

        info = ticker.info

        return Company(
            name=info.get("longName", company),
            ticker=info.get("symbol", ""),
            industry=info.get("industry", ""),
            sector=info.get("sector", ""),
            country=info.get("country", ""),
            exchange=info.get("exchange", ""),
        )