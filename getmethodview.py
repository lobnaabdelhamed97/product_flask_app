from flask.views import MethodView
from flask import  jsonify, make_response
from models import Product,ProductSchema

class GET(MethodView):
    def get(self):
        get_products = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(get_products)
        return make_response(jsonify({"product": products}))