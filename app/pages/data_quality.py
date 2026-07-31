import streamlit as st
import pandas as pd


def show():

    st.title("🧹 Data Quality Report")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["df"]

    st.subheader("📋 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    with col4:
        st.metric("Duplicate Rows", int(df.duplicated().sum()))

    st.divider()

    st.subheader("📊 Column Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(info_df, use_container_width=True)

    st.divider()

    st.subheader("❗ Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    missing_df = missing_df.sort_values(
        by="Missing Values",
        ascending=False
    )

    st.dataframe(missing_df, use_container_width=True)

    st.divider()

    st.subheader("💾 Memory Usage")

    memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

    st.metric(
        "Memory Used (MB)",
        f"{memory:.2f}"
    )

    st.divider()

    st.subheader("🔍 Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )