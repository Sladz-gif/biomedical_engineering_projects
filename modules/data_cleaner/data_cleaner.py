import pandas as pd
from modules.data_cleaner.sample_messy_data import generate_messy_data  # import messy data generator

def clean_data(df=None):
    """Clean messy biomedical data from a DataFrame."""
    
    # If no DataFrame is provided, generate messy data
    if df is None:
        df = generate_messy_data(save_csv=True)
    
    # Replace placeholders with NaN
    df.replace(["??", "N/A", "missing", "high"], pd.NA, inplace=True)

    # Convert Age and Weight to numeric
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Weight_kg"] = pd.to_numeric(df["Weight_kg"], errors="coerce")

    # Validate Blood_Pressure format
    df.loc[~df["Blood_Pressure"].str.contains(r"^\d+/\d+$", na=True), "Blood_Pressure"] = pd.NA

    # Fill missing numerical values with mean
    for col in ["Age", "Height_cm", "Weight_kg"]:
        df[col] = df[col].fillna(df[col].mean())

    return df

def main():
    print("\n🧹 Generating and cleaning biomedical sample data...\n")
    df_clean = clean_data()
    print(df_clean.head())
    # Save cleaned file
    cleaned_path = "sample_data/cleaned_data.csv"
    df_clean.to_csv(cleaned_path, index=False)
    print(f"📂 Cleaned data saved to {cleaned_path}")

if __name__ == "__main__":
    main()
