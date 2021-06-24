from models import Product,ProductSchema,db
from flask.views import MethodView
from flask import  make_response,request

class DELETE(MethodView):   
    def delete(self):
        data = request.get_json()
        product_schema = ProductSchema()
        product = product_schema.load(data)
        get_products = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(get_products)
        #update
        for item in products:
            if item["id"] == product['id']:
                get_product = Product.query.get(item["id"])
                db.session.delete(get_product)
                db.session.commit()
        return make_response("",204)