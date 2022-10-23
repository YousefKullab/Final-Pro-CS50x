
from flask import Flask, render_template, redirect
from requests import request

from helpers import login_required

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="JoBa-Home")

@app.route("/login")
def login():
    return render_template("login.html", title="JoBa-Login")

@app.route("/register")
def register():
    return render_template("register.html", title="JoBa-Register")

@app.route("/shop1")
@login_required
def shop1():
    return render_template("shop1.html", title="JoBa-Shop1")

@app.route("/shop2")
@login_required
def shop2():
    return render_template("shop2.html", title="JoBa-Shop2")

@app.route("/shop3")
@login_required
def shop3():
    return render_template("shop3.html", title="JoBa-Shop3")

@app.route("/product")
@login_required
def product():
    return render_template("product.html", title="JoBa-Product Details")

@app.route("/contact")
@login_required
def contact():
    return render_template("contact_us.html", title="JoBa-Contact Us")


if __name__ == "__main__":
    
    app.run(debug=True, port= 5000)
    
    
# Software Engineer Joseph 