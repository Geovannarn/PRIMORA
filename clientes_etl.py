
import os
import pandas as pd

from validators.limpeza import (
    limpar_cnpj,
    limpar_telefone,
    limpar_cep,
    limpar_data,
)


def aplicar(df, coluna, funcao):
    resultado = df[coluna].map(funcao)

    df[f"{coluna}_original"] = df[coluna]
    df[coluna] = resultado.map(lambda valor: valor[0])
    df[f"{coluna}_erro"] = resultado.map(lambda valor: valor[1])


os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv(
    "data/raw/clientes_distribuidora_vetor.csv",
    sep=";",
    dtype=str,
    keep_default_na=False,
    encoding="utf-8",
)


for coluna, funcao in [
    ("cnpj", limpar_cnpj),
    ("telefone", limpar_telefone),
    ("cep", limpar_cep),
    ("data_cadastro", limpar_data),
]:
    aplicar(df, coluna, funcao)


colunas_erro = [
    coluna for coluna in df.columns
    if coluna.endswith("_erro")
]

tem_erro = (
    df[colunas_erro]
    .fillna("")
    .ne("")
    .any(axis=1)
)


df[~tem_erro].to_csv(
    "data/clean/clientes_distribuidora_vetor_validos.csv",
    sep=";",
    index=False,
    encoding="utf-8",
)

df[tem_erro].to_csv(
    "data/clean/clientes_distribuidora_vetor_invalidos.csv",
    sep=";",
    index=False,
    encoding="utf-8",
)


print(f"Total de registros: {len(df)}")
print(f"Registros válidos: {(~tem_erro).sum()}")
print(f"Registros inválidos: {tem_erro.sum()}")
print("Arquivos salvos na pasta data/clean.")
