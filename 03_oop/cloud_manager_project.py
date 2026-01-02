class CloudResource: # Clase padre
    def __init__(self, name):
        self.name = name
        self.status = 'Stopped'
        
    def power_on(self):
        self.status = 'Running'
        print(f"{self.name} está ahora {self.status}.")

    def power_off(self):
        self.status = 'Stopped'
        print(f"{self.name} está ahora {self.status}.")

class EC2Instance(CloudResource): # Clase hija: Instancia de EC2
    def __init__(self, name, image_id):
        super().__init__(name) # Llama al constructor de la clase padre
        self.image_id = image_id

    def power_on(self):
        print(f"EC2 Instance Name: {self.name}, Image ID: {self.image_id}, Status: {self.status}")

class S3Bucket(CloudResource): # Clase hija: Bucket de S3 (Storage)
    def power_on(self):
        print(f"Bucket Name: '{self.name}' es almacenamiento en la nube. Siempre está disponible.")

    def power_off(self):
        print(f"No puedes apagar un bucket de S3.")

# --- Ejecución ---
print("=== Gestión de Recursos en la Nube ===")
# Creamos los recursos
server_web = EC2Instance("web-prod-01", "ami-0abcdef1234567890")
storage_imgs = S3Bucket("user-images-bucket")

# Lista de atributos del objeto
inventory = [server_web, storage_imgs]

# Operación masiva
for item in inventory:
    item.power_on()  # Llama al método power_on para cada atributo (esto generará un error ya que los atributos no son objetos con métodos)