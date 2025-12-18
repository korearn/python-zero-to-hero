# Un servidor definido como diccionario
servidor = {
    "hostname": "web-01",
    "ip": "192.168.1.10",
    "activo": True,
    "puertos": [80, 443, 22] # Puede tener listas dentro
}

# Acceder a los valores usando las llaves
print("Dirección IP del Servidor:", servidor["ip"]) # Imprime "192.168.1.10"
print("------------------------------")

# Agregar/Modificar
servidor["os"] = "Ubuntu" # Crea una nueva clave
servidor["activo"] = False

#Iterar
for clave, valor in servidor.items():
    print(f"{clave}: {valor}")