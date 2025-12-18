def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

terreno = calcular_area_rectangulo(20, 50)
print("\t.:Calculadora de Área de Terreno Rectangular:.")
print(f"Base: {20} m\nAltura: {50} m")
print("------------------------")
print(f"El área del terreno es de: {terreno} m2")