"""
Sentiment Tool

Analyzes sentiment of company news articles using the configured LLM.
"""

from typing import List

from llm.service import LLMService
from schemas.news_output import NewsItem


class SentimentTool:
    """
    Uses the LLM to determine the sentiment
    of each news article.
    """

    def __init__(self, llm: LLMService):
        self.llm = llm

    def execute(
        self,
        articles: List[dict],
    ) -> List[NewsItem]:
        """
        Analyze each article and assign sentiment.
        """

        analyzed_articles: List[NewsItem] = []

        for article in articles:

            # ----------------------------------------
            # Safely extract article information
            # ----------------------------------------

            title = article.get("title") or ""
            summary = article.get("summary") or ""

            publisher = article.get("publisher")

            # Handle publisher if it is a dictionary
            if isinstance(publisher, dict):
                publisher = (
                    publisher.get("displayName")
                    or publisher.get("name")
                    or publisher.get("publisher")
                    or "Unknown Source"
                )

            publisher = str(publisher) if publisher else "Unknown Source"

            # Skip invalid articles
            if not title.strip():
                continue

            prompt = f"""
You are a financial news analyst.

Analyze the following news article.

Title:
{title}

Summary:
{summary}

Return ONLY in the following format:

Sentiment:
(Positive / Neutral / Negative)

Business Impact:
(1-2 concise sentences)
"""

            response = self.llm.generate(prompt)

            # Ensure response is a string
            response = str(response).strip()

            analyzed_articles.append(
                NewsItem(
                    title=title,
                    summary=summary,
                    sentiment=response,
                    impact=response,
                    source=publisher,
                )
            )

        return analyzed_articles