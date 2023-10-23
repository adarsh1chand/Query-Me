import uvicorn
from fastapi import FastAPI

from routes.chat import router as chat_router
from routes.conversation import router as conversation_router
from app import app, startup, shutdown, env

@app.get("/")
async def root() -> dict:
    """Root route that returns a message."""
    return {"message": env("server_on_message")}

# Include routers
app.include_router(chat_router, tags=["Chat with Personal Data"], prefix="/chatDB")
app.include_router(conversation_router, tags=["Conversation Name"], prefix="/conversation")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8001, log_level="info", reload=True)
