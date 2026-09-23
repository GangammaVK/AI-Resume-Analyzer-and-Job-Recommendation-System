from io import BytesIO
from pypdf import PdfReader
from docx import Document

def extract_pdf_text(file_bytes):
    reader = PdfReader(BytesIO(file_bytes))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        if text.strip():
            pages.append(text)
    return "\n".join(pages)

def extract_docx_text(file_bytes):
    document = Document(BytesIO(file_bytes))
    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)

def extract_text_from_file(uploaded_file):
    data = uploaded_file.getvalue()
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        return extract_pdf_text(data)
    if name.endswith(".docx"):
        return extract_docx_text(data)

    raise ValueError("Only PDF and DOCX files are supported.")
