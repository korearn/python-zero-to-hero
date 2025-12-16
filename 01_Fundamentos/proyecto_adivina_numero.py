import random

secreto = random.randint(1, 50) # Elige un valor entre 1 y 50
adivina = False # Boolean
intentos = 0

input("¡Bienvenido al juego de adivinanza de números! Presiona Enter para comenzar...")

# Usamos while not porque no sabemos cuántos intentos necesitará el usuario
while not adivina:
    usuario = int(input("Elige un número entre 1 y 50: "))
    intentos += 1

    if usuario == secreto:
        adivina = True
        print(f"¡Felicidades! Has adivinado el número {secreto} en {intentos} intentos.")
    elif usuario < secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")