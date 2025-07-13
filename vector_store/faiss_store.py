import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
faiss_index = {}
user_docs = {}

def add_chunks_to_faiss(user_id: str, chunks: list[str]):
    embeddings = model.encode(chunks)
    if user_id not in faiss_index:
        faiss_index[user_id] = faiss.IndexFlatL2(384)
        user_docs[user_id] = []
    faiss_index[user_id].add(np.array(embeddings).astype("float32"))
    user_docs[user_id].extend(chunks)

def search_faiss(user_id: str, query: str, top_k=3):
    if user_id not in faiss_index:
        return []
    q_emb = model.encode([query]).astype("float32")
    D, I = faiss_index[user_id].search(q_emb, top_k)
    return [user_docs[user_id][i] for i in I[0] if i < len(user_docs[user_id])]
