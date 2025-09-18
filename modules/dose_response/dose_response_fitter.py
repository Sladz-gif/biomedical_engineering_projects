
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sample_dose_response import generate_sample_dose_response

def hill_equation(dose, ec50, slope):
    """Sigmoidal dose-response function"""
    return 100 / (1 + (ec50 / dose) ** slope)

def fit_dose_response(data_file="sample_dose_response.csv", results_file="fitted_results.csv", save_path=None):
    """
    Fits a dose-response curve (Hill equation) to experimental data.
    Saves fitted EC50 and slope to CSV.
    Optionally saves the plot to `save_path`.
    Returns fitted EC50 and slope.
    """
    # Load data
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(" No dataset found, generating a new one...")
        df = generate_sample_dose_response(data_file)

    x = df["Dose_uM"].values
    y = df["Response_percent"].values

    # Curve fitting
    popt, _ = curve_fit(hill_equation, x, y, p0=[10, 1])  # initial guess
    ec50, slope = popt

    print(f" Fitted EC50: {ec50:.2f} µM")
    print(f" Fitted Hill Slope: {slope:.2f}")

    # Save fitted parameters
    pd.DataFrame({"EC50_uM": [ec50], "Hill_Slope": [slope]}).to_csv(results_file, index=False)
    print(f" Fitted results saved to {results_file}")

    # Plot experimental data + fitted curve
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label="Experimental Data", color="blue")
    x_fit = np.logspace(np.log10(min(x)), np.log10(max(x)), 100)
    y_fit = hill_equation(x_fit, ec50, slope)
    plt.plot(x_fit, y_fit, label="Fitted Curve", color="red")
    plt.xscale("log")
    plt.xlabel("Dose (µM)")
    plt.ylabel("Response (%)")
    plt.title("Dose-Response Curve Fit")
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()
        print(f" Plot saved to {save_path}")
    else:
        plt.show()

    return ec50, slope
