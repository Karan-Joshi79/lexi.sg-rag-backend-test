# Lexi RAG Backend Test

This is a FastAPI backend service that answers legal queries using Retrieval-Augmented Generation (RAG) and real legal documents.

### 🚀 Features
- Accepts a legal query via `POST /query`
- Retrieves relevant document chunks using FAISS
- Generates an answer using top chunks
- Returns citations with snippet + file source

### 📁 Project Structure
- `app/` – FastAPI app, loader, rag logic
- `scripts/` – Script to generate FAISS index
- `legal_docs/` – Your uploaded .pdf/.docx documents
- `embeddings/` – Generated index + metadata
