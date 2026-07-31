"""
Charts Section
"""

import streamlit as st
import plotly.graph_objects as go


def render_charts(state):
    """
    Render dashboard charts.
    """

    st.subheader("📊 Investment Dashboard")

    if not state:
        st.info("No chart data available.")
        return

    financial = state.get("financial_data")
    risk = state.get("risk_analysis")

    if financial is None:
        st.warning("Financial data not available.")
        return

    statement = financial.financial_statement

    # =====================================================
    # Financial Metrics
    # =====================================================

    revenue = statement.get("revenue", 0)
    gross_profit = statement.get("gross_profit", 0)
    net_income = statement.get("net_income", 0)
    operating_cashflow = statement.get("operating_cashflow", 0)
    free_cashflow = statement.get("free_cashflow", 0)

    fig = go.Figure()

    fig.add_bar(
        x=[
            "Revenue",
            "Gross Profit",
            "Net Income",
            "Operating CF",
            "Free CF",
        ],
        y=[
            revenue,
            gross_profit,
            net_income,
            operating_cashflow,
            free_cashflow,
        ],
    )

    fig.update_layout(
        title="Financial Performance",
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.divider()

    # =====================================================
    # Financial Ratios
    # =====================================================

    ratios = financial.ratios

    fig = go.Figure()

    fig.add_bar(
        x=[
            "PE",
            "Profit Margin",
            "Debt/Equity",
        ],
        y=[
            ratios.pe_ratio,
            ratios.profit_margin,
            ratios.debt_to_equity,
        ],
    )

    fig.update_layout(
        title="Financial Ratios",
        height=450,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.divider()

    # =====================================================
    # Risk Gauge
    # =====================================================

    if risk:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=risk.risk_score,
                title={"text": "Risk Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "red"},
                },
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )