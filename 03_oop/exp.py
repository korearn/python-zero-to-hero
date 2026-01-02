# Crea un Jugador con atributos y un método para subir de nivel
class Player:
    def __init__(self, nickname, class_type, xp=0):
        self.nickname = nickname
        self.class_type = class_type
        self.xp = xp

    def level_up(self):
        # Sube 100 de XP cada vez que se llama este método
        self.xp += 100
        print(f"{self.nickname} ha subido de nivel! EXP total: {self.xp}")

# Inicializamos un objeto Player
player_1 = Player("DragonSlayer", "Warrior")
player_1.level_up()  # Llama al método para subir de nivel

print(f"Jugador: {player_1.nickname}, Clase: {player_1.class_type}")
print(f"XP Actual: {player_1.xp}")