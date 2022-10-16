
from flask import Flask, render_template, redirect
from requests import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="JoBa-Home")

@app.route("/shop")
def shop():
    return render_template("shop.html", title="JoBa-Shop")

@app.route("/product")
def product():
    return render_template("product.html", title="JoBa-Product Details")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="JoBa-Blog")

@app.route("/about")
def about():
    return render_template("about.html", title="JoBa-About")

@app.route("/contact")
def contact():
    return render_template("contact_us.html", title="JoBa-Contact Us")


if __name__ == "__main__":
    
    app.run(debug=True, port= 5000)
    
    
# Software Engineer Joseph 