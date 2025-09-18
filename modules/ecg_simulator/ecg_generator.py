import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime
import os

# Folder for saving synthetic ECG samples
SAMPLE_FOLDER = os.path.join(os.path.dirname(__file__), "samples")
os.makedirs(SAMPLE_FOLDER, exist_ok=True)


def generate_ecg(duration=10, fs=250, noise_level=0.05):
    """
    Generate synthetic ECG-like signal with noise.

    Args:
        duration (int): Signal duration in seconds
        fs (int): Sampling frequency (Hz)
        noise_level (float): Noise amplitude

    Returns:
        pd.DataFrame: ECG signal with timestamps
    """
    t = np.linspace(0, duration, duration * fs)

    # --- Generate synthetic ECG waveform ---
    # Base heartbeat frequency (60–100 bpm -> 1–1.67 Hz)
    hr = random.randint(60, 100)
    f = hr / 60  

    # ECG shape approximation using sinusoids + Gaussian peaks
    ecg_wave = (
        0.6 * np.sin(2 * np.pi * f * t) +  # P/T wave
        0.9 * np.sign(np.sin(2 * np.pi * f * t)) +  # QRS spike
        0.1 * np.random.randn(len(t))  # baseline noise
    )

    # Add adjustable random noise
    ecg_wave += noise_level * np.random.randn(len(t))

    # Normalize signal
    ecg_wave = (ecg_wave - np.mean(ecg_wave)) / np.std(ecg_wave)

    # Save as DataFrame
    df = pd.DataFrame({"time_sec": t, "ecg": ecg_wave})

    # Save CSV with timestamped name
    filename = os.path.join(SAMPLE_FOLDER, f"ecg_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    df.to_csv(filename, index=False)

    return df, filename


if __name__ == "__main__":
    # Example usage
    signal, filepath = generate_ecg(duration=5, noise_level=0.1)
    print(f"Synthetic ECG saved to {filepath}")

    # Plot for visualization
    plt.figure(figsize=(10, 4))
    plt.plot(signal["time_sec"], signal["ecg"], label="ECG Signal")
    plt.title("Synthetic ECG Signal (Sample)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()
    plt.show()
