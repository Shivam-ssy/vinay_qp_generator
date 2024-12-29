import pdfplumber

def extract_pdf_content(file_path):
    with pdfplumber.open(file_path) as pdf:
        content = ""
        for page in pdf.pages:
            content += page.extract_text()
    return content
