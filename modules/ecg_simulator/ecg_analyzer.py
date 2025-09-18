
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks
from .ecg_generator import generate_ecg, SAMPLE_FOLDER

def analyze_ecg(file_path=None, save_path=None):
    """
    Analyze ECG signal to detect peaks and estimate heart rate.
    Optionally save plot to save_path instead of displaying.
    """
    # Load sample ECG or generate new one
    if file_path is None:
        df, file_path = generate_ecg()
    else:
        df = pd.read_csv(file_path)

    signal = df["ecg"].values
    time = df["time_sec"].values

    # Peak detection (R-peaks)
    peaks, _ = find_peaks(signal, distance=50, height=0.5)  

    rr_intervals = np.diff(time[peaks])
    avg_rr = np.mean(rr_intervals) if len(rr_intervals) > 0 else np.nan
    heart_rate = 60.0 / avg_rr if avg_rr > 0 else np.nan

    results = {
        "file_analyzed": file_path,
        "num_beats": len(peaks),
        "avg_rr_interval_sec": round(float(avg_rr), 3) if not np.isnan(avg_rr) else None,
        "estimated_heart_rate_bpm": round(float(heart_rate), 1) if not np.isnan(heart_rate) else None,
    }

    # Plot
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, label="ECG Signal")
    plt.plot(time[peaks], signal[peaks], "ro", label="Detected Beats")
    plt.title("ECG Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()
        print(f" ECG plot saved to {save_path}")
    else:
        plt.show()

    return results
