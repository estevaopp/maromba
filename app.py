import sqlite3
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 


app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config["SECRET_KEY"] = "thisisasecretkey"

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from app.controllers import default
