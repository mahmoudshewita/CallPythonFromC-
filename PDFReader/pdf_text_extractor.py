import fitz  # type: ignore # PyMuPDF
# import os
# print(os.environ['PATH'])

def extractTextFromPDF(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def hello():
    return "Hello from PYTHON !"