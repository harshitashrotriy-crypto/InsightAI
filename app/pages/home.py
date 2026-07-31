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
        max-width:1500px;
        padding-top:0.8rem;
        padding-bottom:1rem;
     }

        h1,h2,h3,h4{
            color:#103b6d;
        }

        .hero-title{
            text-align:center;
            font-size:42px;
            font-weight:700;
            color:#103b6d;
            margin-top:8px;
            margin-bottom:10px;
        }

        .hero-subtitle{
            text-align:center;
            font-size:18px;
            color:#5a6470;
            max-width:760px;
            margin:auto;
            line-height:1.8;
        }

        .section-title{
            text-align:center;
            font-size:30px;
            font-weight:700;
            color:#103b6d;
            margin-top:25px;
            margin-bottom:20px;
        }

        .small-gap{
            margin-top:10px;
        }

        div[data-testid="stHorizontalBlock"] > div{
            align-self:stretch;
        }

        div[data-testid="stVerticalBlock"] > div[data-testid="stContainer"]{
            height:100%;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# FEATURE CARD
# ==========================================================

def feature_card(icon, title, desc):

    with st.container(border=True):

        st.markdown(
            f"<h1 style='text-align:center;font-size:42px;'>{icon}</h1>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<h4 style='text-align:center;color:#103b6d;'>{title}</h4>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <p style="
            text-align:center;
            color:#555;
            line-height:1.7;
            min-height:85px;">
            {desc}
            </p>
            """,
            unsafe_allow_html=True,
        )


# ==========================================================
# STEP CARD
# ==========================================================

def step_card(title, text, emoji):

    with st.container(border=True):

        st.markdown(
            f"<h2 style='text-align:center'>{emoji}</h2>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<h4 style='text-align:center;color:#103b6d'>{title}</h4>",
            unsafe_allow_html=True,
        )

        st.write(text)


# ==========================================================
# HOME PAGE
# ==========================================================

def show():

    load_css()

    st.markdown("<div class='small-gap'></div>", unsafe_allow_html=True)

    if LOGO.exists():

        c1, c2, c3 = st.columns([1.5,1,1.5])

        with c2:
            st.image(str(LOGO), width=620)
    st.markdown(
        "<div class='hero-title'>Welcome to InsightAI</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='hero-subtitle'>

        Transform your raw business data into meaningful insights using
        Artificial Intelligence, interactive dashboards,
        automated reporting and smart visualizations.

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        "<div class='section-title'>✨ Everything You Need for Data Analysis</div>",
        unsafe_allow_html=True,
    )

    row1 = st.columns(3, gap="large")

    with row1[0]:
        feature_card(
            "📂",
            "Upload Dataset",
            "Upload CSV or Excel datasets securely and prepare them instantly for analysis."
        )

    with row1[1]:
        feature_card(
            "🤖",
            "AI Assistant",
            "Ask business questions in natural language and receive AI-powered insights."
        )

    with row1[2]:
        feature_card(
            "📊",
            "Interactive Dashboard",
            "Explore KPIs, charts and trends using beautiful interactive dashboards."
        )
        # ==========================================================
    # SECOND ROW OF FEATURES
    # ==========================================================

    st.write("")

    row2 = st.columns(3, gap="large")

    with row2[0]:
        feature_card(
            "📈",
            "AI Visualizer",
            "Automatically generate meaningful charts and visualizations to understand business trends faster."
        )

    with row2[1]:
        feature_card(
            "🛡️",
            "Data Quality",
            "Detect missing values, duplicate records and data inconsistencies before analysis."
        )

    with row2[2]:
        feature_card(
            "📄",
            "Executive Reports",
            "Generate professional PDF reports and business summaries ready for stakeholders."
        )

    st.write("")
    st.write("")

    # ==========================================================
    # GET STARTED
    # ==========================================================

    st.markdown(
        "<div class='section-title'>🚀 Ready to Get Started?</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='hero-subtitle'>
        Follow these three simple steps to unlock powerful insights from your business data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        step_card(
            "① Upload Dataset",
            "Import your CSV or Excel dataset securely into InsightAI.",
            "📂",
        )

    with c2:
        step_card(
            "② Analyze Data",
            "Use AI insights, dashboards and visualizations to explore trends.",
            "📊",
        )

    with c3:
        step_card(
            "③ Generate Reports",
            "Create executive-ready reports and download them in just one click.",
            "📄",
        )

    st.write("")
    st.write("")

    # ==========================================================
    # WHY CHOOSE INSIGHTAI
    # ==========================================================

    st.markdown(
        "<div class='section-title'>⭐ Why Choose InsightAI?</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='hero-subtitle'>
        Everything you need for modern business analytics in one intelligent platform.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.info("### ⚡\n\n**10x**\n\nFaster Analysis")

    with kpi2:
        st.info("### 📊\n\n**20+**\n\nInteractive Charts")

    with kpi3:
        st.info("### 🤖\n\n**Yes**\n\nAI Powered")

    with kpi4:
        st.info("### 📄\n\n**1 Click**\n\nPDF Reports")

    st.write("")

    st.success(
        "🚀 InsightAI combines Artificial Intelligence, Interactive Dashboards, Smart Visualizations and Automated Reporting to help businesses make faster and smarter decisions."
    )

    st.write("")
    st.write("")

        # ==========================================================
    # WHAT YOU CAN DO
    # ==========================================================

    st.markdown(
        "<div class='section-title'>💼 What You Can Do</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='hero-subtitle'>
        Empower your business decisions with AI-driven analytics, interactive dashboards,
        and intelligent reporting — all in one place.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    left, right = st.columns(2, gap="large")

    with left:
        with st.container(border=True):

            st.markdown("## 📊 Business Analytics")

            st.markdown("""
- Analyze large datasets effortlessly
- Track KPIs and business performance
- Identify trends and anomalies
- Build interactive dashboards
- Create executive summaries
- Improve decision making
- Monitor business growth
            """)

    with right:
        with st.container(border=True):

            st.markdown("## 🤖 AI Capabilities")

            st.markdown("""
- Natural language business queries
- AI-powered insights
- Smart chart recommendations
- Automated data quality checks
- Correlation analysis
- Executive report generation
- Faster business intelligence
            """)

    st.write("")
    st.write("")

    # ==========================================================
    # EXPLORE THE PLATFORM
    # ==========================================================

    st.markdown(
        "<div class='section-title'>⚡ Explore the Platform</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='hero-subtitle'>
        Everything you need to transform raw data into meaningful business insights.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        with st.container(border=True):

            st.markdown("## 📂 Upload")

            st.write(
                "Import CSV or Excel datasets quickly and securely to begin your analytics journey."
            )

    with c2:
        with st.container(border=True):

            st.markdown("## 📊 Analyze")

            st.write(
                "Discover trends using dashboards, AI insights, KPIs and interactive visualizations."
            )

    with c3:
        with st.container(border=True):

            st.markdown("## 📄 Export")

            st.write(
                "Generate executive-ready reports and share insights with your stakeholders instantly."
            )

    st.write("")
    st.write("")

            # ==========================================================
    # FOOTER
    # ==========================================================

    st.divider()

    logo_left, logo_center, logo_right = st.columns([2.2, 1, 2.2])

    with logo_center:
      if LOGO.exists():
        st.image(str(LOGO), width=650)
        st.markdown(
    "<div style='margin-top:-12px;'></div>",
    unsafe_allow_html=True,
)
    


    st.markdown(
            """
        <p style="
            text-align:center;
            color:#5f6368;
            font-size:16px;
            line-height:1.7;
            max-width:700px;
            margin:auto;
            ">
        Transforming Business Data into Intelligent Decisions with
        Artificial Intelligence, Interactive Dashboards,
        Smart Visualizations and Automated Reporting.
            </p>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    info1, info2, info3 = st.columns(3)

    with info1:
        st.success("🐍 Python")

    with info2:
        st.info("📊 Streamlit")

    with info3:
        st.warning("🤖 Groq AI")

    st.write("")

    st.markdown(
    """
    <div style="
        text-align:center;
        color:#777;
        font-size:14px;
        padding-top:10px;
    ">

    Built with ❤️ using Streamlit, Python, Plotly & Groq AI

    </div>
    """,
    unsafe_allow_html=True,
    )

    st.markdown(
    """
    <div style="
        text-align:center;
        color:#5f6368;
        font-size:15px;
        font-weight:600;
        padding-top:4px;
        padding-bottom:4px;
    ">
        Designed & Developed by <b>Harshita Shrotriy</b>
    </div>
    """,
    unsafe_allow_html=True,
)

    st.markdown(
    """
    <div style="
        text-align:center;
        color:#888;
        font-size:13px;
        padding-top:4px;
        padding-bottom:10px;
    ">
        © 2026 InsightAI • AI Business Analytics Platform
    </div>
    """,
    unsafe_allow_html=True,
)
    st.write("")







