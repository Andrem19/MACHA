from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64))  # новое поле для роли пользователя
    address = db.relationship('Address', backref='user', uselist=False)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Float)
    description = db.Column(db.String(256))
    short_description = db.Column(db.String(128))  # новое поле для короткого описания
    image_url = db.Column(db.String(256))  # новое поле для URL изображения

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    stripe_payment_id = db.Column(db.String(128))  # новое поле для ID платежа Stripe
    items = db.relationship('OrderItem', backref='order')

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)  # количество единиц данного продукта в заказе

