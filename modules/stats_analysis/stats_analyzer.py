
import pandas as pd
from scipy import stats
from modules.stat_analysis.sample_clinical import generate_sample_clinical_data

def analyze_clinical_data(input_file="sample_clinical_data.csv"):
    """
    Performs summary statistics and hypothesis testing on clinical dataset.
    """
    try:
        df = pd.read_csv(input_file)
        print(f" Loaded dataset: {input_file}")
    except FileNotFoundError:
        print(" No dataset found, generating new sample data...")
        df = generate_sample_clinical_data(input_file)
    
    print("\n First 5 rows of dataset:")
    print(df.head())
    
    # Summary statistics
    summary = df.groupby("Group")["Measurement"].describe()
    print("\n Summary Statistics by Group:")
    print(summary)
    
    # Split groups
    treatment = df[df["Group"] == "Treatment"]["Measurement"]
    control = df[df["Group"] == "Control"]["Measurement"]
    
    # T-test
    t_stat, p_val = stats.ttest_ind(treatment, control, equal_var=False)
    print("\n Hypothesis Test (t-test, unequal variance):")
    print(f"T-statistic: {t_stat:.3f}, P-value: {p_val:.4f}")
    
    if p_val < 0.05:
        print(" Significant difference between Treatment and Control groups.")
    else:
        print(" No significant difference detected.")
    
    return summary, (t_stat, p_val)

if __name__ == "__main__":
    analyze_clinical_data()
