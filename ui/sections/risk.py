"""
Risk Analysis Section
"""

import streamlit as st


def render_risk(state):
    """
    Render Risk Analysis section.
    """

    st.subheader("⚠️ Risk Analysis")

    if not state:
        st.info("No risk analysis available.")
        return

    risk = state.get("risk_analysis")

    if risk is None:
        st.info("Risk analysis not available.")
        return

    # ======================================================
    # Risk Overview
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Risk",
            risk.overall_risk
        )

    with col2:

        st.metric(
            "Risk Score",
            f"{risk.risk_score:.0f}/100"
        )

    st.progress(risk.risk_score / 100)

    st.divider()

    # ======================================================
    # Executive Summary
    # ======================================================

    st.markdown("## 📋 Executive Summary")

    st.warning(risk.summary)

    st.divider()

    # ======================================================
    # Risk Categories
    # ======================================================

    st.markdown("## 🏢 Business Risk")
    st.write(risk.business_risk)

    st.divider()

    st.markdown("## 💰 Financial Risk")
    st.write(risk.financial_risk)

    st.divider()

    st.markdown("## 🌍 Market Risk")
    st.write(risk.market_risk)

    st.divider()

    st.markdown("## 📰 News Risk")
    st.write(risk.news_risk)

    st.divider()

    st.markdown("## 📈 Technical Risk")
    st.write(risk.technical_risk)

    st.divider()

    st.markdown("## 💵 Valuation Risk")
    st.write(risk.valuation_risk)

    st.divider()

    # ======================================================
    # Final Recommendation
    # ======================================================

    st.markdown("## 🎯 Risk Recommendation")

    st.success(risk.recommendation)