import pandas as pd
import os

def clean_data(file_path="sample_data/messy_data.csv"):
    """Clean messy biomedical data from CSV."""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)

    # Replace placeholders with NaN
    df.replace(["??", "N/A", "missing", "high"], pd.NA, inplace=True)

    # Convert Age to numeric, coerce errors
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    # Convert Weight to numeric
    df["Weight_kg"] = pd.to_numeric(df["Weight_kg"], errors="coerce")

    # Simple rule: replace "Blood_Pressure" text with NaN
    df.loc[~df["Blood_Pressure"].str.contains(r"^\d+/\d+$", na=True), "Blood_Pressure"] = pd.NA

    # Fill missing numerical values with mean
    for col in ["Age", "Height_cm", "Weight_kg"]:
        df[col] = df[col].fillna(df[col].mean())

    return df

def main():
    """Entry point for data cleaner."""
    print("\n🧹 Cleaning biomedical sample data...\n")
    df_clean = clean_data()
    if df_clean is not None:
        print(df_clean.head())
        # Save cleaned file
        cleaned_path = "sample_data/cleaned_data.csv"
        df_clean.to_csv(cleaned_path, index=False)
        print(f"📂 Cleaned data saved to {cleaned_path}")

if __name__ == "__main__":
    main()
