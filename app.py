
"""
Main Streamlit Application
"""

import streamlit as st

from core.config import Config
from graph.investment_graph import InvestmentGraph

from ui.theme import load_theme
from ui.sidebar import create_sidebar
from ui.home import home


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_theme()


# ==========================================================
# Cache Graph
# ==========================================================

@st.cache_resource
def get_graph():
    """
    Compile the LangGraph workflow only once.
    """
    return InvestmentGraph().compile()


graph = get_graph()


# ==========================================================
# Sidebar
# ==========================================================

company, investment_period, risk_level, analyze = create_sidebar()


# ==========================================================
# Header
# ==========================================================

st.title("📈 AI Investment Research Agent")
st.caption("Multi-Agent AI Powered Investment Analysis")


# ==========================================================
# Workflow State
# ==========================================================

workflow_state = None


# ==========================================================
# Run Analysis
# ==========================================================

if analyze:

    if not company.strip():

        st.warning("Please enter a company ticker (e.g. TSLA, AAPL, MSFT).")
        st.stop()

    initial_state = {
        "company_name": company.strip().upper(),
        "ticker": company.strip().upper(),
        "investment_period": investment_period,
        "risk_tolerance": risk_level,

        "completed_nodes": [],
        "errors": [],
        "current_node": None,
    }

    try:

        with st.spinner("🤖 AI agents are analyzing the company..."):

            workflow_state = graph.invoke(initial_state)

        st.success("✅ Analysis completed successfully!")

    except Exception as e:

        st.error("❌ Workflow execution failed.")
        st.exception(e)

        st.stop()


# ==========================================================
# Home Page
# ==========================================================

home(workflow_state)


