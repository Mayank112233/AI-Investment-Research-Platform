"""
News Tool

Fetches the latest news articles for a company
using yfinance.
"""

from typing import Any

import yfinance as yf

from tools.base_tool import BaseTool


class NewsTool(BaseTool):
    """
    Retrieves the latest news articles for a company.
    """

    @property
    def name(self) -> str:
        return "news_tool"

    @property
    def description(self) -> str:
        return "Fetches the latest company news."

    def execute(
        self,
        ticker: str,
        limit: int = 10,
    ) -> list[dict]:
        """
        Fetch latest company news.
        """

        stock = yf.Ticker(ticker)

        try:
            news_items = stock.news or []
        except Exception:
            return []

        articles: list[dict] = []

        for item in news_items[:limit]:

            # -----------------------------------------
            # Support both old and new yfinance formats
            # -----------------------------------------

            content: dict[str, Any] = item.get("content", item)

            title = (
                content.get("title")
                or item.get("title")
                or ""
            )

            publisher = (
                content.get("provider")
                or content.get("publisher")
                or item.get("publisher")
                or "Unknown Source"
            )

            summary = (
                content.get("summary")
                or item.get("summary")
                or ""
            )

            link = (
                content.get("canonicalUrl", {}).get("url")
                or content.get("clickThroughUrl", {}).get("url")
                or item.get("link")
                or ""
            )

            published = (
                content.get("pubDate")
                or item.get("providerPublishTime")
                or ""
            )

            # Skip invalid articles
            if not title:
                continue

            articles.append(
                {
                    "title": title,
                    "publisher": publisher,
                    "summary": summary,
                    "link": link,
                    "published": published,
                }
            )

        return articles
    