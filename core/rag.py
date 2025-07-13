from vector_store.faiss_store import search_faiss

def get_relevant_context(user_id: str, query: str, top_k: int = 3):
    return search_faiss(user_id, query, top_k)
