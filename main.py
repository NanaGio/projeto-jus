from fastapi import FastAPI
from pydantic import BaseModel
from agent import agente_ON

app = FastAPI(title="Agente")

class AgentRequest(BaseModel):
    message: str

sessions = {}

@app.post("/chat")
async def chat_endpoint(request: AgentRequest):
    try:
        resposta = agente_ON(request.message)
        return resposta
    except Exception as e:
        return {"erro": str(e)}
