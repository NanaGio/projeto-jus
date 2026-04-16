import json
import re
from tools import calcular_prazo
#MUDAR ESSA FILE NA VERSÃO AGENTE
def agente_ON(mensagem_user: str, historico: list = None) -> dict:
    if historico is None:
        historico = []

    resposta = ""

    try:
        match mensagem_user.lower():
            case msg if "prazo" in msg:
                datas = re.findall(r'\d{2}/\d{2}/\d{4}', mensagem_user)
                if len(datas) >= 2:
                    resultado = calcular_prazo("calculo_prazo_intimacao", {"data_inicio": datas[0], "data_limite": datas[1]})
                    resposta = resultado.get("prazo_calculado", resultado.get("erro"))
                else:
                    resposta = "Por favor, forneça a data de início e a data limite no formato DD/MM/YYYY."

                #colocar elaborar defesa depois aqui

            case _:
                resposta = "Ferramenta não encontrada."

    except Exception as E:
        print(f"ERRO no agente: {E}") 
    
    
    historico = historico + [
        {"role": "user", "content": mensagem_user},
        {"role": "agente", "content": resposta}
    ]

    return {"Resposta": resposta, "historico": historico}