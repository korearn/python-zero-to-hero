# Definimos variables para inicializar solamente (se usarán en otro archivo)
def sum(a, b):
    return a + b

def rest(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b