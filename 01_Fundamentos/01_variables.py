nombre = "Leo"      # String
edad = 26           # Integer
altura = 1.66       # Float
es_estudiante = False # Boolean

# Entrada y Salida
print(f"Hola, soy {nombre} y tengo {edad} años.") # f-string to format

# Conversión de tipos
edad_usuario = input("Introduce tu edad: ") # Devuelve un texto
edad_numero = int(edad_usuario) # Convierte a entero
print("Tu edad en un año será: " + str(edad_numero + 1)) # Suma 1 a la edad