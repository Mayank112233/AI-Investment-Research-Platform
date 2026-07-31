"""
Test Valuation Agent

Run:

python -m test.test_valuation_agent
"""

from pprint import pprint

from agents.news.news_agent import NewsAgent
from agents.technology.financial_agent import FinancialAgent
from agents.technology.technical_agent import TechnicalAgent
from agents.valuation.valuation_agent import ValuationAgent

from llm.providers.openai_provider import OpenAIProvider
from llm.service import LLMService
from tools.registry import ToolRegistry


def main():

    provider = OpenAIProvider()
    llm = LLMService(provider)
    registry = ToolRegistry()

    state = {
        "company_name": "Apple Inc.",
        "ticker": "AAPL",
        "investment_period": "5 Years",
        "risk_tolerance": "Moderate",
    }

    print("=" * 60)
    print("RUNNING FINANCIAL AGENT")
    print("=" * 60)

    financial = FinancialAgent(llm, registry)
    state = financial.run(state)

    print("=" * 60)
    print("RUNNING NEWS AGENT")
    print("=" * 60)

    news = NewsAgent(llm, registry)
    state = news.run(state)

    print("=" * 60)
    print("RUNNING TECHNICAL AGENT")
    print("=" * 60)

    technical = TechnicalAgent(llm, registry)
    state = technical.run(state)

    print("=" * 60)
    print("RUNNING VALUATION AGENT")
    print("=" * 60)

    valuation = ValuationAgent(llm, registry)
    state = valuation.run(state)

    print()
    print("=" * 60)
    print("VALUATION ANALYSIS")
    print("=" * 60)

    pprint(
        state["valuation_analysis"].model_dump(),
        sort_dicts=False,
    )


if __name__ == "__main__":
    main()