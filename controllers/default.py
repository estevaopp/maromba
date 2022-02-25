from app.app import app
from flask import render_template, request, session, flash

@app.route("/")
def index():
    return "nothing"
    

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

