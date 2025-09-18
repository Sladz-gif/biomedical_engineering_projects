
import os
import json
import pandas as pd
import pydicom
from .sample_dicom import generate_sample_dicom  # relative import for deploy

# Clinically relevant DICOM fields
CLINICAL_FIELDS = [
    "PatientName",
    "PatientID",
    "PatientBirthDate",
    "PatientSex",
    "StudyDate",
    "StudyDescription",
    "Modality",
    "Manufacturer",
    "InstitutionName",
    "BodyPartExamined",
    "SliceThickness",
    "KVP",
    "RepetitionTime",
    "EchoTime",
    "PixelSpacing",
    "Rows",
    "Columns",
]

def extract_dicom_metadata(
    dicom_file="sample.dcm",
    csv_file="dicom_metadata.csv",
    json_file="dicom_metadata.json"
):
    """
    Extract clinically relevant metadata from a DICOM file
    and save it to CSV and JSON.
    """
    # If DICOM file is missing, generate a sample
    if not os.path.exists(dicom_file):
        print(" No DICOM file found, generating a sample one...")
        dicom_file = generate_sample_dicom()

    # Read the DICOM file
    ds = pydicom.dcmread(dicom_file)

    # Extract metadata
    metadata = {}
    for field in CLINICAL_FIELDS:
        metadata[field] = str(getattr(ds, field)) if hasattr(ds, field) else pd.NA

    # Save to CSV
    pd.DataFrame([metadata]).to_csv(csv_file, index=False)
    print(f" Clinically relevant metadata saved to {csv_file}")

    # Save to JSON
    with open(json_file, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f" Clinically relevant metadata saved to {json_file}")

    return metadata

def main():
    """Entry point for DICOM metadata extraction."""
    print("\n🩺 Extracting DICOM metadata...\n")
    meta = extract_dicom_metadata()
    print(" Metadata Preview:")
    print(meta)

if __name__ == "__main__":
    main()
