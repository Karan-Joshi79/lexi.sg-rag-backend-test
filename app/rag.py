from app.model import embedding_model, load_faiss_index
import numpy as np

index, meta = load_faiss_index()

def search_docs(query, top_k=3):
    query_vec = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)

    results = []
    for idx in indices[0]:
        results.append({
            "text": meta["texts"][idx],
            "source": meta["metadata"][idx]["source"]
        })
    return results

def generate_answer(query):
    docs = search_docs(query)
    combined = " ".join([doc["text"] for doc in docs])
    answer = f"Based on the retrieved documents, here’s a possible answer:\n\n{combined[:500]}..."

    return {
        "answer": answer,
        "citations": docs
    }
