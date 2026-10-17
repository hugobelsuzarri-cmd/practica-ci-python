import pytest

from calculadora import sumar, dividir, promedio


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_promedio():
    assert promedio([2, 4, 6]) == 4


def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        promedio([])
