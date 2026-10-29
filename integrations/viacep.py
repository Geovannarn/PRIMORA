import requests

URL_VIACEP = "https://viacep.com.br/ws/{cep}/json/"
TIMEOUT = 3


def consultar_viacep(cep):
    url = URL_VIACEP.format(cep=cep)

    try:
        resposta = requests.get(url, timeout=TIMEOUT)

        if resposta.status_code != 200:
            return None

        dados = resposta.json()
    except (requests.RequestException, ValueError):
        return None

    if dados.get("erro"):
        return None

    return dados