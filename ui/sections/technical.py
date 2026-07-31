"""
Technical Analysis Section
"""

import streamlit as st


def render_technical(state):
    """
    Render Technical Analysis section.
    """

    st.subheader("📊 Technical Analysis")

    if not state:
        st.info("No technical analysis available.")
        return

    technical = state.get("technical_analysis")

    if technical is None:
        st.info("Technical analysis not available.")
        return

    # ======================================================
    # Market Status
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Trend",
            technical.trend
        )

    with col2:
        st.metric(
            "Momentum",
            technical.momentum
        )

    with col3:
        st.metric(
            "Volatility",
            technical.volatility
        )

    st.divider()

    # ======================================================
    # Trend Analysis
    # ======================================================

    st.markdown("## 📈 Trend Analysis")

    st.info(
        technical.trend_reason
    )

    st.divider()

    # ======================================================
    # Momentum Analysis
    # ======================================================

    st.markdown("## ⚡ Momentum Analysis")

    st.write(
        technical.momentum_reason
    )

    st.divider()

    # ======================================================
    # Volatility Analysis
    # ======================================================

    st.markdown("## 📉 Volatility")

    st.write(
        technical.volatility_reason
    )

    st.divider()

    # ======================================================
    # Volume Analysis
    # ======================================================

    st.markdown("## 📊 Volume")

    st.metric(
        "Volume Trend",
        technical.volume
    )

    st.write(
        technical.volume_reason
    )

    st.divider()

    # ======================================================
    # Trading Signal
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Trading Signal",
            technical.trading_signal
        )

    with col2:

        st.metric(
            "Confidence",
            f"{technical.confidence:.0f}%"
        )

    st.progress(
        technical.confidence / 100
    )

    st.divider()

    # ======================================================
    # Final Summary
    # ======================================================

    st.markdown("## 📋 Technical Summary")

    st.success(
        technical.summary
    )