"""
Risk Agent
"""

from typing import Any, Dict, Type

from agents.base_agent import BaseAgent
from prompts.risk_prompt import RiskPromptBuilder
from schemas.risk_output import RiskAnalysisOutput


class RiskAgent(BaseAgent):
    """
    Evaluates the overall investment risk by combining
    previous agent analyses.
    """

    TOOL_NAME = "risk_tool"

    # -----------------------------------------------------
    # Collect Data
    # -----------------------------------------------------

    def collect_data(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Collect data required for risk analysis.
        """

        tool = self.tools.get_tool(self.TOOL_NAME)

        if tool is None:
            raise ValueError(
                f"{self.TOOL_NAME} is not registered."
            )

        data = tool.execute(state)

        if not isinstance(data, dict):
            raise ValueError(
                "Risk tool must return a dictionary."
            )

        return data

    # -----------------------------------------------------
    # Validate Data
    # -----------------------------------------------------

    def validate_data(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Validate risk analysis context.
        """

        required_sections = (
            "company",
            "investment",
            "analysis",
        )

        for section in required_sections:
            if section not in data or not data[section]:
                raise ValueError(
                    f"Missing required section: {section}"
                )

        return data

    # -----------------------------------------------------
    # Prompt Builder
    # -----------------------------------------------------

    def build_prompt(
        self,
        data: Dict[str, Any],
    ) -> str:
        """
        Build the risk analysis prompt.
        """

        return RiskPromptBuilder.build(data)

    # -----------------------------------------------------
    # Output Schema
    # -----------------------------------------------------

    def output_schema(
        self,
    ) -> Type[RiskAnalysisOutput]:
        """
        Structured output schema.
        """

        return RiskAnalysisOutput

    # -----------------------------------------------------
    # Update Graph State
    # -----------------------------------------------------

    def update_state(
        self,
        state: Dict[str, Any],
        result: RiskAnalysisOutput,
    ) -> Dict[str, Any]:
        """
        Store risk analysis.
        """

        state["risk_analysis"] = result

        return state