# app/model.py
import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
save_path = "embeddings"

def load_faiss_index():
    index_path = os.path.join(save_path, "index.faiss")
    meta_path = os.path.join(save_path, "meta.json")

    if not os.path.exists(index_path):
        raise FileNotFoundError(f"FAISS index not found at {index_path}")
    if not os.path.exists(meta_path):
        raise FileNotFoundError(f"Metadata not found at {meta_path}")

    index = faiss.read_index(index_path)
    
    with open(meta_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return index, metadata
