"""
Base Agent

Provides the common execution workflow for all AI agents.
Each specific agent only needs to implement its own
business logic.
"""

from abc import ABC, abstractmethod

from graph.state import GraphState


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.
    """

    def __init__(self, llm_service, tool_registry):
        self.llm = llm_service
        self.tools = tool_registry

    @abstractmethod
    def collect_data(self, state: GraphState):
        """
        Collect required data.
        """
        pass

    @abstractmethod
    def validate_data(self, data):
        """
        Validate collected data.

        Return the validated data. If None is returned,
        the original collected data will be used.
        """
        pass

    @abstractmethod
    def build_prompt(self, data):
        """
        Build LLM prompt.
        """
        pass

    @abstractmethod
    def update_state(
        self,
        state: GraphState,
        result,
    ):
        """
        Update workflow state.
        """
        pass

    @abstractmethod
    def output_schema(self):
        """
        Return the output schema.
        """
        pass

    def analyze(self, prompt):
        """
        Execute the LLM.
        """

        return self.llm.generate(
            prompt=prompt,
            output_schema=self.output_schema(),
        )
    
    def run(self, state: GraphState):
        """
        Common workflow executed by every agent.
        """

        # Step 1
        data = self.collect_data(state)

        # Cache raw financial data
        if self.__class__.__name__ == "FinancialAgent":
            state["financial_data"] = data

        # Step 2
        validated = self.validate_data(data)

        if validated is None:
            validated = data

        # Step 3
        prompt = self.build_prompt(validated)

        # Step 4
        result = self.analyze(prompt)

        # Step 5
        self.update_state(state, result)

        return state