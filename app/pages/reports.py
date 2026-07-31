import streamlit as st

from app.utils.ai import ask_ai
from app.utils.data_summary import generate_summary
from app.utils.pdf_generator import create_pdf


def show():

    st.title("📄 AI Business Report")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    summary = generate_summary(df)

    prompt = f"""
    You are a Senior Business Analyst.

    Generate a professional executive summary for the following dataset.

    Dataset Information:

    Rows: {summary['rows']}
    Columns: {summary['columns']}
    Missing Values: {summary['missing']}
    Duplicate Rows: {summary['duplicates']}

    Numeric Columns:
    {summary['numeric_columns']}

    Categorical Columns:
    {summary['categorical_columns']}

    Statistics:
    {summary['statistics']}

    Write:
    - Dataset Overview
    - Data Quality
    - Key Observations
    - Business Recommendations

    Keep it professional.
    """

    with st.spinner("Generating AI Report..."):
        ai_report = ask_ai(prompt)

    st.subheader("Executive Summary")

    st.write(ai_report)

    pdf = create_pdf(ai_report)

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf,
        file_name="InsightAI_Executive_Report.pdf",
        mime="application/pdf",
    )

    st.divider()

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", summary["rows"])
        st.metric("Columns", summary["columns"])

    with col2:
        st.metric("Missing Values", summary["missing"])
        st.metric("Duplicate Rows", summary["duplicates"])