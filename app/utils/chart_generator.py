import pandas as pd
import plotly.express as px


def find_column(df, query):

    query = query.lower()

    for col in df.columns:
        if col.lower() in query:
            return col

    return None


def detect_chart_type(query):

    query = query.lower()

    if "pie" in query:
        return "pie"

    if "hist" in query or "distribution" in query:
        return "histogram"

    if "line" in query or "trend" in query:
        return "line"

    if "scatter" in query:
        return "scatter"

    return "bar"


def generate_chart(df, query):

    chart_type = detect_chart_type(query)

    column = find_column(df, query)

    if column is None:
        return None, None, "I couldn't identify a matching column."

    summary = ""

    # ----------------------------
    # BAR CHART
    # ----------------------------
    if chart_type == "bar":

        counts = (
            df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [column, "Count"]

        fig = px.bar(
            counts,
            x=column,
            y="Count",
            title=f"{column} Distribution"
        )

        summary = counts.to_string(index=False)

        return fig, f"{column} Distribution", summary

    # ----------------------------
    # PIE CHART
    # ----------------------------
    if chart_type == "pie":

        counts = (
            df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [column, "Count"]

        fig = px.pie(
            counts,
            names=column,
            values="Count",
            title=f"{column} Distribution"
        )

        summary = counts.to_string(index=False)

        return fig, f"{column} Distribution", summary

    # ----------------------------
    # HISTOGRAM
    # ----------------------------
    if chart_type == "histogram":

        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                None,
                None,
                f"{column} is not numeric. Histogram cannot be created."
            )

        fig = px.histogram(
            df,
            x=column,
            title=f"{column} Distribution"
        )

        summary = df[column].describe().to_string()

        return fig, f"{column} Distribution", summary

    # ----------------------------
    # LINE CHART
    # ----------------------------
    if chart_type == "line":

        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                None,
                None,
                f"{column} is not numeric. Line chart cannot be created."
            )

        fig = px.line(
            df,
            y=column,
            title=f"{column} Trend"
        )

        summary = df[column].describe().to_string()

        return fig, f"{column} Trend", summary

    # ----------------------------
    # SCATTER
    # ----------------------------
    if chart_type == "scatter":

        numeric = df.select_dtypes(include="number").columns.tolist()

        if len(numeric) < 2:

            return (
                None,
                None,
                "Scatter plot requires at least two numeric columns."
            )

        fig = px.scatter(
            df,
            x=numeric[0],
            y=numeric[1],
            title=f"{numeric[0]} vs {numeric[1]}"
        )

        summary = df[numeric].describe().to_string()

        return fig, f"{numeric[0]} vs {numeric[1]}", summary

    return None, None, "Unable to generate chart."