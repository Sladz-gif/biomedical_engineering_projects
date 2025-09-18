# app.py
from flask import Flask, jsonify, send_file
import os

# --- Import all modules ---
from modules.dicom_metadata.dicom_extractor import extract_dicom_metadata
from modules.dna_analyzer import analyze_dna
from modules.sample_dna import generate_sample_dna
from modules.dose_response.dose_response_fitter import fit_dose_response
from modules.dose_response.sample_dose_response import generate_sample_dose_response
from modules.ecg_analyzer import analyze_ecg
from modules.ecg_generator import generate_ecg
from modules.stat_analysis.stats_analyzer import analyze_clinical_data
from modules.stat_analysis.sample_clinical import generate_sample_clinical_data

# --- Create folders ---
PLOT_FOLDER = "static/plots"
os.makedirs(PLOT_FOLDER, exist_ok=True)

app = Flask(__name__)

# --- Routes ---
@app.route("/")
def index():
    return "<h1>Biomedical Engineering Portfolio API</h1>" \
           "<p>Available routes: /dicom_metadata, /dna_analyzer, /dose_response, /ecg, /clinical_stats</p>"

# 1. DICOM Metadata
@app.route("/dicom_metadata")
def run_dicom_metadata():
    meta = extract_dicom_metadata()
    return jsonify(meta)

# 2. DNA Analyzer
@app.route("/dna_analyzer")
def run_dna_analyzer():
    seq = generate_sample_dna(length=60)
    results = analyze_dna(seq)
    results["Generated_Sequence"] = seq
    return jsonify(results)

# 3. Dose-Response Curve Fitter
@app.route("/dose_response")
def run_dose_response():
    generate_sample_dose_response()
    plot_path = os.path.join(PLOT_FOLDER, "dose_response.png")
    ec50, slope = fit_dose_response(save_path=plot_path)
    return jsonify({
        "EC50_uM": ec50,
        "Hill_Slope": slope,
        "plot_url": f"/plot/dose_response"
    })

# 4. ECG Analyzer
@app.route("/ecg")
def run_ecg():
    df, file_path = generate_ecg()
    plot_path = os.path.join(PLOT_FOLDER, "ecg.png")
    results = analyze_ecg(file_path=file_path, save_path=plot_path)
    return jsonify({
        **results,
        "plot_url": f"/plot/ecg"
    })

# Serve plots
@app.route("/plot/<plot_name>")
def serve_plot(plot_name):
    plot_file = os.path.join(PLOT_FOLDER, f"{plot_name}.png")
    if os.path.exists(plot_file):
        return send_file(plot_file, mimetype="image/png")
    return jsonify({"error": "Plot not found"})

# 5. Clinical Data Statistics
@app.route("/clinical_stats")
def run_clinical_stats():
    generate_sample_clinical_data()
    summary, (t_stat, p_val) = analyze_clinical_data()
    return jsonify({
        "summary": summary.to_dict(),
        "t_statistic": t_stat,
        "p_value": p_val
    })

if __name__ == "__main__":
    app.run(debug=True)
