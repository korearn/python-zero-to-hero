# Principiante
#numeros = [1, 2, 3, 4, 5]
#cuadrados = []
#for n in numeros:
#    cuadrados.append(n * n)
#print(cuadrados)

# pro
numeros = [1, 2, 3, 4, 5]
cuadrados = [n * n for n in numeros]
print(cuadrados)

pares = [n for n in numeros if n % 2 == 0]