from fastapi import FastAPI
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/questions/")
async def get_questions():
    query = "SELECT id, description, options, correct_answer FROM questions;"
    return await database.fetch_all(query=query)
