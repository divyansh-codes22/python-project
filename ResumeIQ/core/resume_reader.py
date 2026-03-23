# resume_reader.py
# This module handles reading resumes in PDF and TXT formats

import os
from PyPDF2 import PdfReader

def read_resume(file_path):
    """
    Reads resume content from PDF or TXT file
    Returns extracted raw text
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found")

    # Check file extension
    extension = file_path.split('.')[-1].lower()

    if extension == "pdf":
        return read_pdf(file_path)

    elif extension == "txt":
        return read_txt(file_path)

    else:
        raise ValueError("Unsupported file format. Only PDF and TXT allowed.")


def read_pdf(file_path):
    """
    Extracts text from a PDF resume
    """

    text = ""
    reader = PdfReader(file_path)

    for page in reader.pages:
        text += page.extract_text() + " "

    return text


def read_txt(file_path):
    """
    Reads text from a TXT resume
    """

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        text = file.read()

    return text