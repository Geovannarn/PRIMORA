import re 
from datetime import datetime

def consulta_digitos(valor):
    return re.sub(r"\D", "", valor or "")

def limpar_cnpj(valor):
    cnpj = consulta_digitos(valor)
    
    if len(cnpj) != 14:
        return None, "CNPJ Inválido!"
    if cnpj == cnpj[0]*14:
        return None, "CNPJ Inválido!"

    return cnpj, None

def limpar_telefone(valor):
    telefone = consulta_digitos(valor)

    if telefone.startswith("55") and len(telefone) in (12,13):
        telefone = telefone [2:]

    if len(telefone) not in (10,11):
        return None, "Telefone Inválido!"

    return f"+55{telefone}", None

def limpar_cep(valor):
    cep = consulta_digitos(valor)

    if not cep:
        return None, "CEP Inexistente!"

    if len(cep) !=8:
        return None, "Tamanho do CEP indicado é inválido"

    return f"{cep[:5]}-{cep[5:]}", None

def limpar_data(valor):
    valor = (valor or "").strip()
    
    formatos = [

        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y",

    ]    
    for formatos in formatos: 
        try:
            data = datetime.strptime(valor, formatos)
            return data.date().isoformat(), None 
        except ValueError:
            pass
    return None, "Data Inválida"