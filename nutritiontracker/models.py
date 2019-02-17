import os
from flask_login import UserMixin
from nutritiontracker import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email    = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    foods    = db.relationship('foodEntry',backref='consumer', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class foodEntry(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    food_name   = db.Column(db.String(50), nullable = False)
    food_id     = db.Column(db.Ineger, nullable = False)
    quantity    = db.Column(db.Integer, nullable = True, default = 1)
    meal        = db.Column(db.String(9), nullable = False)
    date        = db.Column(db.DateTime, nullable = True, default = datetime.date)
    consumer_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable = False)