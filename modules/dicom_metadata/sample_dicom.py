# modules/dicom_metadata/sample_dicom.py
import pydicom
from pydicom.dataset import Dataset, FileDataset
import datetime
import tempfile
import os
import random

def generate_sample_dicom(file_path="sample.dcm"):
    """
    Generates a fake DICOM file with randomized metadata for testing.
    """
    # Temporary file meta information
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = pydicom.uid.SecondaryCaptureImageStorage
    file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    file_meta.ImplementationClassUID = pydicom.uid.generate_uid()

    # Create dataset
    ds = FileDataset(file_path, {}, file_meta=file_meta, preamble=b"\0" * 128)

    # Add metadata fields
    ds.PatientName = f"Test^Patient{random.randint(100,999)}"
    ds.PatientID = str(random.randint(10000, 99999))
    ds.PatientBirthDate = datetime.date(
        random.randint(1960, 2000), random.randint(1, 12), random.randint(1, 28)
    ).strftime("%Y%m%d")
    ds.PatientSex = random.choice(["M", "F"])
    ds.StudyDate = datetime.date.today().strftime("%Y%m%d")
    ds.Modality = random.choice(["CT", "MR", "XR"])
    ds.Manufacturer = random.choice(["Siemens", "GE Healthcare", "Philips"])
    ds.StudyDescription = "Synthetic DICOM Study"

    # Save to file
    ds.save_as(file_path)
    print(f"📂 Sample DICOM file created: {file_path}")
    return file_path

if __name__ == "__main__":
    generate_sample_dicom()
