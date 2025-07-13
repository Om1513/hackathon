from fastapi import FastAPI
from api import chat, crm, documents

app = FastAPI()
app.include_router(chat.router)
app.include_router(documents.router)
app.include_router(crm.router)
