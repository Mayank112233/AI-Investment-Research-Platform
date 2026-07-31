from pprint import pprint

from agents.committee.committee_agent import CommitteeAgent
from agents.news.news_agent import NewsAgent
from agents.portfolio.portfolio_agent import PortfolioAgent
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

    state = FinancialAgent(llm, registry).run(state)
    state = NewsAgent(llm, registry).run(state)
    state = TechnicalAgent(llm, registry).run(state)
    state = ValuationAgent(llm, registry).run(state)
    state = RiskAgent(llm, registry).run(state)
    state = CommitteeAgent(llm, registry).run(state)
    state = PortfolioAgent(llm, registry).run(state)

    pprint(
        state["portfolio_analysis"].model_dump(),
        sort_dicts=False,
    )


if __name__ == "__main__":
    main()