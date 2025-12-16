# loop FOR (imprime Rango de 0 a 4) osea 5 espacios
for i in range(5):
    print(f"Iteración número {i}")

#loop WHILE
contador = 5
while contador > 0:
    print(f"Despegue en {contador}...")
    contador -= 1 # Restamos 1 en cada vuelta al ser int
print("¡Despegue!")