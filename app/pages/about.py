
import streamlit as st
from pathlib import Path

import streamlit as st
from pathlib import Path

# ==========================================================
# ASSETS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
LOGO = BASE_DIR / "assets" / "insightai_logo.png"


# ==========================================================
# PAGE STYLING
# ==========================================================

def load_css():

    st.markdown(
        """
        <style>

        .block-container{
            max-width:1350px;
            padding-top:1rem;
            padding-bottom:1rem;
        }

        h1,h2,h3,h4{
            color:#103b6d;
        }

        .section-title{
            text-align:center;
            color:#103b6d;
            font-size:34px;
            font-weight:700;
            margin-top:10px;
            margin-bottom:10px;
        }

        .subtitle{
            text-align:center;
            color:#6b7280;
            font-size:18px;
            line-height:1.8;
            max-width:850px;
            margin:auto;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# SHOW
# ==========================================================

def show():

    load_css()

    st.markdown(
        "<div class='section-title'>ℹ️ About InsightAI</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns([2,1,2])

    with c2:
        if LOGO.exists():
            st.image(str(LOGO), width=180)

    st.markdown(
        """
        <div class='subtitle'>
        <b>AI-Powered Business Analytics Platform</b>
        <br><br>

        Transform raw business data into meaningful insights using
        Artificial Intelligence, interactive dashboards,
        automated reporting and intelligent visualizations —
        all from one modern platform.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    with st.container(border=True):

        st.markdown("## 📌 About InsightAI")

        st.write(
            """
InsightAI is an AI-powered Business Analytics Platform designed to simplify
business data analysis. It enables users to upload datasets, analyze
business performance through interactive dashboards, generate AI-powered
insights, visualize trends, assess data quality, and create executive-ready
reports — all within one intuitive application.

Whether you're a Business Analyst, Data Analyst, or decision-maker,
InsightAI helps transform raw data into actionable insights faster and
more efficiently.
            """
        )

    st.write("")
    # ==========================================================
    # KEY FEATURES
    # ==========================================================

    st.markdown(
        "<div class='section-title'>✨ Key Features</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='subtitle'>
        Everything you need to analyze, visualize and generate
        AI-powered business insights from your data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    row1 = st.columns(3, gap="large")

    with row1[0]:
        with st.container(border=True):
            st.markdown("## 📂 Upload Dataset")
            st.write(
                "Import CSV or Excel datasets securely and prepare them instantly for analysis."
            )

    with row1[1]:
        with st.container(border=True):
            st.markdown("## 🤖 AI Assistant")
            st.write(
                "Ask business questions in natural language and receive AI-powered insights."
            )

    with row1[2]:
        with st.container(border=True):
            st.markdown("## 📊 Interactive Dashboard")
            st.write(
                "Explore KPIs, business metrics and trends using interactive dashboards."
            )

    st.write("")

    row2 = st.columns(3, gap="large")

    with row2[0]:
        with st.container(border=True):
            st.markdown("## 📈 AI Visualizer")
            st.write(
                "Automatically generate meaningful charts and visualizations from your data."
            )

    with row2[1]:
        with st.container(border=True):
            st.markdown("## 🛡️ Data Quality")
            st.write(
                "Identify missing values, duplicate records and inconsistencies before analysis."
            )

    with row2[2]:
        with st.container(border=True):
            st.markdown("## 📄 Executive Reports")
            st.write(
                "Generate professional business reports and executive-ready summaries."
            )

    st.write("")
    
    # ==========================================================
    # KEY FEATURES
    # ==========================================================

    st.markdown(
        "<div class='section-title'>✨ Key Features</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='subtitle'>
        Everything you need to analyze, visualize and generate
        AI-powered business insights from your data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    row1 = st.columns(3, gap="large")

    with row1[0]:
        with st.container(border=True):
            st.markdown("## 📂 Upload Dataset")
            st.write(
                "Import CSV or Excel datasets securely and prepare them instantly for analysis."
            )

    with row1[1]:
        with st.container(border=True):
            st.markdown("## 🤖 AI Assistant")
            st.write(
                "Ask business questions in natural language and receive AI-powered insights."
            )

    with row1[2]:
        with st.container(border=True):
            st.markdown("## 📊 Interactive Dashboard")
            st.write(
                "Explore KPIs, business metrics and trends using interactive dashboards."
            )

    st.write("")

    row2 = st.columns(3, gap="large")

    with row2[0]:
        with st.container(border=True):
            st.markdown("## 📈 AI Visualizer")
            st.write(
                "Automatically generate meaningful charts and visualizations from your data."
            )

    with row2[1]:
        with st.container(border=True):
            st.markdown("## 🛡️ Data Quality")
            st.write(
                "Identify missing values, duplicate records and inconsistencies before analysis."
            )

    with row2[2]:
        with st.container(border=True):
            st.markdown("## 📄 Executive Reports")
            st.write(
                "Generate professional business reports and executive-ready summaries."
            )

    st.write("")
    st.write("")
    # ==========================================================
    # TECHNOLOGY STACK
    # ==========================================================

    st.markdown(
        "<div class='section-title'>🛠 Technologies & Skills</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='subtitle'>
        Built using modern technologies for AI-powered analytics,
        visualization and business intelligence.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # First Row
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
     with st.container(border=True):
        st.markdown("### 🤖 AI & Analytics")
        st.success("🧠 Generative AI")
        st.success("🤖 Groq LLM")
        st.success("💬 Prompt Engineering")
        st.success("📈 AI-Powered Insights")

    with row1_col2:
     with st.container(border=True):
        st.markdown("### 📈 Visualization")
        st.warning("📊 Plotly")
        st.warning("📉 Interactive Dashboards")
        st.warning("📋 Business Intelligence")
        st.warning("📄 Automated Reporting")

    st.write("")

    # Second Row
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
     with st.container(border=True):
        st.markdown("### 📊 Data Analytics")
        st.info("🐍 Python")
        st.info("🐼 Pandas")
        st.info("🔍 Exploratory Data Analysis (EDA)")
        st.info("📊 KPI Analysis")

    with row2_col2:
     with st.container(border=True):
        st.markdown("### 💻 Application")
        st.success("🎈 Streamlit")
        st.success("📂 Excel Processing")
        st.success("📄 OpenPyXL")
        st.success("🛡 Data Quality Analysis")

    st.write("")
    st.write("")
    # ==========================================================
    # PROJECT OBJECTIVE
    # ==========================================================

    st.markdown(
        "<div class='section-title'>🎯 Project Objective</div>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):

        st.write(
        """
        InsightAI was developed to simplify business analytics by combining Artificial
        Intelligence, interactive dashboards, data visualization and automated reporting
        into a single easy-to-use platform.

        The application empowers Business Analysts, Data Analysts and decision-makers
        to transform raw business data into meaningful insights faster, improve reporting
        efficiency and support data-driven decision making.
            """
        )

    st.write("")
    st.write("")
    # ==========================================================
    # ABOUT THE DEVELOPER
    # ==========================================================

    st.markdown(
        "<div class='section-title'>👩🏻‍💻 About the Developer</div>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):

        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown(
                """
                <div style="font-size:90px; text-align:center;">
                    👩🏻‍💻
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown("### Harshita Shrotriy")
            st.caption("AI Business Analyst • Data Analytics Enthusiast")

            st.write(
                """
Passionate about transforming business data into meaningful insights through
AI, analytics, and interactive dashboards. This project showcases how modern
AI can simplify data exploration, visualization, reporting, and business
decision-making in a single platform.
                """
            )

            st.info("🚀 Built with Python • Streamlit • Plotly • Pandas • Groq AI")

    st.write("")
    st.write("")

    # ==========================================================
    # THANK YOU
    # ==========================================================

    with st.container(border=True):
        st.markdown(
            """
                <div style="text-align:center;padding:10px 0;">
                <h2 style="color:#103b6d;">🙏 Thank You for Visiting InsightAI</h2>

                <p style="font-size:18px;color:#555;">
                Thank you for exploring InsightAI. I hope this project demonstrates
                my passion for data analytics, AI-powered solutions, and building
                intuitive business applications.
                </p>

                <p style="font-size:16px;color:#777;">
                Feedback and suggestions are always welcome.
                </p>
                </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.divider()

    footer_left, footer_center, footer_right = st.columns([1, 2, 1])

    with footer_center:
        logo_left, logo_center, logo_right = st.columns([1,2,1])

    with logo_center:

        if LOGO.exists():
         st.image(str(LOGO), width=220)

        st.markdown(
            """
            <div style="text-align:center;color:#666;font-size:15px;">

            <b>InsightAI</b><br>

            AI-Powered Business Analytics Platform
            <br>

            Built with ❤️ using
            <br>
            Python • Streamlit • Plotly • Groq AI
            <br>

            Designed & Developed by
            <br>
            <b>Harshita Shrotriy</b>
            <br>

            Version 1.0
            <br>

            © 2026 InsightAI. All Rights Reserved.

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
       