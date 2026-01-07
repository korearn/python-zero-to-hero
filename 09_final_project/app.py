from flask import Flask, jsonify, request
from models import db, Expense
from sqlalchemy import func  # 🔴 CORRECCIÓN 1: Importamos func para la suma
from datetime import datetime # 🔴 CORRECCIÓN 2: Necesario para procesar fechas

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gastos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Buena práctica agregarlo
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])

@app.route('/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    expense = Expense.query.get_or_404(id)
    return jsonify(expense.to_dict())

@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    
    # 🔴 CORRECCIÓN 3: Convertir el string '2024-01-01' a objeto Fecha real
    # Asumimos que el cliente envía formato YYYY-MM-DD
    fecha_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()

    expense = Expense(
        description=data['description'], 
        amount=data['amount'], 
        category=data['category'], 
        date=fecha_obj 
    )
    db.session.add(expense)
    db.session.commit()
    return jsonify(expense.to_dict()), 201

@app.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)
    data = request.json
    if 'description' in data:
        expense.description = data['description']
    if 'amount' in data:
        expense.amount = data['amount']
    if 'category' in data:
        expense.category = data['category']
    if 'date' in data:
        # 🔴 CORRECCIÓN 4: También debemos convertir la fecha al actualizar
        expense.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        
    db.session.commit()
    return jsonify(expense.to_dict())

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted'})

@app.route('/expenses/total', methods=['GET'])
def get_total():
    # 🔴 CORRECCIÓN 5: Usamos scalar() que es más limpio y manejamos si es None
    total = db.session.query(func.sum(Expense.amount)).scalar()
    
    # Si no hay gastos, total será None, así que devolvemos 0
    return jsonify({'total': total if total else 0})

if __name__ == '__main__':
    app.run(debug=True, port=5000)