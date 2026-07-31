import pandas as pd


def generate_summary(df):

    numeric = df.select_dtypes(include="number")
    categorical = df.select_dtypes(exclude="number")

    summary = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "column_names": list(df.columns),
        "numeric_columns": list(numeric.columns),
        "categorical_columns": list(categorical.columns),
        "top_values": {},
        "statistics": ""
    }

    for col in categorical.columns:
        summary["top_values"][col] = (
            df[col]
            .value_counts()
            .head(5)
            .to_dict()
        )

    if not numeric.empty:
        summary["statistics"] = numeric.describe().to_string()
    else:
        summary["statistics"] = "No numeric columns found."

    return summary