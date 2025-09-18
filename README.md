```markdown
# Biomedical Engineering Projects Portfolio

This repository contains a collection of biomedical engineering tools and sample projects, including:

## Projects/Modules

1. **Data Cleaner**  
   - Cleans messy biomedical data from CSV files.  
   - Generates sample messy data for testing.

2. **DICOM Metadata Extractor**  
   - Extracts clinically relevant metadata from DICOM files.  
   - Saves metadata to CSV and JSON formats.

3. **DNA/Protein Analyzer**  
   - Generates sample DNA sequences.  
   - Computes GC content, RNA transcription, protein translation, and motif counts.

4. **Dose-Response Curve Fitter**  
   - Generates sample dose-response datasets.  
   - Fits Hill equation to experimental data.  
   - Plots and saves dose-response curves.

5. **ECG Analyzer**  
   - Generates sample ECG data.  
   - Detects R-peaks, calculates heart rate, and plots ECG signals.

6. **Clinical Data Statistical Analysis**  
   - Generates sample clinical datasets with treatment and control groups.  
   - Performs summary statistics and t-tests.

## Web Integration

- Flask-based API (`app.py`) exposes all modules as endpoints.  
- Plots are served via `/plot/<plot_name>` route.

## Requirements

```

numpy
scipy
matplotlib
pandas
biopython
pydicom
Pillow
Flask

````

## Usage

- Run locally:  
```bash
python main.py
````

* Run API server:

```bash
python app.py
```

```
```
