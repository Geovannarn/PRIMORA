
import re
from datetime import datetime


def consultar_digitos(valor):
    return re.sub(r"\D", "", str(valor or ""))


def limpar_cnpj(valor):
    cnpj = consultar_digitos(valor)

    if len(cnpj) != 14:
        return None, "CNPJ inválido!"

    if cnpj == cnpj[0] * 14:
        return None, "CNPJ inválido!"

    return cnpj, None


def limpar_telefone(valor):
    telefone = consultar_digitos(valor)

    if telefone.startswith("55") and len(telefone) in (12, 13):
        telefone = telefone[2:]

    if len(telefone) not in (10, 11):
        return None, "Telefone inválido!"

    return f"+55{telefone}", None


def limpar_cep(valor):
    cep = consultar_digitos(valor)

    if not cep:
        return None, "CEP ausente!"

    if len(cep) != 8:
        return None, "Tamanho do CEP inválido!"

    return f"{cep[:5]}-{cep[5:]}", None


def limpar_data(valor):
    valor = str(valor or "").strip()

    formatos = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y",
    ]

    for formato in formatos:
        try:
            data = datetime.strptime(valor, formato)
            return data.date().isoformat(), None
        except ValueError:
            pass

    return None, "Data inválida!"
