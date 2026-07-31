"""
Financial Prompt Builder
"""

from schemas.financial import FinancialAnalysisInput


class FinancialPromptBuilder:
    """
    Builds prompts for the Financial Agent.
    """

    @staticmethod
    def build(data: FinancialAnalysisInput) -> str:

        return f"""
You are a senior equity research analyst.

Analyze the financial health of the following company.

Ticker:
{data.ticker}

Financial Statement:
{data.financial_statement}

Stock Information:
{data.stock_information.model_dump()}

Market Information:
{data.market_information.model_dump()}

Financial Ratios:
{data.ratios.model_dump()}

Provide your analysis in the following format:

1. Revenue & Profitability
2. Financial Stability
3. Valuation
4. Risks
5. Strengths
6. Overall Financial Health

Keep the explanation concise, factual, and suitable for investment research.
"""