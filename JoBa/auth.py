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
        name = request.form.get("firstName")
        password = request.form.get("password")
        confirm = request.form.get("confirm") 
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!", category="error")
        elif len(email) < 6:
            flash("Email must be greater than 5 characters.", category="error")
        elif len(name) < 3:
            flash("Name must be greater than 2 characters.", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 6 characters.", category="error")
        elif password != confirm:
            flash("Passwords don't match.", category="error")
        else:
            new_user = User(email=email, first_name=name, password=generate_password_hash(password, method='sha256'), budget=100)
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))
    return render_template("sign_up.html", title="JoBa-Sign_Up", user=current_user)



@auth.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "GET":
        return render_template("profile.html", title="JoBa-Profile", user=current_user)
    
    # Allow to user change password
    else:
        user = User.query.filter_by(email=current_user.email).first()
        hash_pass = user.password
        my_password = request.form.get("my_password")
        new_password = request.form.get("new_password")
        
        if not my_password:
            flash("Enter the old password field", category="error")
            return redirect(url_for("auth.profile"))
            
        if not new_password:
            flash("Enter the new password field", category="error")  
            return redirect(url_for("auth.profile"))  
        
        if not check_password_hash(hash_pass, my_password):
            flash("Enter the correct old password!", category="error")  
            return redirect(url_for("auth.profile"))  
        
        else:
            hash = generate_password_hash(new_password)
            user.password = hash  
            db.session.commit()
            flash("The Password Will Be Changed!", category="success") 
            return redirect(url_for("auth.profile"))
