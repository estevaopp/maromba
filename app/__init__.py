from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

app.secret_key = b'_3#y2S"F4X0i\n\xec]/'

lm = LoginManager()
lm.init_app(app)

from app.controllers import default
