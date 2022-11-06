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
        
        from bs4 import BeautifulSoup
        HTMLFile = open("JoBa/templates/product.html", "r")
        index = HTMLFile.read()
        soup= BeautifulSoup(index, 'lxml')
        
        product_name = soup.find("h3", {"id": "product-name"}).text
        product_price = soup.find("h2", {"id": "product-price"}).text
        size = request.form.get("select-size")
        quantity = int(request.form.get("quantity"))
        if quantity > 12 or quantity < 1:
            flash("You Must Add 1 to 12 Piece.", category="error")
            return redirect(url_for("views.product"))
        else:
            new_product = Product(product_name=product_name, product_price=product_price, size=size, quantity=quantity, user_id=current_user.id)
            if current_user.budget < (quantity * float(product_price)):
                flash("You do not have enough money!", category="error")
                return redirect(url_for("views.product"))
            else:
                db.session.add(new_product)
                current_user.budget = current_user.budget - (quantity * float(product_price))
                db.session.commit()
                flash("Your Product Added To Cart.", category="success")
    return render_template("cart.html", title="JoBa-Cart", user=current_user)
    
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
            return redirect(url_for("auth.profile"))
        
@views.route("//delete-product", methods=["POST"])
def delete_product():
    product = json.loads(request.data)
    productId = product['productId']
    product = Product.query.get(productId)
    if product:
        if product.user_id == current_user.id:
            current_user.budget = current_user.budget + (product.quantity * float(product.product_price))
            db.session.delete(product)
            flash("The Product Deleted Form The Cart.", category="success")
            db.session.commit()
            
    return jsonify({})
        
@views.route("/contact_us")
@login_required
def contact_us():
    return render_template("contact_us.html", title="JoBa-Contact_Us", user=current_user)


