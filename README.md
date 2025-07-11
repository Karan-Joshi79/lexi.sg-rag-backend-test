
# Lexi RAG Backend – FastAPI Implementation

A Retrieval-Augmented Generation (RAG) backend for answering legal queries with source citations from real legal documents (PDF/DOCX).

---

## ✅ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Karan-Joshi79/lexi.sg-rag-backend-test.git
   cd lexi.sg-rag-backend-test
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip setuptools
   pip install -r requirements.txt
   ```

4. **Add legal documents**
   - Place all `.pdf` or `.docx` files inside the `legal_docs/` folder (create if missing).
   - Subfolders like `legal_docs/case1/` are supported.

5. **Build FAISS index**
   ```bash
   python -m scripts.build_faiss_index
   ```

6. **Run the API server**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 How to Test the API

1. Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Find the `/query` endpoint.
3. Click "Try it out", then enter a query like:

```json
{
  "query": "Is an insurance company liable to pay compensation if a transport vehicle involved in an accident was being used without a valid permit?"
}
```

4. Click **Execute** to test.

---

## 💡 Example Input / Output

**Input (POST `/query`):**

```json
{
  "query": "Is an insurance company liable to pay compensation if a transport vehicle involved in an accident was being used without a valid permit?"
}
```

**Output:**

```json
{
  "answer": "Based on the retrieved documents, here’s a possible answer:\n\n[Relevant answer text]",
  "citations": [
    {
      "text": "Use of a vehicle in a public place without a permit is a fundamental statutory infraction...",
      "source": "InsuranceCase.docx"
    },
    {
      "text": "The insurer shall be entitled to recover the same from the owner and the driver.",
      "source": "Judgment2021.pdf"
    }
  ]
}
```

---

✅ This project uses:
- Sentence Transformers for embeddings  
- FAISS for vector search  
- FastAPI for serving endpoints  
- PyMuPDF and python-docx for document parsing

