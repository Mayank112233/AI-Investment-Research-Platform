"""
Committee Tool

Aggregates outputs from previous agents for the
Investment Committee.
"""

from datetime import datetime
from typing import Any, Dict

from tools.base_tool import BaseTool


class CommitteeTool(BaseTool):
    """
    Aggregates previous analyses into a structured
    context for the Committee Agent.
    """

    name = "committee_tool"

    description = (
        "Aggregates financial, news, technical, "
        "valuation and risk analyses for the "
        "Investment Committee."
    )

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------

    def execute(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Build committee context.
        """

        self._validate_state(state)

        return {

            # ---------------------------------------------
            # Company Information
            # ---------------------------------------------

            "company": {
                "name": state["company_name"],
                "ticker": state["ticker"],
            },

            # ---------------------------------------------
            # Investor Profile
            # ---------------------------------------------

            "investment": {
                "period": state["investment_period"],
                "risk_tolerance": state["risk_tolerance"],
            },

            # ---------------------------------------------
            # Previous Agent Outputs
            # ---------------------------------------------

            "analysis": {

                "financial": state["financial_analysis"],

                "news": state["news_analysis"],

                "technical": state["technical_analysis"],

                "valuation": state["valuation_analysis"],

                "risk": state["risk_analysis"],
            },

            # ---------------------------------------------
            # Metadata
            # ---------------------------------------------

            "generated_at": datetime.utcnow().isoformat(),
        }

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    def _validate_state(
        self,
        state: Dict[str, Any],
    ) -> None:
        """
        Validate workflow state before committee review.
        """

        required_fields = {

            "company_name": "Company name",

            "ticker": "Ticker",

            "investment_period": "Investment period",

            "risk_tolerance": "Risk tolerance",

            "financial_analysis": "Financial analysis",

            "news_analysis": "News analysis",

            "technical_analysis": "Technical analysis",

            "valuation_analysis": "Valuation analysis",

            "risk_analysis": "Risk analysis",
        }

        for field, label in required_fields.items():

            if state.get(field) is None:

                raise ValueError(
                    f"{label} is missing from workflow state."
                )