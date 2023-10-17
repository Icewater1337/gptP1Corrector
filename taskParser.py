import os
import zipfile
from pathlib import Path

import PyPDF2


def load_java_files(parent_directory):
    zip_contents_dict = {}

    for root, dirs, files in os.walk(parent_directory):
        zip_files = [f for f in files if f.lower().endswith('.zip')]

        if zip_files:
            folder_name = Path(root).name
            extracted_contents = {}

            for zip_file in zip_files:
                zip_file_path = os.path.join(root, zip_file)
                with zipfile.ZipFile(zip_file_path, 'r') as z:
                    for filename in z.namelist():
                        with z.open(filename) as f:
                            # Read the content of the file and decode it to a string
                            content = f.read().decode('utf-8', errors='ignore')
                            extracted_contents[filename] = content

            zip_contents_dict[folder_name] = extracted_contents

    return zip_contents_dict









def extract_text_from_first_pdf(directory):
    all_files = os.listdir(directory)

    pdf_files = [file for file in all_files if file.lower().endswith('.pdf')]

    if not pdf_files:
        return ""

    first_pdf_path = os.path.join(directory, pdf_files[0])

    with open(first_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text

