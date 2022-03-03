from app import app, db, lm
from functools import wraps
from is_safe_url import is_safe_url
from flask import redirect, render_template, request, session, flash, url_for, abort
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.tables import User, Info
from app.models.forms import LoginForm, RegisterForm



@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")
    

@app.route("/calculator", methods=["GET", "POST"])
@login_required
def calculator():
    return render_template("calculator.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        else:
            return flash("Invalid login.")
    return render_template("login.html", form=form)


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    logout_user()
    form = RegisterForm()
    if form.validate_on_submit():
        form.validate_user(form.username, form.email)
        hashed_password = generate_password_hash(form.password.data, "pbkdf2:sha256", 8)
        new_user = User(username=form.username.data, name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    else:
        return render_template("register.html", form=form)
