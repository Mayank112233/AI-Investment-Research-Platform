"""
Portfolio Tool

Aggregates all information required by the
Portfolio Agent.
"""

from datetime import datetime
from typing import Any, Dict

from tools.base_tool import BaseTool


class PortfolioTool(BaseTool):
    """
    Collects all required workflow outputs and investor
    information for portfolio construction.
    """

    name = "portfolio_tool"

    description = (
        "Aggregates investment committee decision and "
        "workflow outputs for portfolio recommendation."
    )

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------

    def execute(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Build portfolio context.
        """

        self._validate_state(state)

        return {

            # -------------------------------------------------
            # Company
            # -------------------------------------------------

            "company": {
                "name": state["company_name"],
                "ticker": state["ticker"],
            },

            # -------------------------------------------------
            # Investor Profile
            # -------------------------------------------------

            "investment": {
                "period": state["investment_period"],
                "risk_tolerance": state["risk_tolerance"],
            },

            # -------------------------------------------------
            # Committee Decision
            # -------------------------------------------------

            "committee": state["committee_decision"],

            # -------------------------------------------------
            # Previous Analyses
            # -------------------------------------------------

            "analysis": {

                "financial": state["financial_analysis"],

                "news": state["news_analysis"],

                "technical": state["technical_analysis"],

                "valuation": state["valuation_analysis"],

                "risk": state["risk_analysis"],
            },

            # -------------------------------------------------
            # Metadata
            # -------------------------------------------------

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
        Validate workflow before portfolio generation.
        """

        required_fields = {

            "company_name": "Company Name",

            "ticker": "Ticker",

            "investment_period": "Investment Period",

            "risk_tolerance": "Risk Tolerance",

            "financial_analysis": "Financial Analysis",

            "news_analysis": "News Analysis",

            "technical_analysis": "Technical Analysis",

            "valuation_analysis": "Valuation Analysis",

            "risk_analysis": "Risk Analysis",

            "committee_decision": "Committee Decision",
        }

        for field, label in required_fields.items():

            if state.get(field) is None:

                raise ValueError(
                    f"{label} is missing from GraphState."
                )
            

            