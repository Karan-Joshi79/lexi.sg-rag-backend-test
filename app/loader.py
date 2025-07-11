# app/loader.py
import os
import fitz  # PyMuPDF for PDF
import docx

def load_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def load_documents(directory):
    docs = []
    for root, dirs, files in os.walk(directory):  # Walk subfolders
        for fname in files:
            path = os.path.join(root, fname)
            if fname.endswith(".pdf"):
                content = load_pdf(path)
            elif fname.endswith(".doc") or fname.endswith(".docx"):
                try:
                    content = load_docx(path)
                except:
                    continue
            else:
                continue

            # Split into chunks
            chunks = [content[i:i+500] for i in range(0, len(content), 500)]
            for i, chunk in enumerate(chunks):
                docs.append({
                    "text": chunk,
                    "metadata": {
                        "source": fname,
                        "chunk_id": i
                    }
                })
    return docs
