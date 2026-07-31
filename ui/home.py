"""
Home Page
"""

import streamlit as st

from ui.dashboard import render_dashboard


def home(workflow_state):
    """
    Render the application home page.
    """

    # ======================================================
    # Landing Page
    # ======================================================

    if workflow_state is None:

        st.markdown(
            """
            # 📈 AI Investment Research Platform

            Analyze any publicly traded company using a team of AI agents.

            ---
            """
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                """
                ### 🤖 AI Agents

                - Financial Analyst
                - News Analyst
                - Technical Analyst
                - Valuation Analyst
                - Risk Analyst
                - Investment Committee
                - Portfolio Advisor
                """
            )

        with col2:

            st.markdown(
                """
                ### 📊 Features

                - Financial Statement Analysis
                - News & Sentiment Analysis
                - Technical Indicators
                - Valuation Assessment
                - Risk Analysis
                - Investment Recommendation
                - Interactive Dashboard
                """
            )

        st.info("👈 Enter a company ticker in the sidebar and click **Analyze**.")

        return

    # ======================================================
    # Workflow Errors
    # ======================================================

    errors = workflow_state.get("errors", [])

    if errors:

        st.error("Workflow completed with errors.")

        with st.expander("View Errors"):
            for error in errors:
                st.write(error)

    # ======================================================
    # Dashboard
    # ======================================================

    render_dashboard(workflow_state)