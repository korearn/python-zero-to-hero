from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'Expense {self.description} - {self.amount} - {self.category}'

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'date': str(self.date)
        }
