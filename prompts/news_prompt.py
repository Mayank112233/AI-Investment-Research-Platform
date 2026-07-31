"""
News Prompt Builder

Builds the prompt for the News Agent.
"""

from schemas.news_output import NewsItem


class NewsPromptBuilder:
    """
    Builds prompts for the News Agent.
    """

    @staticmethod
    def build(
        company_name: str,
        ticker: str,
        articles: list[NewsItem],
        key_events: list[str],
    ) -> str:
        """
        Build the News Agent prompt.
        """

        article_section = ""

        for index, article in enumerate(articles, start=1):

            article_section += f"""
==================================================
Article {index}

Title:
{article.title}

Summary:
{article.summary}

Sentiment:
{article.sentiment}

Business Impact:
{article.impact}

Source:
{article.source}

==================================================
"""

        event_section = "\n".join(
            f"- {event}"
            for event in key_events
        )

        prompt = f"""
You are a Senior Investment Research Analyst.

Your task is to analyze recent news for the company.

--------------------------------------------------
Company Information
--------------------------------------------------

Company Name:
{company_name}

Ticker:
{ticker}

--------------------------------------------------
Recent News
--------------------------------------------------

{article_section}

--------------------------------------------------
Major Business Events
--------------------------------------------------

{event_section}

--------------------------------------------------
Instructions
--------------------------------------------------

Analyze the company's recent news and provide:

1. Overall Market Sentiment

2. Confidence Score
   (0.0 - 1.0)

3. Key Business Events

4. Opportunities

5. Risks

6. Final Summary

Focus on:

• Revenue impact

• Growth opportunities

• Risks

• Competitive advantages

• Regulatory concerns

• Product launches

• Partnerships

• Acquisitions

• Management changes

Return ONLY the structured response.
"""

        return prompt