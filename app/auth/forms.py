from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import  User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired('Username cannot be empty'),
                                                   Length(min=4, max=20)])
    firstname = StringField("First Name", validators=[DataRequired('First Name cannot be empty')])
    lastname = StringField("Last Name", validators=[DataRequired('Last Name cannot be empty')])
    phone = StringField("Phone Number", validators=[DataRequired("Phone Number cannot be empty!"), Length(max=11)])
    email = StringField('Email', validators=[DataRequired("Email is required"), Email(message="Invalid email!")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", "Password Must be Equal!")])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(user_name=username.data).first()
        print(user)
        if user:
            raise ValidationError("A user with this username already exists! Please choose another username")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        print(user)
        if user:
            print(User.query.all())
            raise ValidationError("An account with this email already exists!")

    def validate_phone(self, phone):
        user = User.query.filter_by(phone_number=phone.data).first()
        print(user)
        if user:
            raise ValidationError("An account with this phone number already exists!")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired('Username cannot be empty')])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Login')