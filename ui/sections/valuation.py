"""
Valuation Analysis Section
"""

import streamlit as st


def render_valuation(state):
    """
    Render Valuation Analysis section.
    """

    st.subheader("💰 Valuation Analysis")

    if not state:
        st.info("No valuation analysis available.")
        return

    valuation = state.get("valuation_analysis")

    if valuation is None:
        st.info("Valuation analysis not available.")
        return

    # ======================================================
    # Overall Valuation
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Valuation",
            valuation.valuation
        )

    with col2:

        st.metric(
            "Confidence",
            f"{valuation.confidence:.0f}%"
        )

    st.progress(
        valuation.confidence / 100
    )

    st.divider()

    # ======================================================
    # Executive Summary
    # ======================================================

    st.markdown("## 📋 Executive Summary")

    st.success(
        valuation.summary
    )

    st.divider()

    # ======================================================
    # Valuation Reason
    # ======================================================

    st.markdown("## 📈 Valuation Reason")

    st.write(
        valuation.valuation_reason
    )

    st.divider()

    # ======================================================
    # Margin of Safety
    # ======================================================

    st.markdown("## 🛡 Margin of Safety")

    st.info(
        valuation.margin_of_safety
    )

    st.divider()

    # ======================================================
    # Fair Value Opinion
    # ======================================================

    st.markdown("## ⚖ Fair Value Opinion")

    st.write(
        valuation.fair_value_opinion
    )

    st.divider()

    # ======================================================
    # Investment Outlook
    # ======================================================

    st.markdown("## 📊 Investment Outlook")

    st.write(
        valuation.investment_outlook
    )