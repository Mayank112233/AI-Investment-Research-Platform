"""
Graph Nodes

Each node is responsible for orchestrating a single AI Agent.
"""

from typing import Tuple, Type

from graph.state import GraphState

# =====================================================
# Agents
# =====================================================

from agents.technology.financial_agent import FinancialAgent
from agents.news.news_agent import NewsAgent
from agents.technology.technical_agent import TechnicalAgent
from agents.valuation.valuation_agent import ValuationAgent
from agents.risk.risk_agent import RiskAgent
from agents.committee.committee_agent import CommitteeAgent
from agents.portfolio.portfolio_agent import PortfolioAgent

# =====================================================
# LLM
# =====================================================

from llm.factory import ProviderFactory
from llm.service import LLMService

# =====================================================
# Tool Registry
# =====================================================

from tools.registry import ToolRegistry


# =====================================================
# Shared Dependency Builder
# =====================================================

def _build_dependencies() -> Tuple[LLMService, ToolRegistry]:
    """
    Create shared dependencies required by agents.
    """

    provider = ProviderFactory.create("openai")

    llm = LLMService(provider)

    registry = ToolRegistry()

    return llm, registry


# =====================================================
# Generic Agent Runner
# =====================================================

def _run_agent(
    state: GraphState,
    agent_cls: Type,
    node_name: str,
) -> GraphState:
    """
    Generic helper for executing an AI agent.
    """

    print("\n" + "=" * 60)
    print(f"Running {node_name.replace('_', ' ').title()}")
    print("=" * 60)

    state["current_node"] = node_name

    try:

        llm, registry = _build_dependencies()

        agent = agent_cls(
            llm_service=llm,
            tool_registry=registry,
        )

        state = agent.run(state)

        state["completed_nodes"].append(node_name)

        print(f"✓ {node_name} completed successfully.")

    except Exception as e:

        error_message = f"{node_name}: {str(e)}"

        state["errors"].append(error_message)

        print(f"✗ {error_message}")

    return state


# =====================================================
# Financial Node
# =====================================================

def financial_node(state: GraphState) -> GraphState:
    """
    Execute the Financial Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=FinancialAgent,
        node_name="financial_agent",
    )


# =====================================================
# News Node
# =====================================================

def news_node(state: GraphState) -> GraphState:
    """
    Execute the News Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=NewsAgent,
        node_name="news_agent",
    )


# =====================================================
# Technical Node
# =====================================================

def technical_node(state: GraphState) -> GraphState:
    """
    Execute the Technical Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=TechnicalAgent,
        node_name="technical_agent",
    )


# =====================================================
# Valuation Node
# =====================================================

def valuation_node(state: GraphState) -> GraphState:
    """
    Execute the Valuation Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=ValuationAgent,
        node_name="valuation_agent",
    )


# =====================================================
# Risk Node
# =====================================================

def risk_node(state: GraphState) -> GraphState:
    """
    Execute the Risk Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=RiskAgent,
        node_name="risk_agent",
    )


# =====================================================
# Committee Node
# =====================================================

def committee_node(state: GraphState) -> GraphState:
    """
    Execute the Committee Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=CommitteeAgent,
        node_name="committee_agent",
    )


# =====================================================
# Portfolio Node
# =====================================================

def portfolio_node(state: GraphState) -> GraphState:
    """
    Execute the Portfolio Agent.
    """

    return _run_agent(
        state=state,
        agent_cls=PortfolioAgent,
        node_name="portfolio_agent",
    )