import os
from nutritiontracker import db
from datetime import datetime

class User(db.Model):
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
    quantity    = db.Column(db.Integer, nullable = True, default = 1)
    meal        = db.Column(db.String(9), nullable = False)
    date        = db.Column(db.DateTime, nullable = True, default = datetime.date)
    consumer_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable = False)