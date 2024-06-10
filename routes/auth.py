from flask import request, jsonify, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask import flash
import re
from __init__ import app, db

login = LoginManager(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address.')
            return render_template('register.html')

        # Check if password is at least 6 characters and contains both letters and numbers
        if not (re.search('[a-zA-Z]', password) and re.search('[0-9]', password) and len(password) >= 6):
            flash('Password must be at least 6 characters and contain both letters and numbers.')
            return render_template('register.html')

        user = User(username=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401
        login_user(user)
        return redirect(url_for('home'))  # redirect to home page after successful login
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})