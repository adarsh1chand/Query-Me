import openai
from typing import Any
from app import env

openai.api_key = env('OPENAI_API_KEY')

def get_conversation_name_controller(query: str) -> str:
    """
    Get a conversation name using OpenAI API.
    
    Parameters:
    - query (str): The user query for which to generate a conversation name.
    
    Returns:
    - str: The generated conversation name.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"You are an assistant whose job is to suggest names for the queries asked by the user. Respond with a very small and meaningful name for the following query given by the user: {query}.",
            max_tokens=20
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Unnamed Conversation"