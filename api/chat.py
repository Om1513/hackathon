from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schema import ChatRequest, ChatResponse
from db.session import get_db
from db.models import Conversation
from core.langgraph_orchestration import run_langgraph_chat
import time

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    start = time.time()
    result = run_langgraph_chat(req.user_id, req.message, db)

    db.add(Conversation(
        user_id=req.user_id,
        user_message=req.message,
        bot_response=result["response"],
        tags=result.get("tags", {})
    ))
    db.commit()

    return ChatResponse(
        response=result["response"],
        response_time=round(time.time() - start, 3),
        context_used=result.get("documents", []),
        model=result["model"],
        rag_triggered=result["rag"]
    )
