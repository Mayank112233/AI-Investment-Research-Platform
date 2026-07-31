"""
Committee Decision Section
"""

import streamlit as st


def render_committee(state):
    """
    Render Committee Decision section.
    """

    st.subheader("🏛 AI Investment Committee")

    if not state:
        st.info("No committee decision available.")
        return

    committee = state.get("committee_decision")

    if committee is None:
        st.info("Committee decision not available.")
        return

    # ======================================================
    # Decision Overview
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        decision = committee.decision.upper()

        if decision == "BUY":
            st.success(f"Decision: {decision}")

        elif decision == "HOLD":
            st.warning(f"Decision: {decision}")

        elif decision == "SELL":
            st.error(f"Decision: {decision}")

        else:
            st.info(decision)

    with col2:

        st.metric(
            "Committee Confidence",
            f"{committee.confidence:.0f}%"
        )

    st.progress(committee.confidence / 100)

    st.divider()

    # ======================================================
    # Executive Summary
    # ======================================================

    st.markdown("## 📋 Executive Summary")

    st.info(
        committee.executive_summary
    )

    st.divider()

    # ======================================================
    # Investment Thesis
    # ======================================================

    st.markdown("## 💡 Investment Thesis")

    st.write(
        committee.investment_thesis
    )

    st.divider()

    # ======================================================
    # Supporting Factors
    # ======================================================

    st.markdown("## ✅ Supporting Factors")

    for factor in committee.supporting_factors:

        st.markdown(
            f"- {factor}"
        )

    st.divider()

    # ======================================================
    # Major Concerns
    # ======================================================

    st.markdown("## ⚠ Major Concerns")

    for concern in committee.major_concerns:

        st.markdown(
            f"- {concern}"
        )

    st.divider()

    # ======================================================
    # Decision Conditions
    # ======================================================

    st.markdown("## 📌 What Could Change This Decision?")

    for condition in committee.decision_conditions:

        st.markdown(
            f"- {condition}"
        )