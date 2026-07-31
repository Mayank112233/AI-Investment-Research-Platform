from ui.widgets.kpi_cards import render_kpi_cards

import streamlit as st

# ==========================================================
# Widgets
# ==========================================================

from ui.widgets.kpi_cards import render_kpi_cards

# ==========================================================
# Sections
# ==========================================================

from ui.sections.overview import render_overview
from ui.sections.financial import render_financial
from ui.sections.news import render_news
from ui.sections.technical import render_technical
from ui.sections.valuation import render_valuation
from ui.sections.risk import render_risk
from ui.sections.committee import render_committee
from ui.sections.portfolio import render_portfolio
from ui.sections.charts import render_charts
from ui.sections.report import render_report


def render_dashboard(state):
    """
    Render the complete dashboard.
    """

    if state is None:
        st.warning("No workflow results available.")
        return

    # ======================================================
    # Header
    # ======================================================

    st.title("📈 AI Investment Research Dashboard")
    st.caption(
        "Multi-Agent AI Powered Investment Analysis Platform"
    )

    # ======================================================
    # KPI Cards
    # ======================================================

    try:
        render_kpi_cards(state)

    except Exception as e:
        st.error("Unable to render KPI cards.")
        st.exception(e)

    st.divider()

    # ======================================================
    # Tabs
    # ======================================================

    tab_names = [
        "🏠 Overview",
        "💰 Financial",
        "📰 News",
        "📊 Technical",
        "💵 Valuation",
        "⚠️ Risk",
        "🏛 Committee",
        "💼 Portfolio",
        "📈 Charts",
        "📄 Report",
    ]

    tabs = st.tabs(tab_names)

    renderers = [
        render_overview,
        render_financial,
        render_news,
        render_technical,
        render_valuation,
        render_risk,
        render_committee,
        render_portfolio,
        render_charts,
        render_report,
    ]

    # ======================================================
    # Render Each Section
    # ======================================================

    for tab, renderer in zip(tabs, renderers):

        with tab:

            try:
                renderer(state)

            except Exception as e:

                st.error(
                    f"Error rendering '{renderer.__name__}'"
                )

                with st.expander("View Error Details"):
                    st.exception(e)

    # ======================================================
    # Footer
    # ======================================================

    st.divider()

    st.caption(
        "AI Investment Research Platform | "
        "Financial • News • Technical • "
        "Valuation • Risk • Committee • Portfolio"
    )