from flask import Flask, jsonify, request
from models import db, Task

app = Flask(__name__)

# Configuración de la Base de Datos (SQLite crea un archivo local)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conectamos la DB con la App
db.init_app(app)

# Crear las tablas antes de la primera petición
with app.app_context():
    db.create_all()

# --- RUTAS ---

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # SELECT * FROM task;
    tasks_list = Task.query.all()
    # Convertimos objetos a diccionarios
    return jsonify([task.to_dict() for task in tasks_list])

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    tarea = Task.query.get(id)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tarea.to_dict())

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    # Creamos un OBJETO (Instancia de clase)
    new_task = Task(title=data['titulo']) 
    
    # Guardamos en DB
    db.session.add(new_task)
    db.session.commit() # Confirmar cambios (INSERT)

    return jsonify(new_task.to_dict()), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    tarea = Task.query.get_or_404(id)
    tarea.done = True
    db.session.commit()
    return jsonify(tarea.to_dict())

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    tarea = Task.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada"}), 204

# --- Ejecución ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
