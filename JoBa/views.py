from flask import Blueprint, flash, render_template,request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Product, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route("/")
def home(): 
    return render_template("home.html", title="JoBa-Home", user=current_user)

@views.route("/shop1")
@login_required
def shop1():
    return render_template("shop1.html", title="JoBa-Shop1", user=current_user)

@views.route("/shop2")
@login_required
def shop2():
    return render_template("shop2.html", title="JoBa-Shop2", user=current_user)

@views.route("/shop3")
@login_required
def shop3():
    return render_template("shop3.html", title="JoBa-Shop3", user=current_user)

@views.route("/product", methods=["GET", "POST"])
@login_required
def product():
    if request.method == "GET":
        return render_template("product.html", title="JoBa-Product", user=current_user)
    else:
        ###############################################################################################
                                            # Note >>> Problem
        ###############################################################################################
        product_name = "Product name"
        product_price = int("100")
        size = request.form.get("select-size")
        quantity = int(request.form.get("quantity"))
        total = quantity * int(product_price)
        
        new_product = Product(product_name=product_name, product_price=product_price, size=size, quantity=quantity, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        flash("Your Product Added To Cart.", category="success")
        return redirect(url_for("views.cart"))
    

@views.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    
    if request.method == "GET":
        return render_template("cart.html", title="JoBa-Cart", user=current_user)
    else:
        user = User.query.filter_by(email=current_user.email).first()
        input_money = int(request.form.get("money"))
        if input_money <= 0:
            flash("You must add number greater than zero", category="error")
            return redirect(url_for("views.cart"))
        else:
            new_budget = user.budget + input_money
            user.budget = new_budget
            db.session.commit()
            flash("Money has been added successfully", category="success")
            return redirect(url_for("views.cart"))
        
@views.route("/contact_us")
@login_required
def contact_us():
    return render_template("contact_us.html", title="JoBa-Contact_Us", user=current_user)


