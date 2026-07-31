import streamlit as st
import plotly.express as px


def show():

    st.title("🔥 Correlation Heatmap")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        st.warning("Need at least 2 numeric columns to calculate correlation.")
        return

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto",
        title="Correlation Matrix"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Correlation Table")

    st.dataframe(
        corr.round(2),
        use_container_width=True
    )