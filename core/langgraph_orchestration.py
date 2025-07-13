from core.rag import get_relevant_context
from core.openai_client import ask_openai

def run_langgraph_chat(user_id, message, db):
    context = get_relevant_context(user_id, message)
    prompt = f"Context:\n{''.join(context)}\n\nUser: {message}" if context else message
    response = ask_openai(prompt)
    return {
        "response": response,
        "documents": context,
        "model": "gpt-3.5-turbo",
        "rag": bool(context)
    }
