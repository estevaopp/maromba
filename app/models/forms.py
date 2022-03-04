from app import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo, NumberRange


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), 
        Length(min=2, max=20)], render_kw={"placeholder": "Username"})

    name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Name"})

    email = StringField(validators=[InputRequired()], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})

    confirm = PasswordField(validators=[InputRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Password"})

    submit = SubmitField("Register")

    def validate_user(self, username, email):
        existing_user_username = db.User.query.filter_by(username=username.data).first()
        existing_user_email = db.User.query.filter_by(email=email.data).first()
        if existing_user_username and existing_user_email:
            if existing_user_username:
                raise ValidationError("This username already exists. Please choose a different one.")
            if existing_user_email:
                raise ValidationError("This email already exists. Please choose a different one.")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Login")


class InfoForm(FlaskForm):
    height = FloatField(validators=[InputRequired(), NumberRange(min=100, max=250, message="Send your height in cm.")], render_kw={"placeholder": "Height"})

    weight = FloatField(validators=[InputRequired(), NumberRange(min=20, max=200)], render_kw={"placeholder": "Weight"})

    age = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Age"})

    gender = SelectField(u'Genders', choices=[('M', 'Male'), ('F', 'Female')])

    submit = SubmitField("Submit")

