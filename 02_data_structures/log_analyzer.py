logs = [200, 404, 500, 200, 301, 404, 200, 503, 200, 404, 506] # lista en crudo

server_errors = [0] # Variable para contar errores del servidor

for status in logs:
    if status >= 500:
        print(f"Server error detected: {status}")
        server_errors[0] += 1
    else:
        print(f"Status code: {status}")
else:
    print("Errores encontrados:", f"{server_errors[0]}")