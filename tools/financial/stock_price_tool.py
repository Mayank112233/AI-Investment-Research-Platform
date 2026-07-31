"""
Stock Price Tool

Fetches the latest stock market information
using yfinance.
"""

from typing import Any, Dict

import yfinance as yf

from tools.base_tool import BaseTool


class StockPriceTool(BaseTool):
    """
    Retrieves stock price information from Yahoo Finance.
    """

    @property
    def name(self) -> str:
        return "stock_price_tool"

    @property
    def description(self) -> str:
        return (
            "Returns current stock market information."
        )

    def execute(
        self,
        ticker: str,
    ) -> Dict[str, Any]:
        """
        Fetch current stock market data.

        Args:
            ticker: Stock ticker symbol.

        Returns:
            Dictionary containing stock price information.
        """

        if not ticker:
            raise ValueError("Ticker symbol is required.")

        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            if not info:
                raise ValueError(
                    f"No stock data found for '{ticker}'."
                )

            return {
                "current_price": info.get("currentPrice"),
                "previous_close": info.get("previousClose"),
                "open_price": info.get("open"),
                "day_high": info.get("dayHigh"),
                "day_low": info.get("dayLow"),
                "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
                "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
                "volume": info.get("volume"),
                "average_volume": info.get("averageVolume"),
                "currency": info.get("currency"),
                "exchange": info.get("exchange"),
            }

        except Exception as exc:
            raise RuntimeError(
                f"Failed to fetch stock price data for '{ticker}'."
            ) from exc
        