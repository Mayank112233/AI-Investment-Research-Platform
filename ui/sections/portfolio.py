"""
Portfolio Recommendation Section
"""

import streamlit as st


def render_portfolio(state):
    """
    Render Portfolio Recommendation section.
    """

    st.subheader("💼 Portfolio Recommendation")

    if not state:
        st.info("No portfolio recommendation available.")
        return

    portfolio = state.get("portfolio_recommendation")

    if portfolio is None:
        st.info("Portfolio recommendation not available.")
        return

    # ======================================================
    # Recommendation Overview
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        if hasattr(portfolio, "recommendation"):
            st.metric(
                "Recommendation",
                portfolio.recommendation
            )
        elif hasattr(portfolio, "decision"):
            st.metric(
                "Recommendation",
                portfolio.decision
            )

    with col2:

        if hasattr(portfolio, "confidence"):
            st.metric(
                "Confidence",
                f"{portfolio.confidence:.0f}%"
            )

            st.progress(portfolio.confidence / 100)

    st.divider()

    # ======================================================
    # Executive Summary
    # ======================================================

    if hasattr(portfolio, "summary"):

        st.markdown("## 📋 Executive Summary")

        st.info(portfolio.summary)

        st.divider()

    # ======================================================
    # Investment Strategy
    # ======================================================

    if hasattr(portfolio, "investment_strategy"):

        st.markdown("## 📈 Investment Strategy")

        st.write(portfolio.investment_strategy)

        st.divider()

    # ======================================================
    # Allocation
    # ======================================================

    if hasattr(portfolio, "allocation"):

        st.markdown("## 💰 Recommended Allocation")

        st.success(portfolio.allocation)

        st.divider()

    # ======================================================
    # Entry Strategy
    # ======================================================

    if hasattr(portfolio, "entry_strategy"):

        st.markdown("## 🎯 Entry Strategy")

        st.write(portfolio.entry_strategy)

        st.divider()

    # ======================================================
    # Exit Strategy
    # ======================================================

    if hasattr(portfolio, "exit_strategy"):

        st.markdown("## 🚪 Exit Strategy")

        st.write(portfolio.exit_strategy)

        st.divider()

    # ======================================================
    # Holding Period
    # ======================================================

    if hasattr(portfolio, "holding_period"):

        st.markdown("## ⏳ Holding Period")

        st.write(portfolio.holding_period)

        st.divider()

    # ======================================================
    # Risk Management
    # ======================================================

    if hasattr(portfolio, "risk_management"):

        st.markdown("## 🛡 Risk Management")

        st.warning(portfolio.risk_management)

        st.divider()

    # ======================================================
    # Action Items
    # ======================================================

    if hasattr(portfolio, "action_items"):

        st.markdown("## ✅ Action Items")

        for action in portfolio.action_items:
            st.markdown(f"- {action}")