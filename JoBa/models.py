from . import db   # . => current package (JoBa)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10000))
    product_name = db.Column(db.DateTime(timezone= True), default=func.now())
    product_price = db.Column(db.Integer)
    product_num = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    products = db.relationship('Product')
    


