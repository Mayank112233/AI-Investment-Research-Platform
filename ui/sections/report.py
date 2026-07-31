"""
Investment Report
"""

import streamlit as st


def render_report(state):

    st.subheader("📄 Investment Report")

    if not state:
        st.info("No report available.")
        return

    committee = state.get("committee_decision")
    financial = state.get("financial_analysis")
    news = state.get("news_analysis")
    technical = state.get("technical_analysis")
    valuation = state.get("valuation_analysis")
    risk = state.get("risk_analysis")

    st.markdown("# Executive Summary")

    if committee:
        st.info(committee.executive_summary)

    st.divider()

    if financial:
        st.markdown("## Financial")
        st.write(financial.summary)

    if news:
        st.markdown("## News")
        st.write(news.final_summary)

    if technical:
        st.markdown("## Technical")
        st.write(technical.summary)

    if valuation:
        st.markdown("## Valuation")
        st.write(valuation.summary)

    if risk:
        st.markdown("## Risk")
        st.write(risk.summary)

    if committee:

        st.markdown("## Final Recommendation")

        st.success(
            committee.decision
        )

        st.metric(
            "Confidence",
            f"{committee.confidence:.0f}%"
        )