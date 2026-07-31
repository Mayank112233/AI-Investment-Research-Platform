"""
Financial Analysis Section
"""

import streamlit as st


def render_financial(state):
    """
    Render Financial Analysis section.
    """

    st.subheader("📈 Financial Analysis")

    if not state:
        st.info("No analysis available.")
        return

    analysis = state.get("financial_analysis")

    if analysis is None:
        st.info("Financial analysis not available.")
        return

    # ======================================================
    # Executive Summary
    # ======================================================

    st.markdown("## Executive Summary")

    st.success(analysis.summary)

    st.divider()

    # ======================================================
    # Strengths & Risks
    # ======================================================

    left, right = st.columns(2)

    with left:

        st.markdown("### ✅ Strengths")

        if analysis.strengths:

            for strength in analysis.strengths:
                st.markdown(f"- {strength}")

        else:
            st.info("No strengths available.")

    with right:

        st.markdown("### ⚠️ Risks")

        if analysis.risks:

            for risk in analysis.risks:
                st.markdown(f"- {risk}")

        else:
            st.info("No risks available.")

    st.divider()

    # ======================================================
    # Valuation & Recommendation
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 💰 Valuation")

        st.write(analysis.valuation)

    with col2:

        st.markdown("### 🎯 Recommendation")

        st.write(analysis.recommendation)

    st.divider()

    # ======================================================
    # Confidence Score
    # ======================================================

    confidence = analysis.confidence_score * 100

    st.metric(
        "Confidence Score",
        f"{confidence:.0f}%"
    )

    st.progress(confidence / 100)