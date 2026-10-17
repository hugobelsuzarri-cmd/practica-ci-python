def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def promedio(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)
