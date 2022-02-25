from app.app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class Info(db.Model):
    __tablename__ = "infos"

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    tmb = db.Column(db.Integer, nullable=False)
    get = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    user = db.relationship("User", foreign_keys=user_id)
    
    def __init__(self, user_id, height, weight, age, gender, tmb, get, protein, fat):
        self.user_id = user_id
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.tmb = tmb
        self.get = get
        self.protein = protein
        self.fat = fat

    def __repr__(self):
        return f"<Info {self.user_id}>"