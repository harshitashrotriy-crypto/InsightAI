import streamlit as st
from app.utils.ai import ask_ai
from app.utils.data_summary import generate_summary


def show():

    st.title("🤖 AI Business Assistant")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    summary = generate_summary(df)

    dataset_info = f"""
Dataset Overview

Rows: {summary['rows']}
Columns: {summary['columns']}

Missing Values:
{summary['missing']}

Duplicate Rows:
{summary['duplicates']}

Column Names:
{summary['column_names']}

Top Values:
{summary['top_values']}

Statistics:
{summary['statistics']}
"""

    # ============================
    # Executive Summary
    # ============================

    st.subheader("✨ AI Executive Summary")

    if st.button("Generate Executive Insights"):

        prompt = f"""
You are a Senior Business Intelligence Consultant.

Below is a complete business summary generated from a dataset.

{dataset_info}

Generate:

1. Executive Summary

2. Top 5 Business Insights

3. Risks

4. Recommendations

5. KPIs to Monitor

Do NOT generate Python code.

Write professionally using markdown headings and bullet points.
"""

        with st.spinner("Generating Executive Summary..."):
            answer = ask_ai(prompt)

        st.markdown(answer)

    st.divider()

    # ============================
    # Ask Anything
    # ============================

    st.subheader("💬 Ask Anything")

    question = st.text_area(
        "Business Question",
        placeholder="Example: Which country has the highest violations?"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        prompt = f"""
You are a Senior Data Analyst.

You MUST answer ONLY using the dataset summary below.

{dataset_info}

Business Question:

{question}

Rules:

- Never generate Python code.
- Never generate SQL.
- Never explain how to analyze the data.
- Answer directly.
- Use the statistics and top values provided.
- If the answer cannot be determined, clearly say so.

Format:

### Direct Answer

### Explanation

### Business Insight
"""

        with st.spinner("Analyzing..."):
            answer = ask_ai(prompt)

        st.markdown(answer)