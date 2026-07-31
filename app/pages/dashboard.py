
import streamlit as st
import pandas as pd
import plotly.express as px


def show():

    st.title("📊 Executive Dashboard")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"].copy()

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    # =====================
    # Filters
    # =====================

    st.subheader("🎛 Dashboard Filters")

    if categorical:

        filter_column = st.selectbox(
            "Filter Dataset",
            ["None"] + categorical
        )

        if filter_column != "None":

            options = sorted(df[filter_column].dropna().unique())

            selected = st.multiselect(
                f"Select {filter_column}",
                options,
                default=options
            )

            if selected:
                df = df[df[filter_column].isin(selected)]

    st.divider()

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    # =====================
    # KPI Cards
    # =====================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Total Records", f"{len(df):,}")

    c2.metric("📋 Total Columns", len(df.columns))

    c3.metric("❌ Missing Values", int(df.isna().sum().sum()))

    c4.metric("🗂 Duplicate Rows", int(df.duplicated().sum()))

    st.divider()

    if not numeric:
        st.warning("No numeric columns available.")
        return

    left, right = st.columns(2)

    with left:
        x_axis = st.selectbox("Select X-axis", df.columns)

    with right:
        y_axis = st.selectbox("Select Y-axis", numeric)

    tabs = st.tabs([
        "📊 Bar",
        "📈 Line",
        "🥧 Pie",
        "📦 Histogram",
        "📉 Scatter"
    ])

    with tabs[0]:

        fig = px.bar(df, x=x_axis, y=y_axis)

        st.plotly_chart(fig, use_container_width=True)

    with tabs[1]:

        fig = px.line(df, x=x_axis, y=y_axis)

        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:

        if x_axis in categorical:

            counts = df[x_axis].value_counts().reset_index()

            counts.columns = [x_axis, "Count"]

            fig = px.pie(
                counts,
                names=x_axis,
                values="Count"
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("Pie chart requires a categorical column.")

    with tabs[3]:

        fig = px.histogram(
            df,
            x=y_axis,
            nbins=30
        )

        st.plotly_chart(fig, use_container_width=True)

    with tabs[4]:

        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("📋 Filtered Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )