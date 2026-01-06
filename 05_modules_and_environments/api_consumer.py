import requests # importamos la librería para hacer requests HTTP
import json

# pedimos los datos a una API pública
url = "https://api.github.com/users/korearn"

print(f"Conectando a {url}...")
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json() # Convierte el JSON recibido a Diccionario
    print(f"Usuario: {datos['login']}")
    print(f"Bio: {datos['bio']}")
    print(f"Repos públicos: {datos['public_repos']}")
else:
    print("Error al conectar.")