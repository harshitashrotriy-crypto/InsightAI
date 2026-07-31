import streamlit as st
import pandas as pd


def show():

    st.title("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        st.info("Please upload a dataset.")
        return

    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

    except Exception as e:
        st.error(e)
        return

    st.session_state["df"] = df

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", int(df.isna().sum().sum()))
    c4.metric("Duplicate Rows", int(df.duplicated().sum()))

    st.divider()

    st.subheader("📋 Data Profile")

    profile = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing": df.isnull().sum().values,
        "Unique": df.nunique().values,
    })

    st.dataframe(profile, use_container_width=True)

    st.subheader("Memory Usage")

    memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

    st.info(f"{memory:.2f} MB")