from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4
from db.models import User, Conversation
from models.schemas import CreateUserRequest, UpdateUserRequest
from db.session import get_db

router = APIRouter()

@router.post("/crm/create_user")
def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    new_user = User(id=str(uuid4()), **user.dict())
    db.add(new_user)
    db.commit()
    return {"user_id": new_user.id, "message": "User created successfully"}

@router.put("/crm/update_user")
def update_user(user: UpdateUserRequest, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.user_id).first()
    if not db_user:
        return {"error": "User not found"}
    for k, v in user.dict().items():
        if k != "user_id" and v is not None:
            setattr(db_user, k, v)
    db.commit()
    return {"message": "User updated"}

@router.get("/crm/conversations/{user_id}")
def get_conversations(user_id: str, db: Session = Depends(get_db)):
    chats = db.query(Conversation).filter(Conversation.user_id == user_id).all()
    return {"history": [{"user": c.user_message, "bot": c.bot_response} for c in chats]}

@router.post("/reset")
def reset(user_id: str, db: Session = Depends(get_db)):
    db.query(Conversation).filter(Conversation.user_id == user_id).delete()
    db.commit()
    return {"message": "Conversation history cleared"}
