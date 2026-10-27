import requests

URL_BRASILAPI = ""
TIMEOUT = 3

def consultar_brasilapi(cep):
    URL_BRASILAPI.format(cep)

    try:
        Resposta = requests .get(url), timeout=TIMEOUT

        if Resposta.status_code == 200:
            return Resposta.json()

    except requests.RequestException:
        return None
    
