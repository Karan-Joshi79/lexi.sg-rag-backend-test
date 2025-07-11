# scripts/build_faiss_index.py
from app.loader import load_documents
from sentence_transformers import SentenceTransformer
import faiss, os, json
import numpy as np

print("🔍 Loading documents...")
docs = load_documents("legal_docs")
print(f"✅ Loaded {len(docs)} documents.")

texts = [d["text"] for d in docs]
metas = [d["metadata"] for d in docs]

if not texts:
    print("❌ No texts found. Aborting.")
    exit()

print("⚙️ Generating embeddings...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)

print(f"✅ Embeddings shape: {embeddings.shape}")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

os.makedirs("embeddings", exist_ok=True)
faiss.write_index(index, "embeddings/index.faiss")

with open("embeddings/meta.json", "w", encoding="utf-8") as f:
    json.dump({"texts": texts, "metadata": metas}, f, ensure_ascii=False, indent=2)

print("✅ FAISS index and meta.json saved successfully.")
