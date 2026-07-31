"""
Financial Schemas

Defines strongly typed models used by the Financial Agent.
"""

from typing import Optional

from pydantic import BaseModel


class StockInformation(BaseModel):
    current_price: Optional[float] = None
    previous_close: Optional[float] = None
    day_high: Optional[float] = None
    day_low: Optional[float] = None


class MarketInformation(BaseModel):
    market_cap: Optional[float] = None
    shares_outstanding: Optional[int] = None
    currency: Optional[str] = None


class FinancialRatios(BaseModel):
    pe_ratio: Optional[float] = None
    profit_margin: Optional[float] = None
    debt_to_equity: Optional[float] = None


class FinancialAnalysisInput(BaseModel):
    ticker: str

    financial_statement: dict

    stock_information: StockInformation

    market_information: MarketInformation

    ratios: FinancialRatios