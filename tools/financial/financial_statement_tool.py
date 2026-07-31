"""
Financial Statement Tool

Fetches key financial statement data for a company
using yfinance.
"""

from typing import Any, Dict

import yfinance as yf

from tools.base_tool import BaseTool


class FinancialStatementTool(BaseTool):
    """
    Retrieves financial statement information from Yahoo Finance.
    """

    @property
    def name(self) -> str:
        return "financial_statement_tool"

    @property
    def description(self) -> str:
        return (
            "Returns key financial statement metrics for a company."
        )

    def execute(
        self,
        ticker: str,
    ) -> Dict[str, Any]:
        """
        Fetch financial statement data.

        Args:
            ticker: Stock ticker symbol (e.g., AAPL, MSFT)

        Returns:
            Dictionary containing financial statement metrics.
        """

        if not ticker:
            raise ValueError("Ticker symbol is required.")

        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            if not info:
                raise ValueError(
                    f"No financial data found for ticker '{ticker}'."
                )

            return {
                "revenue": info.get("totalRevenue"),
                "net_income": info.get("netIncomeToCommon"),
                "gross_profit": info.get("grossProfits"),
                "operating_margin": info.get("operatingMargins"),
                "profit_margin": info.get("profitMargins"),
                "eps": info.get("trailingEps"),
                "book_value": info.get("bookValue"),
                "debt_to_equity": info.get("debtToEquity"),
                "return_on_equity": info.get("returnOnEquity"),
                "return_on_assets": info.get("returnOnAssets"),
                "current_ratio": info.get("currentRatio"),
                "quick_ratio": info.get("quickRatio"),
                "free_cashflow": info.get("freeCashflow"),
                "operating_cashflow": info.get("operatingCashflow"),
            }

        except Exception as exc:
            raise RuntimeError(
                f"Failed to fetch financial statements for '{ticker}'."
            ) from exc