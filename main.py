from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from agent import agente_ON
from dotenv import load_dotenv
import os
#adicionar langchain depois, para gerenciamento do modelo
from fastapi.middleware.cors import CORSMiddleware#ETAPA DE SEGURANÇA
from slowapi import Limiter, _rate_limit_exceeded_handler#ETAPA DE SEGURANÇA - proteção contra DDoS
from slowapi.util import get_remote_address#ETAPA DE SEGURANÇA - lidando com a conexão youjus - Agente
from slowapi.errors import RateLimitExceeded#ETAPA DE SEGURANÇA - proteção contra DDoS

load_dotenv()
app = FastAPI(title="Agente")

#Limiter = 

localhost = os.getenv("localhost")

origins = [
    f"{localhost}"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST"],#Apenas get, para fazer a leitura no banco de dados YouJus
    allow_headers=["*"]
)
#SEGURANÇA

class AgentRequest(BaseModel):
    message: str

sessions = {}

@app.websocket("/ws/chat")#post com websocket - esse é melhor para a nossa IA, deixa a conversa mais fluida e tal
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    historico = []
    try:
        while True:
            try:
                data = await websocket.receive_json()
                mensagem_user = data.get("user message", "")
                
                if mensagem_user:
                    resposta_agente = agente_ON(mensagem_user)
                    historico = resposta_agente.get("historico", [])
                    await websocket.send_json(resposta_agente)
                else:
                    await websocket.send_json({"erro": "Mensagem do usuário não fornecida ou vazia."})
            except Exception as E:
                print(f"Erro ao processar mensagem ou JSON: {E}")
                await websocket.send_json({"Erro, formato inválido. Envie um JSON"})
            


    except WebSocketDisconnect:
        print("Desconectado")