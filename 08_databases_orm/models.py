from flask_sqlalchemy import SQLAlchemy

# Inicializamos la extensión (pero no la app todavía)
db = SQLAlchemy()

# Definimos la tabla 'Task'
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)      # ID único autoincremental
    title = db.Column(db.String(100), nullable=False) # Título, obligatorio
    done = db.Column(db.Boolean, default=False)       # Estado, por defecto False

    # Método opcional para mostrar info bonita al imprimir
    def __repr__(self):
        return f'<Task {self.title}>'

    # Método helper para convertir a diccionario (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }