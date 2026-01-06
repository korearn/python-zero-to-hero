archivo_db = "inventario.txt"
inventario = {}

def cargar_inventario():
    try:
        with open(archivo_db, "r") as f:
            for linea in f:
                nombre, cantidad = linea.strip().split(",")
                inventario[nombre] = int(cantidad)
            print("Inventario de datos cargada correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
    except Exception as e:
        print(f"Error al cargar: {e}")

def guardar_inventario():
    try:
        with open(archivo_db, "w") as f:
            for nombre, cantidad in inventario.items():
                f.write(f"{nombre},{cantidad}\n")
    except Exception as e:
        print(f"Error al guardar: {e}")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    try:
        cantidad = int(input("Cantidad: "))
        inventario[nombre] = cantidad
        guardar_inventario() # Guardado automático
        print("Producto guardado.")
    except ValueError:
        print("La cantidad debe ser un número.")

# --- Ejecución ---
cargar_inventario()

while True:
    print("\n1. Ver Inventario | 2. Agregar/Actualizar | 3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        for n, c in inventario.items():
            print(f"- {n}: {c}")
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        break