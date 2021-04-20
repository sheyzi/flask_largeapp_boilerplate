from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app import bcrypt, db
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash("You are already logged in", "info")
        return redirect(url_for("core.home"))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        user = User.query.filter_by(user_name=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')

            flash("You have successfully logged in!!", "success")
            return redirect(next_page) if next_page else redirect(url_for('core.home'))

        else:
            flash("Incorrect password or username!!", "danger")
    return render_template('auth/login.html', form=form, title="Login")


@auth.route('/sign-up/', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if current_user.is_authenticated:
        flash("You are already logged in", "info")
        return redirect(url_for("core.home"))

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        phone = form.phone.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(user_name=username, first_name=firstname, last_name=lastname,
                    phone_number=phone, email=email, password=hash_password)

        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created successfully!!", 'success')
        return redirect(url_for('auth.login'))
    return render_template("auth/signup.html", form=form, title="Sign Up")


@auth.route('/logout/')
def logout():
    logout_user()
    flash("Logged out successfully!!", "success")
    return redirect(url_for('auth.login'))
