print("\t.:Calculador de Propinas:.")

total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = int(input("Ingrese el porcentaje de propina que desea dejar (10, 15, 20, ...): "))

total_pago = total_cuenta + (total_cuenta * porcentaje_propina / 100)

print(f"El total a pagar, incluyendo una propina del {porcentaje_propina}%, es: ${total_pago:.2f}")

print("¡Gracias por usar el Calculador de Propinas! :)")