from mock.data import PROCESSOS

def executar_tool(processo: str, inputs: dict) -> dict:
    try:
        if processo == "buscar_processo":
            query = inputs["query"]
            resultado = []
            for p in PROCESSOS:
                if query == p["numero"] or query == str(p["id"]):
                    resultado.append({
                        "id": p["id"],
                        "numero": p["numero"]
                    })
            return {"Processo": resultado}
        return {"erro": "Ferramenta não encontrada"}
    except Exception as e:
        return {"erro": str(e)}