nivel_bateria = int(input("Ingrese el nivel de batería (0-100): ")) # int para inidicar que el
                                                                    # valor es un número entero
print("Nivel de batería:", nivel_bateria)

if nivel_bateria > 50:
    print("Batería saludable")
elif nivel_bateria > 20:
    print("Batería moderada")
else:
    print("Batería baja, por favor recargar")