"""
Application Theme
"""

import streamlit as st


def load_theme():
    """
    Load custom CSS for the application.
    """

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        div[data-testid="stMetric"] {
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #444;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )