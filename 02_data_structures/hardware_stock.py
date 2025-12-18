stock = {"RAM": 11, "SSD": 4, "GPU": 2, "CPU": 5, "Motherboard": 7}

print("\t.:Componentes de PC:.")

for i, (item, qty) in enumerate(stock.items(), start=1): # Ciclo para enumerar la lista de stock
    print(f"{i}. {item}: {qty} unidades")

print("------------------------")

item = input("Ingrese el nombre del componente de hardware: ")

if item in stock:
    stock[item] > 0 # Verifica si hay stock disponible (mayor a 0)
    stock[item] -= 1 # Resta 1 unidad del stock
    print(f"Producto encontrado. Quedan {stock[item]} en stock.") # Muestra el stock restante
else:
    print("Producto no encontrado en stock.") # Si la entrada no está en el diccionario