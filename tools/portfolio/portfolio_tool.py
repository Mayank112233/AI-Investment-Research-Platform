"""
Portfolio Tool

Collects all information required by the Portfolio Agent.
"""

from datetime import datetime
from typing import Any, Dict

from tools.base_tool import BaseTool


class PortfolioTool(BaseTool):
    """
    Aggregates all analyses and committee decision into a
    single payload for the Portfolio Agent.
    """

    @property
    def name(self) -> str:
        return "portfolio_tool"

    @property
    def description(self) -> str:
        return (
            "Collects committee decision and all supporting "
            "analyses for portfolio recommendation."
        )

    def execute(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Build the Portfolio Agent input.
        """

        required_fields = [
            "company_name",
            "ticker",
            "investment_period",
            "risk_tolerance",
            "financial_analysis",
            "news_analysis",
            "technical_analysis",
            "valuation_analysis",
            "risk_analysis",
            "committee_decision",
        ]

        missing = [
            field
            for field in required_fields
            if state.get(field) is None
        ]

        if missing:
            raise ValueError(
                "Portfolio Tool missing required fields: "
                + ", ".join(missing)
            )

        return {
            "company": {
                "name": state["company_name"],
                "ticker": state["ticker"],
            },
            "investment": {
                "period": state["investment_period"],
                "risk_tolerance": state["risk_tolerance"],
            },
            "committee": state["committee_decision"],
            "analysis": {
                "financial": state["financial_analysis"],
                "news": state["news_analysis"],
                "technical": state["technical_analysis"],
                "valuation": state["valuation_analysis"],
                "risk": state["risk_analysis"],
            },
            "generated_at": datetime.utcnow().isoformat(),
        }