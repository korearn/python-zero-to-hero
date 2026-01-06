import requests
import json

nombre = input("Ingrese el nombre del Pokémon: ")

url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

print(f"Conectando a {url}...")
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print(f"Pokémon: {datos['name']}")
    print(f"# {datos['id']}")
    tipos = [tipo['type']['name'] for tipo in datos['types']]
    print(f"Tipos: {', '.join(tipos)}")

    # Leer archivo JSON existente (si existe) y agregar nuevos datos
    try:
        with open('pokedex.json', 'r') as file:
            pokedex = json.load(file)
            pokedex.append({
                'nombre': datos['name'],
                'id': datos['id'],
                'tipos': tipos
            })
    except FileNotFoundError: # Si el archivo no existe, crea uno vacío
        pokedex = []

        # Escribir la lista completa
    with open('pokedex.json', 'w') as file:
        json.dump(pokedex, file, indent=4)