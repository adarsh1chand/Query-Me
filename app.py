from fastapi import FastAPI
from dotenv import dotenv_values
import os
import environ

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

# Initialize environment variables and FastAPI application
env = environ.Env()
environ.Env.read_env()

API_KEY = env('OPENAI_API_KEY')

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{env('DBPASS')}@localhost:5432/{env('DATABASE')}",
)

# setup llm
llm = OpenAI(temperature=0, openai_api_key=API_KEY)
QUERY = """
Given an input question and the previous chat_history, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
If the user asks when only then convert them to date IST and EST while displaying the answer (Not display anything about date until asked). Answer each query precisely by creating accurate postgresql
The database belongs to the user asking the question, answer each question as an assitant of the user. Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

chat_history = {chat_history}
question = {question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)



app = FastAPI()

@app.on_event("startup")
async def startup() -> None:
    """Set up environment variables at startup."""
    print("OpenAPI key has been set, the server has been started!")

@app.on_event("shutdown")
async def shutdown() -> None:
    """Perform clean-up during application shutdown."""
    print("Shutting down the server")
