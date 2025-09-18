# main.py
import os
import sys

# --- Import all modules ---
from modules.data_cleaner import clean_data
from modules.data_cleaner.sample_messy_data import generate_messy_data
from modules.dicom_metadata.dicom_extractor import extract_dicom_metadata
from modules.dna_analyzer import analyze_dna
from modules.sample_dna import generate_sample_dna
from modules.dose_response.dose_response_fitter import fit_dose_response
from modules.dose_response.sample_dose_response import generate_sample_dose_response
from modules.ecg_analyzer import analyze_ecg
from modules.ecg_generator import generate_ecg
from modules.stat_analysis.stats_analyzer import analyze_clinical_data
from modules.stat_analysis.sample_clinical import generate_sample_clinical_data

def print_menu():
    print("\n" + "="*60)
    print(" 🧪 BIOMEDICAL ENGINEERING TOOLS PORTFOLIO ")
    print("="*60)
    print("Select a project/tool to run:\n")
    print("1. Biomedical Data Formatter & Cleaner")
    print("2. Medical Image Metadata Extractor (DICOM)")
    print("3. Protein/DNA Sequence Analyzer")
    print("4. Dose-Response Curve Fitter")
    print("5. Medical Device Data Simulator (ECG)")
    print("6. Basic Statistical Analysis for a Clinical Dataset")
    print("0. Exit\n")

def ask_plot_option():
    """Ask the user if they want to display plots for visual tools."""
    choice = input("Do you want to display plots? (y/n): ").strip().lower()
    return choice == "y"

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (0-6): ").strip()
        
        try:
            if choice == "0":
                print("Exiting portfolio. Goodbye! 👋")
                break
            
            elif choice == "1":
                print("\n🧹 Running Biomedical Data Cleaner...\n")
                generate_messy_data()
                cleaned_df = clean_data()
                if cleaned_df is not None:
                    print(cleaned_df.head())
            
            elif choice == "2":
                print("\n🩻 Running DICOM Metadata Extractor...\n")
                metadata = extract_dicom_metadata()
                print(metadata)
            
            elif choice == "3":
                print("\n🧬 Running DNA Sequence Analyzer...\n")
                dna_seq = generate_sample_dna(length=60)
                print(f"Generated DNA Sequence:\n{dna_seq}\n")
                results = analyze_dna(dna_seq)
                for key, value in results.items():
                    print(f"{key}: {value}")
            
            elif choice == "4":
                print("\n💊 Running Dose-Response Curve Fitter...\n")
                generate_sample_dose_response()
                show_plot = ask_plot_option()
                ec50, slope = fit_dose_response(plot=show_plot)
                print(f"\nFitted EC50: {ec50:.2f} µM, Hill Slope: {slope:.2f}")
            
            elif choice == "5":
                print("\n❤️ Running ECG Analyzer...\n")
                df, file_path = generate_ecg()
                show_plot = ask_plot_option()
                results = analyze_ecg(file_path, plot=show_plot)
                print("\nECG Analysis Results:")
                for key, value in results.items():
                    print(f"{key}: {value}")
            
            elif choice == "6":
                print("\n📊 Running Clinical Data Statistical Analysis...\n")
                generate_sample_clinical_data()
                summary, (t_stat, p_val) = analyze_clinical_data()
            
            else:
                print("❌ Invalid choice. Please enter a number between 0-6.")
        except Exception as e:
            print(f"⚠️ An error occurred while running the tool: {e}")

if __name__ == "__main__":
    main()
