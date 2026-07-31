"""
Market Capitalization Tool

Retrieves market capitalization information
for a publicly traded company.
"""

from typing import Any, Dict

import yfinance as yf

from tools.base_tool import BaseTool


class MarketCapTool(BaseTool):
    """
    Fetches market capitalization data from Yahoo Finance.
    """

    @property
    def name(self) -> str:
        return "market_cap_tool"

    @property
    def description(self) -> str:
        return (
            "Returns company market capitalization information."
        )

    def execute(
        self,
        ticker: str,
    ) -> Dict[str, Any]:
        """
        Fetch market capitalization data.

        Args:
            ticker: Stock ticker symbol.

        Returns:
            Dictionary containing market capitalization metrics.
        """

        if not ticker:
            raise ValueError("Ticker symbol is required.")

        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            if not info:
                raise ValueError(
                    f"No market data found for '{ticker}'."
                )

            return {
                "market_cap": info.get("marketCap"),
                "shares_outstanding": info.get("sharesOutstanding"),
                "currency": info.get("currency"),
            }

        except Exception as exc:
            raise RuntimeError(
                f"Failed to fetch market capitalization for '{ticker}'."
            ) from exc
        