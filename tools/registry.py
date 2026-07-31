"""
Tool Registry

Central registry for all tools in the application.
Automatically registers all built-in tools.
"""

from typing import Dict

from tools.base_tool import BaseTool

# =====================================================
# Financial Tools
# =====================================================

from tools.financial.financial_statement_tool import FinancialStatementTool
from tools.financial.stock_price_tool import StockPriceTool
from tools.financial.market_cap_tool import MarketCapTool
from tools.financial.ratio_calculator_tool import RatioCalculatorTool

# =====================================================
# News Tools
# =====================================================

from tools.news.news_tool import NewsTool

# =====================================================
# Technical Tools
# =====================================================

from tools.technical.technical_indicator_tool import TechnicalIndicatorTool

# =====================================================
# Analysis Tools
# =====================================================

from tools.valuation.valuation_tool import ValuationTool
from tools.risk.risk_tool import RiskTool
from tools.committee.committee_tool import CommitteeTool
from tools.portfolio.portfolio_tool import PortfolioTool


class ToolRegistry:
    """
    Central registry responsible for registering
    and providing access to application tools.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, BaseTool] = {}

        self._register_default_tools()

    # =====================================================
    # Register All Tools
    # =====================================================

    def _register_default_tools(self) -> None:
        """
        Register every built-in tool.
        """

        self._register_financial_tools()
        self._register_news_tools()
        self._register_technical_tools()
        self._register_analysis_tools()

    # =====================================================
    # Financial
    # =====================================================

    def _register_financial_tools(self) -> None:

        self.register(FinancialStatementTool())
        self.register(StockPriceTool())
        self.register(MarketCapTool())
        self.register(RatioCalculatorTool())

    # =====================================================
    # News
    # =====================================================

    def _register_news_tools(self) -> None:

        self.register(NewsTool())

    # =====================================================
    # Technical
    # =====================================================

    def _register_technical_tools(self) -> None:

        self.register(TechnicalIndicatorTool())

    # =====================================================
    # Analysis
    # =====================================================

    def _register_analysis_tools(self) -> None:

        self.register(ValuationTool())
        self.register(RiskTool())
        self.register(CommitteeTool())
        self.register(PortfolioTool())

    # =====================================================
    # Register Tool
    # =====================================================

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        Register a tool instance.
        """

        self._tools[tool.name] = tool

    # =====================================================
    # Get Tool
    # =====================================================

    def get_tool(
        self,
        tool_name: str,
    ) -> BaseTool:
        """
        Retrieve a registered tool.
        """

        try:
            return self._tools[tool_name]

        except KeyError as exc:
            raise ValueError(
                f"Tool '{tool_name}' is not registered."
            ) from exc

    # =====================================================
    # List Tools
    # =====================================================

    def list_tools(self) -> list[str]:
        """
        Return all registered tool names.
        """

        return sorted(self._tools.keys())

    # =====================================================
    # Check Tool
    # =====================================================

    def has_tool(
        self,
        tool_name: str,
    ) -> bool:
        """
        Check whether a tool is registered.
        """

        return tool_name in self._tools