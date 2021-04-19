from flask import Blueprint, render_template, flash, redirect, url_for
from app.auth.forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        flash("Login Successful!!", "success")
        return redirect(url_for('core.home'))
    return render_template('auth/login.html', form = form)

@auth.route('/sign-up/', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        phone = form.phone.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f"Your account has been created successfully!!", 'success')
        return redirect(url_for('auth.login'))
    return render_template("auth/signup.html", form=form)

@auth.route('/logout/')
def logout():
    pass

