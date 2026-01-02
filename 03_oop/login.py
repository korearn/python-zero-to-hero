# Sistema de Login
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Contraseña actualizada.")

    def login(self, input_password):
        if self.password == input_password:
            print(f"Bienvenido, {self.name}!")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
        
user_login = User("admin", "1234")
attempt = input(f"Ingrese la contraseña para el usuario {user_login.name}: ")
user_login.login(attempt)