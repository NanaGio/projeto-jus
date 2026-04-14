import json
import re
from tools.handlers import executar_tool

def agente_ON(mensagem: str, historico: list = None) -> dict:
    if historico is None:
        historico = []

    if "processo" in mensagem.lower():
        # Extrai o primeiro número encontrado na mensagem do usuário
        match = re.search(r'\d+', mensagem)
        query_id = match.group() if match else ""
        
        if query_id:
            resultado = executar_tool("buscar_processo", {"query": query_id})
            resposta = f"Processo: {json.dumps(resultado, ensure_ascii=False)}"
    else: 
        resposta = "Por favor, informe o ID ou número do processo."
    
    historico = historico + [
        {"role": "user", "content": mensagem},
        {"role": "assistant", "content": resposta}
    ]

    return {"Resposta": resposta, "historico": historico}