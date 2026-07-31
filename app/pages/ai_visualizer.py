import streamlit as st

from app.utils.chart_generator import generate_chart
from app.utils.ai import ask_ai


def show():

    st.title("📊 AI Visualizer")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    st.markdown("### Describe the chart you want")

    st.info(
        """
Examples:

• Show country distribution

• Pie chart of category

• Histogram of views

• Line chart of sales

• Scatter plot

• Show severity distribution
"""
    )

    query = st.text_input(
        "Chart Request",
        placeholder="Example: Pie chart of Category"
    )

    if st.button("Generate Visualization"):

        if query.strip() == "":
            st.warning("Please enter a chart request.")
            return

        with st.spinner("Generating chart..."):

            fig, title, summary = generate_chart(df, query)

        if fig is None:
            st.error(summary)
            return

        st.success("Visualization Generated Successfully!")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        st.subheader("🤖 AI Business Insights")

        prompt = f"""
You are a Senior Business Intelligence Consultant.

A chart has been generated.

Chart Title:
{title}

Chart Summary:
{summary}

Please provide:

1. Executive Summary

2. Key Business Insights

3. Risks (if any)

4. Recommendations

Do NOT write Python code.

Do NOT mention that you cannot see the chart.

Answer professionally using markdown.
"""

        with st.spinner("Generating AI Insights..."):

            answer = ask_ai(prompt)

        st.markdown(answer)

    st.divider()

    with st.expander("Supported Commands"):

        st.markdown(
            """
### Bar Charts
- Show country distribution
- Show category distribution
- Show region distribution

### Pie Charts
- Pie chart of country
- Pie chart of category

### Histograms
- Histogram of age
- Histogram of salary

### Line Charts
- Line chart of sales

### Scatter Plot
- Scatter plot
"""
        )