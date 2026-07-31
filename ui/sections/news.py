"""
News Analysis Section
"""

import streamlit as st


def render_news(state):
    """
    Render News Analysis section.
    """

    st.subheader("📰 News Analysis")

    if not state:
        st.info("No analysis available.")
        return

    news = state.get("news_analysis")

    if news is None:
        st.info("News analysis not available.")
        return

    # ======================================================
    # Sentiment
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Overall Sentiment",
            news.overall_sentiment
        )

    with col2:
        st.metric(
            "Confidence",
            f"{news.confidence_score * 100:.0f}%"
        )

    st.progress(news.confidence_score)

    st.divider()

    # ======================================================
    # Final Summary
    # ======================================================

    st.markdown("## 📋 News Summary")

    st.info(news.final_summary)

    st.divider()

    # ======================================================
    # Key Events
    # ======================================================

    st.markdown("## 📌 Key Events")

    for event in news.key_events:
        st.markdown(f"- {event}")

    st.divider()

    # ======================================================
    # Opportunities & Risks
    # ======================================================

    left, right = st.columns(2)

    with left:

        st.markdown("### 🚀 Opportunities")

        for opportunity in news.opportunities:
            st.markdown(f"- {opportunity}")

    with right:

        st.markdown("### ⚠ Risks")

        for risk in news.risks:
            st.markdown(f"- {risk}")

    st.divider()

    # ======================================================
    # News Articles
    # ======================================================

    st.markdown("## 📰 Latest Articles")

    for article in news.articles:

        with st.container():

            st.markdown(f"### {article.title}")

            st.write(article.summary)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.caption(f"Source: {article.source}")

            with col2:
                st.caption(f"Sentiment: {article.sentiment}")

            with col3:
                st.caption(f"Impact: {article.impact}")

            st.divider()