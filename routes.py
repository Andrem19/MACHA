from flask import Flask, request, jsonify
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Product
from __init__ import app, db

login = LoginManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401
    login_user(user)
    return jsonify({'message': 'Logged in successfully'})

@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

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