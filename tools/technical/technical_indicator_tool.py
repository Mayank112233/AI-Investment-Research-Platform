"""
Technical Indicator Tool

Calculates technical indicators used by the Technical Agent.
"""

from typing import Dict

import pandas as pd
import yfinance as yf

from tools.base_tool import BaseTool


class TechnicalIndicatorTool(BaseTool):
    """
    Fetches historical market data and calculates
    technical indicators.
    """

    name = "technical_indicator_tool"

    description = (
        "Calculates EMA, RSI, Bollinger Bands and "
        "Volume Trend for a stock."
    )

    def execute(
        self,
        ticker: str,
        period: str = "6mo",
    ) -> Dict:

        stock = yf.Ticker(ticker)

        df = stock.history(period=period)

        if df.empty:
            raise ValueError(f"No market data found for {ticker}")

        close = df["Close"]

        volume = df["Volume"]

        # -------------------------
        # EMA
        # -------------------------

        ema20 = close.ewm(
            span=20,
            adjust=False,
        ).mean()

        ema50 = close.ewm(
            span=50,
            adjust=False,
        ).mean()

        # -------------------------
        # RSI
        # -------------------------

        delta = close.diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()

        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        # -------------------------
        # Bollinger Bands
        # -------------------------

        sma20 = close.rolling(20).mean()

        std20 = close.rolling(20).std()

        upper_band = sma20 + (2 * std20)

        lower_band = sma20 - (2 * std20)

        # -------------------------
        # Volume Trend
        # -------------------------

        volume_ma20 = volume.rolling(20).mean()

        current_volume = float(volume.iloc[-1])

        average_volume = float(volume_ma20.iloc[-1])

        if current_volume > average_volume:
            volume_trend = "Increasing"
        elif current_volume < average_volume:
            volume_trend = "Decreasing"
        else:
            volume_trend = "Neutral"

        # -------------------------
        # Current Price
        # -------------------------

        current_price = float(close.iloc[-1])

        # -------------------------
        # Return
        # -------------------------

        return {

            "current_price": current_price,

            "ema20": float(ema20.iloc[-1]),

            "ema50": float(ema50.iloc[-1]),

            "rsi": float(rsi.iloc[-1]),

            "bollinger_upper": float(
                upper_band.iloc[-1]
            ),

            "bollinger_lower": float(
                lower_band.iloc[-1]
            ),

            "volume_trend": volume_trend,
        }