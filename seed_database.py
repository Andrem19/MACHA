from __init__ import db, app
from models import User, Product, Order, OrderItem, Address
from werkzeug.security import generate_password_hash

def seed_database():
    User.query.delete()
    Product.query.delete()
    Order.query.delete()
    OrderItem.query.delete()
    Address.query.delete()

    # Create users
    user1 = User(username='user1', password_hash=generate_password_hash('password1'), role='admin')
    user2 = User(username='user2', password_hash=generate_password_hash('password2'), role='moderator')
    user3 = User(username='user3', password_hash=generate_password_hash('password3'), role='user')

    # Add users to session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Apply changes to the database
    db.session.commit()

    # Create addresses for users
    address1 = Address(street='Street 1', city='City 1', country='Country 1', user_id=user1.id)
    address2 = Address(street='Street 2', city='City 2', country='Country 2', user_id=user2.id)
    address3 = Address(street='Street 3', city='City 3', country='Country 3', user_id=user3.id)

    # Add addresses to session
    db.session.add(address1)
    db.session.add(address2)
    db.session.add(address3)

    # Apply changes to the database
    db.session.commit()

    # Create products
    product1 = Product(name='Matcha Tea 1', price=10.99, description='Description of Matcha Tea 1', short_description='Short description of Matcha Tea 1', image_url='url1')
    product2 = Product(name='Matcha Tea 2', price=12.99, description='Description of Matcha Tea 2', short_description='Short description of Matcha Tea 2', image_url='url2')
    product3 = Product(name='Matcha Tea 3', price=11.99, description='Description of Matcha Tea 3', short_description='Short description of Matcha Tea 3', image_url='url3')
    product4 = Product(name='Matcha Tea 4', price=13.99, description='Description of Matcha Tea 4', short_description='Short description of Matcha Tea 4', image_url='url4')
    product5 = Product(name='Matcha Tea 5', price=14.99, description='Description of Matcha Tea 5', short_description='Short description of Matcha Tea 5', image_url='url5')

    # Add products to session
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)

    # Apply changes to the database
    db.session.commit()

    # Create orders
    order1 = Order(user_id=user1.id, stripe_payment_id='stripe1')
    order2 = Order(user_id=user2.id, stripe_payment_id='stripe2')

    # Add orders to session
    db.session.add(order1)
    db.session.add(order2)

    # Apply changes to the database
    db.session.commit()

    # Create order items
    order_item1 = OrderItem(order_id=order1.id, product_id=product1.id, quantity=2)
    order_item2 = OrderItem(order_id=order1.id, product_id=product2.id, quantity=1)
    order_item3 = OrderItem(order_id=order2.id, product_id=product3.id, quantity=3)

    # Add order items to session
    db.session.add(order_item1)
    db.session.add(order_item2)
    db.session.add(order_item3)

    # Apply changes to the database
    db.session.commit()


