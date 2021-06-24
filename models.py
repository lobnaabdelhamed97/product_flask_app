from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from __init__ import app
db = SQLAlchemy(app)
ma=Marshmallow(app)
###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),unique=True)
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def __init__(self,title,productDescription,productBrand,price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
    def __repr__(self):
        return '' % self.id

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
    id = ma.auto_field()
    title = ma.auto_field()
    productDescription = ma.auto_field()
    productBrand = ma.auto_field()
    price = ma.auto_field()
db.create_all()