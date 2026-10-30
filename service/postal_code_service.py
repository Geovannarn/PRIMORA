import json
import re
import time
from pathlib import Path

from integrations.viacep import consultar_viacep
from integrations.brasilapi import consultar_brasilapi

CACHE_FILE = Path("data/cep_cache.json")
TENTATIVAS = 3


def carregar_cache():
    if not CACHE_FILE.exists():
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(cache, arquivo, ensure_ascii=False, indent=2)


def consulta_cep(cep):
    cep = re.sub(r"\D", "", str(cep or ""))

    if len(cep) != 8:
        return None

    cache = carregar_cache()

    if cep in cache and cache[cep]:
        return cache[cep]

    for tentativa in range(TENTATIVAS):
        resultado = consultar_viacep(cep)

        if resultado:
            cache[cep] = resultado
            salvar_cache(cache)
            return resultado

        if tentativa < TENTATIVAS - 1:
            time.sleep(1)

    resultado = consultar_brasilapi(cep)

    if resultado:
        cache[cep] = resultado
        salvar_cache(cache)
        return resultado

    return None