"""
Sidebar
"""

import streamlit as st


def create_sidebar():
    """
    Render sidebar and return user inputs.
    """

    with st.sidebar:

        st.title("📈 AI Investment")

        st.markdown("---")

        company = st.text_input(
            "Company / Ticker",
            placeholder="TSLA, AAPL, MSFT..."
        )

        investment_period = st.selectbox(
            "Investment Horizon",
            [
                "Short Term",
                "Medium Term",
                "Long Term",
            ]
        )

        risk_level = st.selectbox(
            "Risk Appetite",
            [
                "Low",
                "Moderate",
                "High",
            ]
        )

        st.markdown("---")

        analyze = st.button(
            "🚀 Analyze Company",
            use_container_width=True
        )

    return (
        company,
        investment_period,
        risk_level,
        analyze,
    )