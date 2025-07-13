# README.md

# Multi-Agent Conversational AI System

This is a modular, production-grade conversational backend using FastAPI, OpenAI GPT, Retrieval-Augmented Generation (RAG), LangGraph-style orchestration, PostgreSQL CRM, and FAISS vector search.

---

## 🚀 Features
- Chat with multi-turn memory using OpenAI GPT
- Retrieval-Augmented Generation with FAISS + document upload
- LangGraph-style multi-agent orchestration
- PostgreSQL CRM to store users and conversation history
- Supports tagging, memory reset, and self-improvement loop

---

## 📁 Project Structure (Simplified)
```
multi_agent_ai/
├── main.py
├── config.py
├── .env.example
├── api/                  # FastAPI routes
├── core/                 # RAG, OpenAI, LangGraph logic
├── db/                   # SQLAlchemy models + session
├── vector_store/         # FAISS vector index
├── models/               # Pydantic schemas
├── static/               # Mermaid schema
├── README.md
├── requirements.txt
└── api_contracts.pdf
```

---

## 🛠️ Setup Instructions

### 1. **Install PostgreSQL**
Create a new database named `multi_agent_ai`:
```bash
createdb multi_agent_ai
```

---

### 2. **Clone the Repository**
```bash
git clone <your-repo-url>
cd multi_agent_ai
```

---

### 3. **Install Python Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

### 4. **Set Environment Variables**
```bash
cp .env.example .env
```
Then edit `.env`:
```
DATABASE_URL=postgresql://<user>:<pass>@localhost:5432/multi_agent_ai
OPENAI_API_KEY=sk-...
```

---

### 5. **Initialize the Database**
```bash
python db/init_db.py
```

---

### 6. **Run the Server**
```bash
uvicorn main:app --reload
```
Visit Swagger UI docs:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing Endpoints

1. **Create User**:
POST `/crm/create_user`

2. **Upload CSV/TXT**:
POST `/upload_docs`

3. **Chat with GPT + RAG**:
POST `/chat`

4. **Fetch Conversation Logs**:
GET `/crm/conversations/{user_id}`

5. **Reset Memory**:
POST `/reset`

---

## 📦 Output Format
Every `/chat` response includes:
```json
{
  "response": "Generated text",
  "context_used": ["retrieved doc 1", "retrieved doc 2"],
  "response_time": 0.584,
  "model": "gpt-3.5-turbo",
  "rag_triggered": true
}
```

---

## 📄 API Contracts
- Input/Output schemas
- Sample requests
- Response metadata

See: `api_contracts.pdf`

---

## 🎯 Roadmap Ideas
- Add LangChain or LangGraph agent visualizer
- Integrate Redis for live session memory
- Web frontend to display conversations and analytics

---

## 🧠 Behavior Prompt (LLM System Message)
```
You are a modular multi-agent assistant that supports dynamic document retrieval and CRM-integrated personalization.
You:
- Respond using OpenAI GPT
- Retrieve supporting context using document embeddings when needed
- Maintain and recall chat history per user
- Capture user information in a CRM
- Use LangGraph to decide which sub-agent should handle each task
- Return JSON with rich metadata for every chat
```
