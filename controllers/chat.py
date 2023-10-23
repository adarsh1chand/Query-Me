from fastapi import HTTPException, status, Request
from typing import Any
from app import QUERY, db_chain

def query_database_controller(request: Request, prompt: str, chat_history: str) -> str:
    """
    Query the database using the provided prompt and chat history.
    
    Parameters:
    - request (Request): FastAPI request object.
    - prompt (str): The query prompt.
    - chat_history (str): The chat history.
    
    Returns:
    - str: The response from the database query.
    """
    try:
        question = QUERY.format(question=prompt, chat_history=chat_history)
        response = db_chain.run(question)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
