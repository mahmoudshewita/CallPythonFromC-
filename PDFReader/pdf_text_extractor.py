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

#print(extract_text("C:\\Applications\\PDF_Reader\\d147e1dd-b4a3-4461-a54e-fe747c37bbd6.pdf"));