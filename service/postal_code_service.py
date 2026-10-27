import json 
import time
from pathlib import Path
from integrations.viacep import consultar_viacep
from integrations.brasilapi import consultar_brasilapi

CACHE_FILE = Path("data/cep_cache.json")
TENTATIVAS = 3

def carregar_cache():
    if not CACHE_FILE.exists():
        return{}
    with open(CACHE_FILE, "r", encoding="utf-8") as arquivo: 
        return json.load(arquivo)

def salvar_cache():
    CACHE_FILE.parent.mkdir(parents=True, exist_ok+True)
    with open(CACHE_FILE, "w", encoding="utf-8") as arquivo: 
        json.dump(cache, arquivo, ensure_ascii=False, indent=2)

def consulta_cep():
    cep = str(cep).replace("-", " ").strip()

    cache = carregar_cache()

    if cep in cache:
        return cache[cep]

    for tentaiva in range(TENTATIVAS):
        Resultado = consultar_viacep(cep)

        if Resultado:
            cache[cep] = Resultado
            salvar_cache(cache)
            return Resultado 

        if tentativas < TENTATIVAS -1:
            time.sleep(1)

    Resultado = consultar_brasilapi(cep)

    if resultado:
        cache[cep] = resultado
        salvar_cache(cache)
        return resultado

    cache[cep] = None
    salvar_cache(cache)

    return None

