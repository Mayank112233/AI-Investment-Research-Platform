"""
Investment Graph

Defines the LangGraph workflow for the AI Investment Research Platform.
"""

from langgraph.graph import START, END, StateGraph

from graph.state import GraphState

from graph.nodes import (
    financial_node,
    news_node,
    technical_node,
    valuation_node,
    risk_node,
    committee_node,
    portfolio_node,
)


class InvestmentGraph:
    """
    Builds and compiles the investment analysis workflow.
    """

    def __init__(self) -> None:
        self.builder = StateGraph(GraphState)
        self._build_graph()

    # =====================================================
    # Build Workflow
    # =====================================================

    def _build_graph(self) -> None:
        """
        Register nodes and connect the workflow.
        """

        # -------------------------------------------------
        # Register Nodes
        # -------------------------------------------------

        self.builder.add_node(
            "financial",
            financial_node,
        )

        self.builder.add_node(
            "news",
            news_node,
        )

        self.builder.add_node(
            "technical",
            technical_node,
        )

        self.builder.add_node(
            "valuation",
            valuation_node,
        )

        self.builder.add_node(
            "risk",
            risk_node,
        )

        self.builder.add_node(
            "committee",
            committee_node,
        )

        self.builder.add_node(
            "portfolio",
            portfolio_node,
        )

        # -------------------------------------------------
        # Workflow
        # -------------------------------------------------

        self.builder.add_edge(
            START,
            "financial",
        )

        self.builder.add_edge(
            "financial",
            "news",
        )

        self.builder.add_edge(
            "news",
            "technical",
        )

        self.builder.add_edge(
            "technical",
            "valuation",
        )

        self.builder.add_edge(
            "valuation",
            "risk",
        )

        self.builder.add_edge(
            "risk",
            "committee",
        )

        self.builder.add_edge(
            "committee",
            "portfolio",
        )

        self.builder.add_edge(
            "portfolio",
            END,
        )

    # =====================================================
    # Compile Graph
    # =====================================================

    def compile(self):
        """
        Compile the LangGraph workflow.
        """

        return self.builder.compile()