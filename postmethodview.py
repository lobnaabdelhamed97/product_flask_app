from flask.views import MethodView
from flask import  request,jsonify, make_response

from models import Product,ProductSchema,db

class POST(MethodView):
    def post(self):
        flag=0
        data = request.get_json()
        product_schema = ProductSchema()
        product = product_schema.load(data)
        result = product_schema.dump(product)

        get_products = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(get_products)
        #update
        for item in products:
            if item["title"] == product['title']:
                flag=1
                get_product = Product.query.get(item["id"])
                get_product.title = product['title']
                get_product.productDescription = product['productDescription']
                get_product.productBrand = product['productBrand']
                get_product.price = product['price']
                db.session.add(get_product)
                db.session.commit()
            
                print('found')
        #insert
        if flag==0:
            newproduct=Product(title=product['title'],productDescription=product['productDescription'],productBrand=product['productBrand'],price=product['price'])
            db.session.add(newproduct)
            db.session.commit()       
        return make_response(jsonify({"product": result}),200)



