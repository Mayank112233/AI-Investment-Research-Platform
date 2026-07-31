"""
Portfolio Agent
"""

from typing import Any, Dict, Type

from agents.base_agent import BaseAgent
from prompts.portfolio_prompt import PortfolioPromptBuilder
from schemas.portfolio_output import PortfolioRecommendationOutput


class PortfolioAgent(BaseAgent):
    """
    Final Portfolio Manager responsible for converting
    the committee analysis into an actionable
    investment strategy.
    """

    TOOL_NAME = "portfolio_tool"

    # -----------------------------------------------------
    # Collect Data
    # -----------------------------------------------------

    def collect_data(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:

        tool = self.tools.get_tool(self.TOOL_NAME)

        if tool is None:
            raise ValueError(
                f"{self.TOOL_NAME} is not registered."
            )

        data = tool.execute(state)

        if not isinstance(data, dict):
            raise ValueError(
                "Portfolio tool must return a dictionary."
            )

        return data

    # -----------------------------------------------------
    # Validate Data
    # -----------------------------------------------------

    def validate_data(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:

        required = (
            "company",
            "investment",
            "committee",
            "analysis",
        )

        for section in required:
            if section not in data or not data[section]:
                raise ValueError(
                    f"Missing required section: {section}"
                )

        return data

    # -----------------------------------------------------
    # Prompt
    # -----------------------------------------------------

    def build_prompt(
        self,
        data: Dict[str, Any],
    ) -> str:

        return PortfolioPromptBuilder.build(data)

    # -----------------------------------------------------
    # Schema
    # -----------------------------------------------------

    def output_schema(
        self,
    ) -> Type[PortfolioRecommendationOutput]:

        return PortfolioRecommendationOutput

    # -----------------------------------------------------
    # Update State
    # -----------------------------------------------------

    def update_state(
        self,
        state: Dict[str, Any],
        result: PortfolioRecommendationOutput,
    ) -> Dict[str, Any]:

        state["portfolio_analysis"] = result

        return state