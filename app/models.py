from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(15), unique=True)
    user_name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100), unique=True)
    active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)