"""
Valuation Tool

Aggregates outputs from previous agents for valuation analysis.
"""

from datetime import datetime
from typing import Any, Dict

from tools.base_tool import BaseTool


class ValuationTool(BaseTool):
    """
    Aggregates outputs from previous agents and prepares
    a structured context for the Valuation Agent.
    """

    name = "valuation_tool"

    description = (
        "Aggregates financial, news and technical "
        "analysis for valuation."
    )

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------

    def execute(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Build the valuation context.
        """

        self._validate_state(state)

        return {

            # -------------------------------------------------
            # Company Information
            # -------------------------------------------------

            "company": {
                "name": state["company_name"],
                "ticker": state["ticker"],
            },

            # -------------------------------------------------
            # User Preferences
            # -------------------------------------------------

            "investment": {
                "period": state["investment_period"],
                "risk_tolerance": state["risk_tolerance"],
            },

            # -------------------------------------------------
            # Previous Agent Outputs
            # -------------------------------------------------

            "analysis": {

                "financial": state["financial_analysis"],

                "news": state["news_analysis"],

                "technical": state["technical_analysis"],
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
        Validate required information before aggregation.
        """

        required_fields = {

            "company_name": "Company name",

            "ticker": "Ticker",

            "investment_period": "Investment period",

            "risk_tolerance": "Risk tolerance",

            "financial_analysis": "Financial analysis",

            "news_analysis": "News analysis",

            "technical_analysis": "Technical analysis",
        }

        for field, label in required_fields.items():

            if state.get(field) is None:

                raise ValueError(
                    f"{label} is missing from workflow state."
                )