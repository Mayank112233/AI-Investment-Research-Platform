"""
Overview Section

Displays the executive investment summary.
"""

import streamlit as st


def render_overview(state):

    st.subheader("Investment Overview")

    if not state:
        st.info("No analysis available.")
        return

    financial = state.get("financial_data")
    committee = state.get("committee_decision")
    valuation = state.get("valuation_analysis")
    risk = state.get("risk_analysis")

    left, right = st.columns(2)

    # =====================================================
    # Company Information
    # =====================================================

    with left:

        st.markdown("### 📊 Company Information")

        st.metric(
            "Company",
            state.get("company_name", "N/A"),
        )

        st.metric(
            "Investment Horizon",
            state.get("investment_period", "N/A"),
        )

        st.metric(
            "Risk Appetite",
            state.get("risk_tolerance", "N/A"),
        )

        if financial:

            price = financial.stock_information.current_price

            if price is not None:

                st.metric(
                    "Current Price",
                    f"${price:.2f}",
                )

    # =====================================================
    # AI Recommendation
    # =====================================================

    with right:

        st.markdown("### 🤖 AI Recommendation")

        if committee:

            st.metric(
                "Decision",
                committee.decision,
            )

            st.metric(
                "Confidence",
                f"{committee.confidence:.0f}%",
            )

        if valuation:

            st.metric(
                "Valuation",
                valuation.valuation,
            )

        if risk:

            st.metric(
                "Overall Risk",
                risk.overall_risk,
            )

    st.divider()

    # =====================================================
    # Executive Summary
    # =====================================================

    if committee:

        st.markdown("## Executive Summary")

        st.info(
            committee.executive_summary
        )

        st.markdown("## Investment Thesis")

        st.write(
            committee.investment_thesis
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### ✅ Supporting Factors")

            for factor in committee.supporting_factors:

                st.markdown(
                    f"- {factor}"
                )

        with col2:

            st.markdown("### ⚠ Major Concerns")

            for concern in committee.major_concerns:

                st.markdown(
                    f"- {concern}"
                )