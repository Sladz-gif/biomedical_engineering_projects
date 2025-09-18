import pandas as pd
import numpy as np
import random
import os

def generate_messy_data(num_rows=10, save_csv=True):
    """Generate randomized messy biomedical sample data."""
    random.seed()  # ensures different results each run

    data = {
        "Patient_ID": [f"P{str(i).zfill(3)}" for i in range(1, num_rows+1)],
        "Age": [random.choice([25, 30, None, "??", 40, "N/A"]) for _ in range(num_rows)],
        "Height_cm": [round(random.uniform(150, 190), 1) if random.random() > 0.2 else None for _ in range(num_rows)],
        "Weight_kg": [round(random.uniform(50, 100), 1) if random.random() > 0.2 else "missing" for _ in range(num_rows)],
        "Blood_Pressure": [random.choice(["120/80", "130/85", None, "high", "??"]) for _ in range(num_rows)],
    }

    df = pd.DataFrame(data)

    if save_csv:
        os.makedirs("sample_data", exist_ok=True)
        file_path = os.path.join("sample_data", "messy_data.csv")
        df.to_csv(file_path, index=False)
        print(f" New messy data saved to {file_path}")

    return df

def main():
    """Entry point for messy data generator."""
    print("\n Generating new messy biomedical sample data...\n")
    df = generate_messy_data()
    print(df.head())

if __name__ == "__main__":
    main()
