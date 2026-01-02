class Server:
    # Método Constructor para inicializar los atributos del objeto
    def __init__(self, hostname, ip, os="Linux"):
        self.hostname = hostname # Atributos
        self.ip = ip
        self.os = os
        self.online = False # Atributo por defecto

    # Método para iniciar el servidor
    def start(self):
        self.online = True
        print(f"El servidor {self.hostname} ({self.ip}) está ahora ONLINE.")

    def ping(self):
        if self.online:
            return f"Ping de {self.hostname}"
        else:
            return "Request timed out (Offline)"
        
# --- Usando la clase (Creando objetos) ---

# Creando los objetos 'web01' y 'db01' usando el molde 'Server'
web01 = Server("web-prod-01", "10.0.0.5")
db01 = Server("db-main", "10.0.0.6", "Windows")

web01.start() # Iniciando el servidor web01
print(web01.ping())
print(db01.ping()) # Intentando hacer ping al servidor db01 (está offline)