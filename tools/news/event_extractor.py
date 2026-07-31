"""
Event Extractor Tool

Extracts important business events from analyzed news articles.
"""

from typing import List

from llm.service import LLMService
from schemas.news_output import NewsItem


class EventExtractorTool:
    """
    Uses the LLM to identify important business events
    from company news.
    """

    def __init__(self, llm: LLMService):
        self.llm = llm

    def execute(
        self,
        articles: List[NewsItem],
    ) -> List[str]:
        """
        Extract key business events from analyzed news.
        """

        article_text = ""

        for article in articles:

            article_text += f"""
Title:
{article.title}

Summary:
{article.summary}

Sentiment:
{article.sentiment}

Impact:
{article.impact}

------------------------------------
"""

        prompt = f"""
You are an investment research analyst.

Analyze the following company news.

Identify only major business events.

Possible event categories include:

- Earnings Report
- Product Launch
- Acquisition
- Merger
- Partnership
- CEO Change
- CFO Change
- Regulatory Investigation
- Legal Issue
- Dividend Announcement
- Share Buyback
- Stock Split
- AI Initiative
- Expansion
- Cost Reduction
- Layoffs
- Supply Chain Issue

Return only a Python list.

Example:

[
    "AI Product Launch",
    "Strategic Partnership",
    "Dividend Announcement"
]

News:

{article_text}
"""

        events = self.llm.generate(prompt)

        if isinstance(events, list):
            return events

        return []