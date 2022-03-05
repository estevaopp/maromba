from app import app, db, lm
from functools import wraps
from is_safe_url import is_safe_url
from flask import redirect, render_template, request, session, flash, url_for, abort
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.tables import User, Info
from app.models.forms import LoginForm, RegisterForm, InfoForm
from app.controllers.helpers import calcTMB, calcFat, calcProtein, calcGET


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_info = Info.query.filter_by(user_id=current_user.id).first()
    """if request.methods == "POST":
        pass"""
    return render_template("index.html", info=user_info)
    

@app.route("/calculator", methods=["GET", "POST"])
@login_required
def calculator():
    form = InfoForm()
    if form.validate_on_submit():
        user_info = Info.query.filter_by(user_id=current_user.id).first()
        if user_info:
            db.session.delete(user_info)
            db.session.commit()
        tmb = calcTMB(form.height.data, form.weight.data, form.age.data, form.gender.data)
        get_workout = calcGET(tmb, True)
        get_off = calcGET(tmb, False)
        protein = calcProtein(form.weight.data)
        fat = calcFat(form.weight.data)
        info = Info(height=form.height.data, weight=form.weight.data, age=form.age.data, gender=form.gender.data, 
            tmb=tmb, get_workout=get_workout, get_off=get_off, protein=protein, fat=fat, user_id=current_user.id)
        db.session.add(info)
        db.session.commit()
        return redirect("/")

    return render_template("calculator.html", form=form)


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
