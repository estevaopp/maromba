from app import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class Info(db.Model):
    __tablename__ = "infos"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    tmb = db.Column(db.Integer, nullable=False)
    get = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    