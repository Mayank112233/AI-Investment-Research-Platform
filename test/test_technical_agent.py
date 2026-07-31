"""
Test Technical Agent

Run:

python -m test.test_technical_agent
"""

from pprint import pprint

from agents.technology.technical_agent import TechnicalAgent
from llm.providers.openai_provider import OpenAIProvider
from llm.service import LLMService
from tools.registry import ToolRegistry


def main():
    """
    Test the Technical Agent independently.
    """

    # -----------------------------------------
    # Initialize LLM
    # -----------------------------------------

    provider = OpenAIProvider()
    llm = LLMService(provider)

    # -----------------------------------------
    # Initialize Tool Registry
    # -----------------------------------------

    registry = ToolRegistry()

    # -----------------------------------------
    # Initialize Agent
    # -----------------------------------------

    agent = TechnicalAgent(
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
    print("TECHNICAL ANALYSIS")
    print("=" * 60)

    pprint(
        result["technical_analysis"].model_dump(),
        sort_dicts=False,
    )


if __name__ == "__main__":
    main()