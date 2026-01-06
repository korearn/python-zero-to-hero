# escribir (crear archivo)
notas = ["Python es genial", "Aprender POO fue útil", "No olvidar el git push"]

with open("mis_notas.txt", "w") as archivo: # w es write
    for nota in notas:
        archivo.write(nota + "\n")

# Leer (Mostrar contenido)
try:
    with open("mis_notas.txt", "r") as archivo: # r es read
        contenido = archivo.read()
        print("--- Contenido del archivo ---")
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")