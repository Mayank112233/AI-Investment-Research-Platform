"""
Test Committee Agent

Run:

python -m test.test_committee_agent
"""

from pprint import pprint

from agents.committee.committee_agent import CommitteeAgent
from agents.news.news_agent import NewsAgent
from agents.risk.risk_agent import RiskAgent
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
    state = FinancialAgent(llm, registry).run(state)

    print("=" * 60)
    print("RUNNING NEWS AGENT")
    print("=" * 60)
    state = NewsAgent(llm, registry).run(state)

    print("=" * 60)
    print("RUNNING TECHNICAL AGENT")
    print("=" * 60)
    state = TechnicalAgent(llm, registry).run(state)

    print("=" * 60)
    print("RUNNING VALUATION AGENT")
    print("=" * 60)
    state = ValuationAgent(llm, registry).run(state)

    print("=" * 60)
    print("RUNNING RISK AGENT")
    print("=" * 60)
    state = RiskAgent(llm, registry).run(state)

    print("=" * 60)
    print("RUNNING COMMITTEE AGENT")
    print("=" * 60)
    state = CommitteeAgent(llm, registry).run(state)

    print()
    print("=" * 60)
    print("COMMITTEE DECISION")
    print("=" * 60)

    pprint(
        state["committee_decision"].model_dump(),
        sort_dicts=False,
    )


if __name__ == "__main__":
    print("Starting Committee Agent Test...\n")
    main()
    print("\nCommittee Agent Test Completed Successfully!")