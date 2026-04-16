from datetime import datetime, timedelta
import re
from workalendar.america import Brazil

#MUDAR ESSA FILE NA VERSÃO AGENTE

#utilizo pandas? SIM! E escrevo no prompt para ele considerar feriados nacionais
def calcular_prazo(mensagem_user: str, inputs: dict) -> dict:#tirar o dict na versão com agente
    try:
            cal = Brazil()
            data_inicio_str = inputs.get("data_inicio")
            data_limite_str = inputs.get("data_limite")

            if not data_inicio_str or not data_limite_str:
                return {"erro": "Forneça as duas datas"}
            
            data1_obj = datetime.strptime(data_inicio_str, '%d/%m/%Y')
            data2_obj = datetime.strptime(data_limite_str, '%d/%m/%Y')

            d1 = min(data1_obj, data2_obj)
            d2 = max(data1_obj, data2_obj)

            while not cal.is_working_day(d2):
                 d2 += timedelta(days=1)

            dias_uteis = cal.get_working_days_delta(d1.date(), d2.date())
            return {
                "prazo_calculado": f"O prazo vence em {d2.strftime('%d/%m/%Y')} ({dias_uteis} dias úteis)."
        }

    except Exception as E:
        return {"erro": str(E)}
    
"""
def defesa_para_pdf(mensagem_user: str, file_name: str, inputs: dict) -> dict:
    try:
        if mensagem_user == mensagem_user.lower("defesa_para_pdf"):

    
    except Exception as E:
        return {"erro": str(E)}
"""

def elaborar_defesa(mensagem_user: str, inputs: dict, resposta_agente: dict) -> dict:
    try:
        if mensagem_user.lower() == "elabore_defesa":
            return {"defesa_elaborada": f"{resposta_agente}"}
        return {"erro": "Comando para elaborar defesa não reconhecido."}
        
    except Exception as E:
        return {"erro": str(E)}