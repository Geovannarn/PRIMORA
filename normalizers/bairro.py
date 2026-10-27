import unicodedata
import re

def limpar_texto(texto):
    if not isinstance(texto, str):
        return ""
    
    nfkd = unicodedata.normalize('NFKD', texto)
    texto_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
   
    return texto_sem_acento.lower().strip()

def normalizar_bairro(texto):
    """
    
    """
    if not texto or not isinstance(texto, str):
        return ("Não informado", "não resolvido")
    
   
    texto_limpo = limpar_texto(texto)
    
    mapa_bairros = {
        # Águas Claras e variações
        "aguas claras": "Águas Claras",
        "aguas claras/df": "Águas Claras",
        "aguas claras - df": "Águas Claras",
        "aguas claras sul": "Águas Claras",
        "aguas claras norte": "Águas Claras",
        "sul (aguas claras)": "Águas Claras",
        "norte (aguas claras)": "Águas Claras",
        
        # Taguatinga e variações
        "taguatinga": "Taguatinga",
        "taguatinga/df": "Taguatinga",
        "taguatinga - df": "Taguatinga",
        "taguatinga sul": "Taguatinga Sul",
        
        # Vicente Pires e variações
        "vicente pires": "Vicente Pires",
        "vicente pires - df": "Vicente Pires",
        "v. pires": "Vicente Pires",
        "vte pires": "Vicente Pires",
        
        # Guará e variações
        "guara i": "Guará I",
        "guara ii": "Guará II",
        "guara - df": "Guará"
    }
    
    if texto_limpo in mapa_bairros:
        return (mapa_bairros[texto_limpo], "dicionário")
    
    
    if "aguas claras" in texto_limpo:
        return ("Águas Claras", "normalização")
    elif "taguatinga" in texto_limpo:
        return ("Taguatinga", "normalização")
    elif "vicente pires" in texto_limpo or "pires" in texto_limpo:
        return ("Vicente Pires", "normalização")
    elif "guara" in texto_limpo:
        return ("Guará", "normalização")
        
    return (texto, "não resolvido")