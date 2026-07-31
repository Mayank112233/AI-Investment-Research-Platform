"""
Risk Tool

Aggregates outputs from previous agents for risk analysis.
"""

from datetime import datetime
from typing import Any, Dict

from tools.base_tool import BaseTool


class RiskTool(BaseTool):
    """
    Aggregates outputs from previous agents and prepares
    a structured context for the Risk Agent.
    """

    name = "risk_tool"

    description = (
        "Aggregates financial, news, technical and "
        "valuation analyses for risk assessment."
    )

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------

    def execute(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Build the risk analysis context.
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
            # Investor Profile
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

                "valuation": state["valuation_analysis"],
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
        Validate required workflow state.
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
        }

        for field, label in required_fields.items():

            if state.get(field) is None:

                raise ValueError(
                    f"{label} is missing from workflow state."
                )