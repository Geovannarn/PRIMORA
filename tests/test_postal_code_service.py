
from unittest.mock import Mock

import pytest

from service import postal_code_service


def test_consulta_cep_encontrado(monkeypatch, tmp_path):
    resultado_esperado = {
        "cep": "70040900",
        "logradouro": "Praça dos Três Poderes",
        "cidade": "Brasília",
        "estado": "DF",
    }

    cache_file = tmp_path / "cep_cache.json"
    monkeypatch.setattr(postal_code_service, "CACHE_FILE", cache_file)
    monkeypatch.setattr(
        postal_code_service,
        "consultar_viacep",
        Mock(return_value=resultado_esperado),
    )

    resultado = postal_code_service.consulta_cep("70040900")

    assert resultado == resultado_esperado


def test_consulta_cep_retorna_none_para_cep_invalido(monkeypatch, tmp_path):
    cache_file = tmp_path / "cep_cache.json"
    monkeypatch.setattr(postal_code_service, "CACHE_FILE", cache_file)
    monkeypatch.setattr(
        postal_code_service,
        "consultar_viacep",
        Mock(return_value= None),
    )
    monkeypatch.setattr(
        postal_code_service,
        "consultar_brasilapi",
        Mock(return_value=None),
    )
    monkeypatch.setattr(postal_code_service.time, "sleep", Mock())

    resultado = postal_code_service.consulta_cep("123")

    assert resultado is None


@pytest.mark.parametrize("entrada", ["", None])
def test_consulta_cep_rejeita_entrada_vazia(entrada):
    resultado = postal_code_service.consulta_cep(entrada)
    assert resultado is None
