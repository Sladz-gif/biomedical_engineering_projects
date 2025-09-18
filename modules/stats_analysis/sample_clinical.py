# modules/stat_analysis/sample_clinical.py
import pandas as pd
import numpy as np
import random

def generate_sample_clinical_data(filename="sample_clinical_data.csv", n_patients=50):
    """
    Generates randomized clinical dataset with Treatment and Control groups.
    Saves to CSV for analysis.
    """
    np.random.seed(None)  # ensure different results each run
    
    patient_ids = [f"P{str(i).zfill(3)}" for i in range(1, n_patients + 1)]
    groups = np.random.choice(["Treatment", "Control"], size=n_patients, p=[0.5, 0.5])
    
    # Simulated biomarker/measurement values
    control_values = np.random.normal(loc=50, scale=10, size=n_patients)
    treatment_effect = np.random.normal(loc=10, scale=5, size=n_patients)
    values = [control_values[i] + (treatment_effect[i] if groups[i] == "Treatment" else 0) for i in range(n_patients)]
    
    data = pd.DataFrame({
        "Patient_ID": patient_ids,
        "Group": groups,
        "Measurement": np.round(values, 2)
    })
    
    data.to_csv(filename, index=False)
    print(f" Sample clinical dataset saved to {filename}")
    return data

if __name__ == "__main__":
    df = generate_sample_clinical_data()
    print(df.head())
