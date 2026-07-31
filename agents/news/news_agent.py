"""
News Agent

Responsible for analyzing recent company news.
"""

from agents.base_agent import BaseAgent

from graph.state import GraphState

from schemas.news_output import NewsAnalysisOutput

from prompts.news_prompt import NewsPromptBuilder

from tools.news.news_tool import NewsTool
from tools.news.sentiment_tool import SentimentTool
from tools.news.event_extractor import EventExtractorTool


class NewsAgent(BaseAgent):
    """
    News Analysis Agent.
    """

    def __init__(self, llm_service, tool_registry):
        super().__init__(llm_service, tool_registry)

    def collect_data(
        self,
        state: GraphState,
    ):
        """
        Collect recent company news.
        """

        ticker = state["ticker"]

        company_name = state["company_name"]

        news_tool = self.tools.get_tool(
            "news_tool"
        )

        sentiment_tool = SentimentTool(self.llm)

        event_tool = EventExtractorTool(self.llm)

        articles = news_tool.execute(ticker)

        analyzed_articles = sentiment_tool.execute(
            articles
        )

        key_events = event_tool.execute(
            analyzed_articles
        )

        return {
            "company_name": company_name,
            "ticker": ticker,
            "articles": analyzed_articles,
            "events": key_events,
        }

    def validate_data(
        self,
        data,
    ):
        """
        Validate collected news.
        """

        if len(data["articles"]) == 0:
            raise ValueError(
                "No news articles found."
            )

        return data

    def build_prompt(
        self,
        data,
    ):
        """
        Build News Prompt.
        """

        return NewsPromptBuilder.build(
            company_name=data["company_name"],
            ticker=data["ticker"],
            articles=data["articles"],
            key_events=data["events"],
        )

    def output_schema(self):
        """
        Expected output schema.
        """

        return NewsAnalysisOutput

    def update_state(
        self,
        state: GraphState,
        result: NewsAnalysisOutput,
    ):
        """
        Update Graph State.
        """

        state["news_analysis"] = result

        return state