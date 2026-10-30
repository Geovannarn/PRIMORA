import pytest

from validators.limpeza import (
    limpar_cnpj,
    limpar_telefone,
    limpar_cep,
    limpar_data,
)


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("84.959.310/0001-20", "84959310000120"),
        ("84959310000120", "84959310000120"),
    ],
)
def test_limpar_cnpj(entrada, esperado):
    resultado, erro = limpar_cnpj(entrada)

    assert resultado == esperado
    assert erro is None


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("(61) 99999-9999", "+5561999999999"),
        ("61999999999", "+5561999999999"),
    ],
)
def test_limpar_telefone(entrada, esperado):
    resultado, erro = limpar_telefone(entrada)

    assert resultado == esperado
    assert erro is None


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("71929-000", "71929-000"),
        ("71929000", "71929-000"),
    ],
)
def test_limpar_cep(entrada, esperado):
    resultado, erro = limpar_cep(entrada)

    assert resultado == esperado
    assert erro is None


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("16/04/2025", "2025-04-16"),
    ],
)
def test_limpar_data(entrada, esperado):
    resultado, erro = limpar_data(entrada)

    assert resultado == esperado
    assert erro is None


@pytest.mark.parametrize(
    "funcao",
    [
        limpar_cnpj,
        limpar_telefone,
        limpar_cep,
        limpar_data,
    ],
)
def test_valor_ausente(funcao):
    resultado, erro = funcao(None)

    assert resultado is None
    assert erro is not None