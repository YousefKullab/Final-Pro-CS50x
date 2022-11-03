from flask import Blueprint, flash, render_template,request, jsonify
from flask_login import login_required, current_user
from .models import Product
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

@views.route("/product")
@login_required
def product():
    return render_template("product.html", title="JoBa-Product", user=current_user)

@views.route("/contact_us")
@login_required
def contact_us():
    return render_template("contact_us.html", title="JoBa-Contact_Us", user=current_user)



