"""
Test News Agent

Run:

python -m test.test_news_agent
"""

from pprint import pprint

from agents.news.news_agent import NewsAgent
from llm.service import LLMService
from tools.registry import ToolRegistry

from llm.providers.openai_provider import OpenAIProvider
from llm.service import LLMService




def main():
    """
    Test the News Agent independently.
    """

    # -----------------------------------------
    # Initialize Services
    # -----------------------------------------

    provider = OpenAIProvider()
    llm = LLMService(provider)

    registry = ToolRegistry()

    agent = NewsAgent(
        llm_service=llm,
        tool_registry=registry,
    )

    # -----------------------------------------
    # Test State
    # -----------------------------------------

    state = {
        "company_name": "Apple Inc.",
        "ticker": "AAPL",
        "investment_period": "5 Years",
        "risk_tolerance": "Moderate",
    }

    # -----------------------------------------
    # Run Agent
    # -----------------------------------------

    result = agent.run(state)

    print("\n")
    print("=" * 60)
    print("NEWS ANALYSIS")
    print("=" * 60)

    pprint(result["news_analysis"].model_dump())


if __name__ == "__main__":
    main()