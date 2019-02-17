from flask import url_for, flash
from flask import request, Response, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from nutritiontracker.forms import RegistrationForm, LoginForm
from nutritiontracker import app, db, bcrypt
from nutritiontracker.models import User, foodEntry

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in','success')
        # redirect to home page here
    # redirect back to registration page      

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            # redirect to home page here
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
        # redirect to login page page here

@app.route('/logout')
def logout():
    logout_user()
    # redirect to loading screen

@app.route('/home/<int:id>', methods = ['POST', 'GET'])
def homeSearch(id):
    error = None
    if request.method == 'POST':
        food_name     = request.data.get('food_name')
        quantity      = request.data.get('quantity')
        meal          = request.data.get('meal')
        date_consumed = request.data.get('date_consumed')
elif request.method == 'GET':
    