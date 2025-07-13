from fastapi import APIRouter, UploadFile, File, Form
from core.loader import parse_csv_and_chunk, chunk_text
from vector_store.faiss_store import add_chunks_to_faiss

router = APIRouter()

@router.post("/upload_docs")
def upload_docs(user_id: str = Form(...), files: list[UploadFile] = File(...)):
    doc_names = []
    all_chunks = []
    for file in files:
        content = file.file.read().decode("utf-8")
        doc_names.append(file.filename)
        chunks = parse_csv_and_chunk(content) if file.filename.endswith(".csv") else chunk_text(content)
        all_chunks.extend(chunks)

    add_chunks_to_faiss(user_id, all_chunks)
    return {"uploaded_files": doc_names, "chunks_indexed": len(all_chunks)}
