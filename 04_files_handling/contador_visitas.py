def contar_visitantes():
    try:
        with open("visitas.txt", "r") as archivo:
            visitas = int(archivo.read())
    except FileNotFoundError:
        visitas = 0
    except ValueError:
        visitas = 0

    visitas += 1

    with open("visitas.txt", "w") as archivo:
        archivo.write(str(visitas))

    return visitas

contar_visitantes()