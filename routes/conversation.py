from fastapi import APIRouter, status
from controllers.conversation import get_conversation_name_controller

router = APIRouter()

@router.post('/get_name', response_model=str, status_code=status.HTTP_200_OK)
async def get_conversation_name(query: str) -> str:
    """
    Generate and return a conversation name based on the query.
    
    Parameters:
    - query (str): The user query for which to generate a conversation name.
    """
    return get_conversation_name_controller(query)
