# modules/dose_response/sample_dose_response.py
import numpy as np
import pandas as pd
import random

def generate_sample_dose_response(file_path="sample_dose_response.csv"):
    """
    Generates a randomized sample dose-response dataset and saves as CSV.
    Columns: Dose (µM), Response (% of max effect)
    """
    np.random.seed()  # ensures different results each run

    # Define dose range (log scale, common in pharmacology)
    doses = np.logspace(-2, 2, num=10)  # 0.01 µM to 100 µM

    # True EC50 (hidden parameter) and Hill slope
    true_ec50 = random.uniform(5, 25)      # µM
    hill_slope = random.uniform(0.8, 1.5)

    # Logistic function for response
    def sigmoid(d, ec50, slope):
        return 100 / (1 + (ec50 / d) ** slope)

    responses = [sigmoid(d, true_ec50, hill_slope) for d in doses]

    # Add experimental noise
    noisy_responses = responses + np.random.normal(0, 5, len(responses))

    df = pd.DataFrame({
        "Dose_uM": doses,
        "Response_percent": noisy_responses
    })

    df.to_csv(file_path, index=False)
    print(f" Sample dose-response data saved to {file_path}")
    return df

if __name__ == "__main__":
    df = generate_sample_dose_response()
    print(df.head())
