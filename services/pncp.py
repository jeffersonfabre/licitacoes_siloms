import requests

def buscar_licitacao(uasg: str, tipo: str, numero: str):
    if tipo == "Pregão":
        url = "https://pncp.gov.br/api/consulta/v1/pregoes"
    else:
        url = "https://pncp.gov.br/api/consulta/v1/dispensas"

    params = {
        "uasg": uasg,
        "numero": numero
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()
