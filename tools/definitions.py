TOOLS = [
    {
        "name": "buscar_processo",
        "description": "Busca por um processo no banco de dados.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Número do processo ou ID"
                }
            },
            "required": ["query"]
        }
    }
]