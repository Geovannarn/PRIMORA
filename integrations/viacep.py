import requests

URL_VIACEP = "https://viacep.com.br/ws/{cep}/json"
TIMEOUT = 3

def consultar_viacep(cep):
    URL_VIACEP.format(cep)

    try:
        Resposta = requests .get(url, timeout=TIMEOUT)

        if Resposta.status_code == 200:
            return Resposta.json()

    except requests.RequestException:
            return None