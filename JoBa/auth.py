from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["Get", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
        else:
            flash("Email is not Exist!", category="error")
    return render_template("login.html", title="JoBa-Login", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["Get", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password = request.form.get("password")
        confirm = request.form.get("confirm") 
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!", category="error")
        elif len(email) < 6:
            flash("Email must be greater than 5 characters.", category="error")
        elif len(first_name) < 3:
            flash("Name must be greater than 2 characters.", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 6 characters.", category="error")
        elif password != confirm:
            flash("Passwords don't match.", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))
    return render_template("sign_up.html", title="JoBa-Sign_Up", user=current_user)


