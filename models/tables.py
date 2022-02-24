from app import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)