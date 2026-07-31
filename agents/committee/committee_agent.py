"""
Committee Agent
"""

from typing import Any, Dict, Type

from agents.base_agent import BaseAgent
from prompts.committee_prompt import CommitteePromptBuilder
from schemas.committee_output import CommitteeDecisionOutput


class CommitteeAgent(BaseAgent):
    """
    Final Investment Committee responsible for
    synthesizing all previous analyses into
    a single investment decision.
    """

    TOOL_NAME = "committee_tool"

    # -----------------------------------------------------
    # Collect Data
    # -----------------------------------------------------

    def collect_data(
        self,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Collect committee context.
        """

        tool = self.tools.get_tool(self.TOOL_NAME)

        if tool is None:
            raise ValueError(
                f"{self.TOOL_NAME} is not registered."
            )

        data = tool.execute(state)

        if not isinstance(data, dict):
            raise ValueError(
                "Committee tool must return a dictionary."
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
        Validate committee context.
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
        Build committee prompt.
        """

        return CommitteePromptBuilder.build(data)

    # -----------------------------------------------------
    # Output Schema
    # -----------------------------------------------------

    def output_schema(
        self,
    ) -> Type[CommitteeDecisionOutput]:
        """
        Structured output schema.
        """

        return CommitteeDecisionOutput

    # -----------------------------------------------------
    # Update State
    # -----------------------------------------------------

    def update_state(
        self,
        state: Dict[str, Any],
        result: CommitteeDecisionOutput,
    ) -> Dict[str, Any]:
        """
        Store committee decision.
        """

        state["committee_decision"] = result

        return state