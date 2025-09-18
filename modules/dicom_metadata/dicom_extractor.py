# modules/dicom_metadata/dicom_extractor.py
import pydicom
import pandas as pd
import json
from sample_dicom import generate_sample_dicom

# Define clinically relevant fields
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
    Extracts clinically relevant metadata from a DICOM file 
    and saves to CSV and JSON.
    """
    try:
        ds = pydicom.dcmread(dicom_file)
    except FileNotFoundError:
        print("⚠️ No DICOM file found, generating a sample one...")
        dicom_file = generate_sample_dicom()
        ds = pydicom.dcmread(dicom_file)

    metadata = {}
    for field in CLINICAL_FIELDS:
        if hasattr(ds, field):
            metadata[field] = str(getattr(ds, field))

    # Save to CSV
    pd.DataFrame([metadata]).to_csv(csv_file, index=False)
    print(f"💾 Clinically relevant metadata saved to {csv_file}")

    # Save to JSON
    with open(json_file, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"💾 Clinically relevant metadata saved to {json_file}")

    return metadata

if __name__ == "__main__":
    generate_sample_dicom()   # always refresh with a new DICOM
    meta = extract_dicom_metadata()
    print("✅ Extracted Clinically Relevant Metadata Preview:")
    print(meta)
