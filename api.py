import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()  # อ่าน OPENAI_API_KEY จาก environment


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question must not be empty",
        )

    response = client.responses.create(
        model=os.environ["OPENAI_MODEL"],
        input=question,
    )

    return {"answer": response.output_text}