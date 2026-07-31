"""
Conditional Edge Functions

These functions decide which node should execute next
based on the current GraphState.
"""

from graph.state import GraphState


class ConditionalEdges:
    """
    Collection of routing decisions.
    """

    @staticmethod
    def after_financial(state: GraphState) -> str:
        """
        Decide where to go after Financial Agent.
        """

        financial = state.get("financial_data", {})

        revenue = financial.get("revenue", 0)

        if revenue <= 0:
            return "risk_agent"

        return "innovation_agent"

    @staticmethod
    def after_risk(state: GraphState) -> str:
        """
        Decide after Risk Agent.
        """

        risk_text = state.get("risk_analysis")

        if risk_text is None:
            return "consensus_agent"

        risk_text = risk_text.lower()

        if "high risk" in risk_text:
            return "consensus_agent"

        return "consensus_agent"

    @staticmethod
    def after_consensus(state: GraphState) -> str:
        """
        Decide after Consensus Agent.
        """

        return "portfolio_agent"