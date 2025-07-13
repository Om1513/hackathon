from config import engine, Base
from db.models import User, Conversation, DocumentChunk

Base.metadata.create_all(bind=engine)
