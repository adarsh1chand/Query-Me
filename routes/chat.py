from fastapi import APIRouter, status, Request, HTTPException
from pydantic import BaseModel
from controllers.chat import query_database_controller

router = APIRouter()

class ChatQuery(BaseModel):
    prompt: str
    chat_history: str

@router.post('/query_database', response_model=str, status_code=status.HTTP_200_OK)
async def query_database(request: Request, chat_query: ChatQuery) -> str:
    """
    Query the database and return the response.

    Parameters:
    - request (Request): FastAPI request object.
    - chat_query (ChatQuery): Query and chat history.
    """
   
    return query_database_controller(request, chat_query.prompt, chat_query.chat_history)
