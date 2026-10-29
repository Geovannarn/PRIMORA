
import pytest

from validators.postal_code import (
    normalizar_cep,
    verifica_cep,
    formatar_cep,
)


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("70040-900", "70040900"),
        ("70040900", "70040900"),
        (" 70040-900 ", "70040900"),
        ("01001-000", "01001000"),
        ("00000-000", "00000000"),
        ("123", None),
        ("123456789", None),
        ("abcde-fgh", None),
        ("", None),
        (None, None),
    ],
)
def test_normalizar_cep(entrada, esperado):
    assert normalizar_cep(entrada) == esperado


@pytest.mark.parametrize(
    "cep, esperado",
    [
        ("70040900", True),
        ("01001000", True),
        ("00000000", True),
        ("123", False),
        ("123456789", False),
        ("abcdefgh", False),
        ("", False),
        (None, False),
    ],
)
def test_verifica_cep(cep, esperado):
    assert verifica_cep(cep) is esperado


@pytest.mark.parametrize(
    "cep, esperado",
    [
        ("70040900", "70040-900"),
        ("01001000", "01001-000"),
        ("00000000", "00000-000"),
    ],
)
def test_formatar_cep(cep, esperado):
    assert formatar_cep(cep) == esperado
