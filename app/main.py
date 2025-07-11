from fastapi import FastAPI
from app.rag import generate_answer

app = FastAPI()

from pydantic import BaseModel
class QueryRequest(BaseModel):
    query: str
@app.post("/query")
async def query_api(req: QueryRequest):
    response = generate_answer(req.query)
    return response