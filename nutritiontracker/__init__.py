from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from nutritiontracker import routes