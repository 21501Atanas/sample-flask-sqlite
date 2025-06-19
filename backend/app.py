from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Път към SQLite файл от /data
db_path = os.path.join(os.getcwd(), '../data/database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/api/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        data = request.get_json()
        item = Item(name=data['name'])
        db.session.add(item)
        db.session.commit()
        return jsonify({'id': item.id, 'name': item.name}), 201
    items = Item.query.all()
    return jsonify([{'id': i.id, 'name': i.name} for i in items])

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
