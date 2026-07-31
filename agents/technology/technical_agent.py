"""
Technical Analysis Agent
"""

from typing import Any, Dict

from agents.base_agent import BaseAgent
from prompts.technical_prompt import TechnicalPromptBuilder
from schemas.technical_output import TechnicalAnalysisOutput


class TechnicalAgent(BaseAgent):
    """
    Agent responsible for performing technical analysis
    using market indicators and LLM-based interpretation.
    """

    TOOL_NAME = "technical_indicator_tool"

    def __init__(self, llm_service, tool_registry):
        super().__init__(llm_service, tool_registry)

    # -----------------------------------------------------
    # Collect Data
    # -----------------------------------------------------

    def collect_data(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetch technical indicators for the given stock.
        """

        ticker = state.get("ticker")

        if not ticker:
            raise ValueError("Ticker is required for technical analysis.")

        technical_tool = self.tools.get_tool(self.TOOL_NAME)

        technical_data = technical_tool.execute(ticker=ticker)

        return {
            "company_name": state["company_name"],
            "ticker": ticker,
            "technical_data": technical_data,
        }

    # -----------------------------------------------------
    # Validate Data
    # -----------------------------------------------------

    def validate_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate collected technical data.
        """

        technical_data = data.get("technical_data")

        if technical_data is None:
            raise ValueError("Technical data is missing.")

        if not isinstance(technical_data, dict):
            raise ValueError("Technical data must be a dictionary.")

        if len(technical_data) == 0:
            raise ValueError("Technical data is empty.")

        return data

    # -----------------------------------------------------
    # Build Prompt
    # -----------------------------------------------------

    def build_prompt(
        self,
        data: Dict[str, Any],
    ) -> str:
        """
        Build the prompt for the LLM.
        """

        return TechnicalPromptBuilder.build(
            company_name=data["company_name"],
            ticker=data["ticker"],
            technical_data=data["technical_data"],
        )

    # -----------------------------------------------------
    # Output Schema
    # -----------------------------------------------------

    def output_schema(self):
        """
        Structured output expected from the LLM.
        """

        return TechnicalAnalysisOutput

    # -----------------------------------------------------
    # Update State
    # -----------------------------------------------------

    def update_state(
        self,
        state: Dict[str, Any],
        result: TechnicalAnalysisOutput,
    ):
        """
        Store the technical analysis result in graph state.
        """

        state["technical_analysis"] = result

        return state