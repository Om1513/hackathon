from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    response_time: float
    context_used: Optional[List[str]] = []
    model: Optional[str]
    rag_triggered: Optional[bool]

class CreateUserRequest(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    preferences: Optional[dict] = {}

class UpdateUserRequest(BaseModel):
    user_id: str
    name: Optional[str]
    email: Optional[str]
    company: Optional[str]
    preferences: Optional[dict]
