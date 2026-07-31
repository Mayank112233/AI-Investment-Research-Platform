"""
Financial Agent

Responsible for analyzing the financial health
of a company.
"""

from agents.base_agent import BaseAgent

from graph.state import GraphState

from schemas.financial_output import FinancialAnalysisOutput

from schemas.financial import (
    FinancialAnalysisInput,
    MarketInformation,
    StockInformation,
    FinancialRatios,
)

from prompts.financial_prompt import FinancialPromptBuilder


class FinancialAgent(BaseAgent):
    """
    Financial analysis agent.
    """

    def __init__(self, llm_service, tool_registry):
        super().__init__(llm_service, tool_registry)

    def collect_data(
        self,
        state: GraphState,
    ) -> FinancialAnalysisInput:
        """
        Collect all financial data required for analysis.
        """

        ticker = state["ticker"]

        financial_tool = self.tools.get_tool(
            "financial_statement_tool"
        )

        stock_tool = self.tools.get_tool(
            "stock_price_tool"
        )

        market_tool = self.tools.get_tool(
            "market_cap_tool"
        )

        ratio_tool = self.tools.get_tool(
            "ratio_calculator_tool"
        )

        financial_statement = financial_tool.execute(
            ticker
        )

        stock_information = stock_tool.execute(
            ticker
        )

        market_information = market_tool.execute(
            ticker
        )

        ratios = ratio_tool.execute(
            financial_statement,
            stock_information,
            market_information,
        )

        return FinancialAnalysisInput(
            ticker=ticker,
            financial_statement=financial_statement,
            stock_information=StockInformation(
                **stock_information
            ),
            market_information=MarketInformation(
                **market_information
            ),
            ratios=FinancialRatios(
                **ratios
            ),
        )

    def validate_data(
        self,
        data: FinancialAnalysisInput,
    ) -> FinancialAnalysisInput:
        """
        Validate collected data.
        """

        if not data.ticker:
            raise ValueError(
                "Ticker is required."
            )

        return data

    def build_prompt(
        self,
        data: FinancialAnalysisInput,
    ) -> str:
        """
        Build financial analysis prompt.
        """

        return FinancialPromptBuilder.build(
            data
        )

    def output_schema(self):
        """
        Output schema returned by the LLM.
        """

        return FinancialAnalysisOutput

    def update_state(
        self,
        state: GraphState,
        result: FinancialAnalysisOutput,
    ):
        """
        Store analysis result in workflow state.
        """

        state["financial_analysis"] = result

        return state