from typing import Any, Dict

from tools.base_tool import BaseTool


class RatioCalculatorTool(BaseTool):
    """
    Calculates derived financial ratios.
    """

    @property
    def name(self) -> str:
        return "ratio_calculator_tool"

    @property
    def description(self) -> str:
        return (
            "Calculates important financial ratios."
        )

    def execute(
        self,
        financial_statement: Dict[str, Any],
        stock_information: Dict[str, Any],
        market_information: Dict[str, Any],
    ) -> Dict[str, Any]:

        revenue = financial_statement.get("revenue", 0) or 0
        net_income = financial_statement.get("net_income", 0) or 0
        eps = financial_statement.get("eps", 0) or 0
        debt_to_equity = (
            financial_statement.get("debt_to_equity", 0) or 0
        )

        current_price = (
            stock_information.get("current_price", 0) or 0
        )

        market_cap = (
            market_information.get("market_cap", 0) or 0
        )

        ratios = {
            "market_cap": market_cap,
            "debt_to_equity": debt_to_equity,
        }

        ratios["pe_ratio"] = (
            round(current_price / eps, 2)
            if eps > 0
            else None
        )

        ratios["profit_margin"] = (
            round(net_income / revenue, 4)
            if revenue > 0
            else None
        )

        return ratios