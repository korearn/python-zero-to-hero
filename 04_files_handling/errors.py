# sin manejo de errores (peligro)
edad = int(input("Edad: ")) # si escribo "veinte" explota

# con manejo de errores (seguro)
try:
    edad = int(input("Edad: "))
    print(f"Tienes {edad} años.")
except ValueError:
    print("Error: Por favor, ingresa un número válido para la edad.")
except ValueError as e:
    print(f"Error de valor: {e}")
finally:
    print("Este bloque se ejecuta siempre, haya o no error.")