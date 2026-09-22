from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import agent


app = FastAPI(
    title="Iyuno AI Agent",
    description="Agentic Knowledge Triage",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Iyuno AI Agent is running",
        "project": "Agentic Knowledge Triage"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = agent(request.question)

    if result["type"] == "tool":
        return {
            "type": "tool",
            "answer": result["answer"],
            "source": result["source"]
        }

    return {
        "type": "rag",
        "answer": result["documents"][0],
        "sources": result["sources"]
    }