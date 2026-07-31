"""
ui/widgets/kpi_cards.py
"""

import streamlit as st


def kpi_card(title, value, delta=None, help_text=None):
    """Render a single KPI card."""
    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text,
    )


def render_kpi_cards(state):
    """Render dashboard KPI cards."""

    financial = state.get("financial_data")
    risk = state.get("risk_analysis")
    valuation = state.get("valuation_analysis")

    revenue = "--"
    market_cap = "--"
    risk_score = "--"
    target_price = "--"

    if financial:
        revenue = getattr(financial, "revenue", "--")
        market_cap = getattr(financial, "market_cap", "--")

    if risk:
        risk_score = getattr(risk, "risk_score", "--")

    if valuation:
        target_price = getattr(valuation, "target_price", "--")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("Revenue", revenue)

    with col2:
        kpi_card("Market Cap", market_cap)

    with col3:
        kpi_card("Risk Score", risk_score)

    with col4:
        kpi_card("Target Price", target_price)