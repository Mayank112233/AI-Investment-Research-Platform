"""
Valuation Agent
"""

from typing import Any, Dict, Type

from agents.base_agent import BaseAgent
from prompts.valuation_prompt import ValuationPromptBuilder
from schemas.valuation_output import ValuationAnalysisOutput


class ValuationAgent(BaseAgent):
    """
    Determines whether a company is undervalued,
    fairly valued, or overvalued by combining
    previous agent analyses.
    """

    TOOL_NAME = "valuation_tool"

    # -----------------------------------------------------
    # Collect Data
    # -----------------------------------------------------

    def collect_data(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Collect data required for valuation analysis.
        """

        tool = self.tools.get_tool(self.TOOL_NAME)

        if tool is None:
            raise ValueError(
                f"{self.TOOL_NAME} is not registered."
            )

        data = tool.execute(state)

        if not isinstance(data, dict):
            raise ValueError("Valuation tool must return a dictionary.")

        return data

    # -----------------------------------------------------
    # Validate Data
    # -----------------------------------------------------

    def validate_data(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Validate valuation context.
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
    # Build Prompt
    # -----------------------------------------------------

    def build_prompt(
        self,
        data: Dict[str, Any],
    ) -> str:
        """
        Build valuation prompt.
        """

        return ValuationPromptBuilder.build(data)

    # -----------------------------------------------------
    # Output Schema
    # -----------------------------------------------------

    def output_schema(
        self,
    ) -> Type[ValuationAnalysisOutput]:
        """
        Structured output schema.
        """

        return ValuationAnalysisOutput

    # -----------------------------------------------------
    # Update Graph State
    # -----------------------------------------------------

    def update_state(
        self,
        state: Dict[str, Any],
        result: ValuationAnalysisOutput,
    ) -> Dict[str, Any]:
        """
        Store valuation analysis.
        """

        state["valuation_analysis"] = result

        return state