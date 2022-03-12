from app import app, db, lm
from functools import wraps
from flask import redirect, render_template, request, flash, url_for, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.tables import User, Info
from app.models.forms import LoginForm, RegisterForm, InfoForm
from app.controllers.helpers import calcTMB, calcFat, calcProtein, calcGET


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_info = Info.query.filter_by(user_id=current_user.id).first()
    if request.method == "POST":
        try:
            weight = request.form["weight"]
            weight = float(weight)
        except:
            weight = ""
        if weight:
            user_info.weight = weight
            db.session.commit()

        try:
            height = request.form["height"]
            height = float(height)
        except:
            height = ""
        if height:
            user_info.height = height
            db.session.commit()

        try:
            age = request.form["age"]
            age = float(age)
        except:
            age = ""
        if age:
            user_info.age = age
            db.session.commit()

        try:
            tmb = request.form["tmb"]
            tmb = float(tmb)
        except:
            tmb = ""
        if tmb:
            user_info.tmb = tmb
            db.session.commit()

        try:
            get_off = request.form["get_off"]
            get_off = float(get_off)
        except:
            get_off = ""
        if get_off:
            user_info.get_off = get_off
            db.session.commit()

        try:
            get_workout = request.form["get_workout"]
            get_workout = float(get_workout)
        except:
            get_workout = ""
        if get_workout:
            user_info.get_workout = get_workout
            db.session.commit()

        try:
            protein = request.form["protein"]
            protein = float(protein)
        except:
            protein = ""
        if protein:
            user_info.protein = protein
            db.session.commit()

        try:
            fat = request.form["fat"]
            fat = float(fat)
        except:
            fat = ""
        if fat:
            user_info.fat = fat
            db.session.commit()

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
