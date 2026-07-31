import streamlit as st
from pathlib import Path

from app.pages import (
    home,
    upload,
    dashboard,
    ai_assistant,
    ai_visualizer,
    data_quality,
    correlation,
    reports,
    about,
)

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------
# SIDEBAR CSS
# -----------------------------------------------------

st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0F172A,#1E293B);
}

/* Reduce top spacing */
[data-testid="stSidebar"] .block-container{
    padding-top:0.4rem;
    padding-bottom:0.5rem;
}

/* Center logo */
[data-testid="stSidebar"] img{
    display:block;
    margin-left:auto;
    margin-right:auto;
}

/* Navigation heading */
[data-testid="stSidebar"] label{
    color:white !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* Navigation text */
div[role="radiogroup"] label p{
    font-size:19px !important;
    font-weight:600 !important;
    color:white !important;
}

/* Radio spacing */
div[role="radiogroup"] label{
    padding-top:6px !important;
    padding-bottom:6px !important;
}

/* Sidebar text */
[data-testid="stSidebar"] *{
    color:white !important;
}

/* Hide Streamlit footer */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------

logo_path = Path("assets/insightai_logo.png")

if logo_path.exists():
    st.sidebar.image(str(logo_path), width=170)

st.sidebar.markdown(
    """
<h2 style="
text-align:left;
margin-top:-8px;
margin-bottom:8px;
color:white;
font-size:30px;
font-weight:700;">
InsightAI
</h2>
""",
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "📂 Upload Dataset",
        "📊 Dashboard",
        "🤖 AI Assistant",
        "📈 AI Visualizer",
        "✅ Data Quality",
        "📉 Correlation",
        "📄 Reports",
        "ℹ️ About",
    ],
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown(
    """
<div style="
text-align:center;
font-size:14px;
color:#CBD5E1;
line-height:1.6;">
🚀 AI-Powered Business Analytics Platform
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# PAGE ROUTING
# -----------------------------------------------------

if page == "🏠 Home":
    home.show()

elif page == "📂 Upload Dataset":
    upload.show()

elif page == "📊 Dashboard":
    dashboard.show()

elif page == "🤖 AI Assistant":
    ai_assistant.show()

elif page == "📈 AI Visualizer":
    ai_visualizer.show()

elif page == "✅ Data Quality":
    data_quality.show()

elif page == "📉 Correlation":
    correlation.show()

elif page == "📄 Reports":
    reports.show()

elif page == "ℹ️ About":
    about.show()