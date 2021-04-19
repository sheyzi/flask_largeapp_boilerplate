from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired('Username cannot be empty')])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Login')