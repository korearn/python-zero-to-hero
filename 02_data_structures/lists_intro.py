# Sintaxis: Corchetes
tecnologias = ["Python", "Docker", "Linux", "SQL"]

# Acceder (El índice empieza en 0)
print(tecnologias[0]) # Imprime Python
print(tecnologias[-1]) # Imprime SQL (El último)

#Modificar
tecnologias.append("Kubernetes") # Agrega al final
tecnologias[1] = "Terraform"    # Modifica el segundo espacio por "Terraform"
tecnologias.pop(2)              # Elimina el elemento en el índice 2 ("Linux")

# Iterar (Lo más común es usar un ciclo for)
for tech in tecnologias:
    print(f"Estoy aprendiendo: {tech}")

print(f"{tech}") # La variable obtiene el último valor del ciclo
# Longitud       # f es para formatear como str