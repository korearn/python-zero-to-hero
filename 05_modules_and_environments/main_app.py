# importamos nuestro propio módulo (debe estar en la misma carpeta)
import my_utils as utiles

precio = 100
total = utiles.calcular_impuesto(precio)
print(f"Impuesto: {total}")

mensaje = utiles.formatear_texto("  hola mundo ")
print(mensaje)