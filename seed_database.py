from __init__ import db, app
from models import User, Product
from werkzeug.security import generate_password_hash

def seed_database():
    User.query.delete()
    Product.query.delete()
    # Создаем пользователей
    user1 = User(username='user1', password_hash=generate_password_hash('password1'))
    user2 = User(username='user2', password_hash=generate_password_hash('password2'))
    user3 = User(username='user3', password_hash=generate_password_hash('password3'))

    # Добавляем пользователей в сессию
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Создаем продукты
    product1 = Product(name='Мача чай 1', price=10.99, description='Описание Мача чай 1')
    product2 = Product(name='Мача чай 2', price=12.99, description='Описание Мача чай 2')
    product3 = Product(name='Мача чай 3', price=11.99, description='Описание Мача чай 3')
    product4 = Product(name='Мача чай 4', price=13.99, description='Описание Мача чай 4')
    product5 = Product(name='Мача чай 5', price=14.99, description='Описание Мача чай 5')

    # Добавляем продукты в сессию
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)

    # Применяем изменения в базе данных
    db.session.commit()