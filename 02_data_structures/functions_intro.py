def saludar(nombre, rol="Usuario"): # "Usuario" es el valor por defecto
    mensaje = f"Hola {nombre}, bienvenido al sistema. Tu rol es: {rol}."
    return mensaje

# Uso de la función
texto_saludo = saludar("Leo", rol="Admin")
texto_saludo_default = saludar("Ana") # Usa el valor por defecto para rol

print("Variables de la Función: ", saludar({nombre}, {rol}))
print(texto_saludo) # Imprime: Hola Leo, bienvenido al sistema. Tu rol es: Admin.
print(texto_saludo_default) # Imprime: Hola Ana, bienvenido al sistema. Tu rol es: Usuario.