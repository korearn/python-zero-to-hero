def safe_division():
    # Bucle infinito para solicitar input al usuario hasta que se complete correctamente
    while True:
        try:
            # Intenta leer el numerador como un float (número con decimales)
            a = float(input("Enter the numerator: "))
            b = float(input("Enter the denominator: "))
        except ValueError:
            # Si no se puede convertir la entrada en un número, imprime mensaje de error
            print("Error: Please enter valid numbers.")
        else:
            # Si la conversión es exitosa, intenta realizar la división
            try:
                result = a / b
            except ZeroDivisionError:
                # Si se intenta dividir por cero, imprime mensaje de error
                print("Error: Division by zero is not allowed.")
            else:
                # Si la división es exitosa, imprime el resultado y sale del bucle
                print(f"The result of {a} divided by {b} is {result}")
                break

# Llama a la función para iniciar el programa
safe_division()