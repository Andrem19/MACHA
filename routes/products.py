from __init__ import app, db
from flask import Flask, request, jsonify
from flask_login import current_user
from models import Product

@app.route('/products', methods=['POST'])
def add_product():
    if not current_user.is_authenticated:
        return jsonify({'error': 'Please log in to add products'}), 401
    name = request.json.get('name')
    price = request.json.get('price')
    description = request.json.get('description')
    product = Product(name=name, price=price, description=description)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}) 