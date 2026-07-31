"""
Graph State

Shared state passed through the entire LangGraph workflow.
Each agent reads from the state and writes its output back.
"""

from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict

# =====================================================
# Raw Data Schemas
# =====================================================

from schemas.financial import FinancialAnalysisInput

# =====================================================
# Agent Output Schemas
# =====================================================

from schemas.financial_output import FinancialAnalysisOutput
from schemas.news_output import NewsAnalysisOutput
from schemas.technical_output import TechnicalAnalysisOutput
from schemas.valuation_output import ValuationAnalysisOutput
from schemas.risk_output import RiskAnalysisOutput
from schemas.committee_output import CommitteeDecisionOutput
from schemas.portfolio_output import PortfolioRecommendationOutput


class GraphState(TypedDict, total=False):
    """
    Shared workflow state used throughout the LangGraph pipeline.
    """

    # =====================================================
    # USER INPUT
    # =====================================================

    company_name: str
    ticker: str
    investment_period: str
    risk_tolerance: str

    # =====================================================
    # RAW TOOL OUTPUTS
    # =====================================================

    financial_data: Optional[FinancialAnalysisInput]

    stock_data: Dict[str, Any]
    news_data: List[Dict[str, Any]]
    technical_data: Dict[str, Any]

    # =====================================================
    # AGENT OUTPUTS
    # =====================================================

    financial_analysis: Optional[FinancialAnalysisOutput]
    news_analysis: Optional[NewsAnalysisOutput]
    technical_analysis: Optional[TechnicalAnalysisOutput]
    valuation_analysis: Optional[ValuationAnalysisOutput]
    risk_analysis: Optional[RiskAnalysisOutput]
    committee_decision: Optional[CommitteeDecisionOutput]
    portfolio_recommendation: Optional[PortfolioRecommendationOutput]

    # =====================================================
    # WORKFLOW METADATA
    # =====================================================

    completed_nodes: List[str]
    current_node: Optional[str]
    errors: List[str]