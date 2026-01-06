# funciones pequeñas y anonimas
# se usan al ordenar datos o configurar frameworks
def sumar(a, b):
    return a + b

# lambda equivalente
# variable = lambda argumentos: retorno
sumar_lambda = lambda a, b: a + b

print(sumar_lambda(5, 3))