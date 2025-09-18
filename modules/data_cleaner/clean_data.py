
import pandas as pd
import os

def clean_data(file_path="sample_data/messy_data.csv"):
    """Clean messy biomedical data from CSV."""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)
    df.replace(["??", "N/A", "missing", "high"], pd.NA, inplace=True)
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Weight_kg"] = pd.to_numeric(df["Weight_kg"], errors="coerce")
    df.loc[~df["Blood_Pressure"].str.contains(r"^\d+/\d+$", na=True), "Blood_Pressure"] = pd.NA
    for col in ["Age", "Height_cm", "Weight_kg"]:
        df[col] = df[col].fillna(df[col].mean())
    return df
