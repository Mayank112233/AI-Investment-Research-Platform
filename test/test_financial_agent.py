from graph.state import GraphState
from agents.technology.financial_agent import FinancialAgent
from llm.factory import ProviderFactory
from llm.service import LLMService
from tools.registry import ToolRegistry


def main():

    state: GraphState = {
        "company_name": "Apple Inc.",
        "ticker": "AAPL",
        "investment_period": "5 years",
        "risk_tolerance": "Moderate",

        "financial_data": {},
        "stock_data": {},
        "news_data": [],
        "technical_data": {},

        "financial_analysis": None,
        "news_analysis": None,
        "technical_analysis": None,
        "valuation_analysis": None,
        "risk_analysis": None,
        "committee_decision": None,
        "portfolio_recommendation": None,

        "completed_nodes": [],
        "current_node": None,
        "errors": [],
    }

    provider = ProviderFactory.create("openai")

    llm = LLMService(provider)

    registry = ToolRegistry()

    agent = FinancialAgent(
        llm_service=llm,
        tool_registry=registry,
    )

    result = agent.run(state)

    print("\n")
    print("=" * 60)
    print("FINANCIAL ANALYSIS")
    print("=" * 60)
    print(result["financial_analysis"])


if __name__ == "__main__":
    main()