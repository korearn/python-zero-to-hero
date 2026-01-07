from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [{"id": 1, "titulo": "Aprender Flask"}, {"id": 2, "titulo": "Crear API con Flask"}]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tareas)

@app.route('/tasks', methods=['POST'])
def create_task():
    nueva_tarea = request.json # accede al JSON
    nueva_tarea['id'] = len(tareas) + 1 # asigna un ID único a la tarea
    tareas.append(nueva_tarea)
    return jsonify({"mensaje": "Tarea creada"}), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    try:
        for tarea in tareas:
            if tarea["id"] == id:
                return jsonify(tarea)
    except Exception as e:
        print(f"Error: {e}")
    return jsonify({"mensaje": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)