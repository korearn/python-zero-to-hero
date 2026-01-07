from flask import Flask, jsonify

app = Flask(__name__)

# definimos ruta raíz
@app.route('/')
def home():
    return "Hola, servidor backend funcionando."

# definimos ruta que devuelve JSON (una API real)
@app.route('/api/status')
def status():
    return jsonify({
        "status": "online",
        "service": "Python Zero to Hero",
        "version": 1.0
    })

if __name__ == '__main__':
    # debug=True permite que el servidor reinicie al cambiar código
    app.run(debug=True, port=5000)