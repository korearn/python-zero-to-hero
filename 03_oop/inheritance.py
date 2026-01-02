# Clase Padre
class Instrumento:
    def __init__(self, marca):
        self.marca = marca

    def tocar(self):
        print("El instrumento está sonando.")

# Clase Hija que hereda de Instrumento
class Guitarra(Instrumento):
    def __init__(self, marca, tipo_cuerda):
        super().__init__(marca)  # Llama al constructor de la clase padre
        self.tipo_cuerda = tipo_cuerda

    # Polimorfismo: Sobrescribe el método tocar
    def tocar(self):
        print(f"La guitarra de marca {self.marca} con cuerdas de {self.tipo_cuerda} está sonando.")

mi_guitarra = Guitarra("Gibson", "acero")
mi_guitarra.tocar()  # Llama al método sobrescrito en la clase hija