edad = int(input("ingrese su edad: "))

if edad < 18:
    print("No puedes pasar")
elif edad >= 18 and edad < 65:
    print("Bienvenido, diviértete")
else:
    print("Entrada VIP gratuita")