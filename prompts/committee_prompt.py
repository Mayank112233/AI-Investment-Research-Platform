"""
Committee Prompt Builder
"""

import json
from typing import Any, Dict


class CommitteePromptBuilder:
    """
    Builds the Investment Committee prompt.
    """

    @staticmethod
    def build(
        data: Dict[str, Any],
    ) -> str:
        """
        Build committee decision prompt.
        """

        company = data["company"]
        investment = data["investment"]
        analysis = data["analysis"]

        return f"""
You are the Chairperson of an Investment Committee at a global asset management firm.

Your responsibility is NOT to perform financial analysis.

Instead, review the analyses prepared by specialist teams and make a final investment decision.

========================================================
COMPANY
========================================================

Company Name:
{company["name"]}

Ticker:
{company["ticker"]}

Investment Horizon:
{investment["period"]}

Risk Tolerance:
{investment["risk_tolerance"]}

========================================================
FINANCIAL ANALYSIS
========================================================

{json.dumps(
    analysis["financial"].model_dump(),
    indent=2
)}

========================================================
NEWS ANALYSIS
========================================================

{json.dumps(
    analysis["news"].model_dump(),
    indent=2
)}

========================================================
TECHNICAL ANALYSIS
========================================================

{json.dumps(
    analysis["technical"].model_dump(),
    indent=2
)}

========================================================
VALUATION ANALYSIS
========================================================

{json.dumps(
    analysis["valuation"].model_dump(),
    indent=2
)}

========================================================
RISK ANALYSIS
========================================================

{json.dumps(
    analysis["risk"].model_dump(),
    indent=2
)}

========================================================
YOUR RESPONSIBILITIES
========================================================

Review every specialist report.

Resolve disagreements between analysts.

Determine whether the company deserves:

BUY

HOLD

SELL

Base your decision on evidence.

Do not simply average opinions.

If technical indicators are weak but long-term fundamentals are excellent,
you may still recommend BUY while acknowledging short-term weakness.

Likewise, a technically strong stock with poor financial health may deserve HOLD or SELL.

========================================================
OUTPUT REQUIREMENTS
========================================================

Return ONLY the structured output schema.

Do not include markdown.

Do not include explanations outside the schema.

Do not invent facts.

If information is insufficient,
state uncertainty in the reasoning while still producing the required schema.
"""
    