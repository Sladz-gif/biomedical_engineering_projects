import pandas as pd
from .sample_messy_data import generate_messy_data

def clean_data(df=None):
    """
    Clean messy biomedical data from a DataFrame.

    Steps:
    - Generate messy data if no DataFrame is provided
    - Replace invalid placeholders with NaN
    - Convert numeric columns
    - Validate Blood_Pressure format
    - Fill missing numeric values with column mean
    """
    # Generate sample messy data if none provided
    if df is None:
        df = generate_messy_data(save_csv=True)

    # Replace common placeholders with NaN
    df.replace(["??", "N/A", "missing", "high"], pd.NA, inplace=True)

    # Convert numeric columns
    for col in ["Age", "Weight_kg", "Height_cm"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Validate Blood_Pressure format: should be "systolic/diastolic"
    if "Blood_Pressure" in df.columns:
        df.loc[~df["Blood_Pressure"].str.contains(r"^\d+/\d+$", na=True), "Blood_Pressure"] = pd.NA

    # Fill missing numeric values with mean
    for col in ["Age", "Height_cm", "Weight_kg"]:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].mean())

    return df

# Optional: run as script
if __name__ == "__main__":
    print("\n🧹 Generating and cleaning biomedical sample data...\n")
    df_clean = clean_data()
    print(df_clean.head())

    # Save cleaned file
    import os
    os.makedirs("sample_data", exist_ok=True)
    cleaned_path = "sample_data/cleaned_data.csv"
    df_clean.to_csv(cleaned_path, index=False)
    print(f"📂 Cleaned data saved to {cleaned_path}")
