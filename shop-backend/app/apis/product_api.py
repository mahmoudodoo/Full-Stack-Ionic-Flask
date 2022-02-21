

from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.product_model import Product

@app.route('/product',methods=['POST'])
def create_product():
   data = request.get_json()
   new_product = Product(title=data['title'],imageUrl=data['imageUrl'],description=data['description'],price=data['price'])
   db.session.add(new_product)
   db.session.commit()

   return jsonify({'message':'The product has been added !!'})


@app.route('/product',methods=['GET'])
def get_all_products():
   products = Product.query.all()
   if not products:
       return jsonify({'message':'No Products !!!'})
   output = []
   for product in products:
       product_data ={}
       product_data['id'] = product.id
       product_data['title'] = product.title
       product_data['imageUrl'] = product.imageUrl
       product_data['description'] = product.description
       product_data['price'] = product.price
       output.append(product_data)
   return jsonify(output)



@app.route('/product/<product_id>',methods=['DELETE'])
def delete_product(product_id):
   product = Product.query.filter_by(id=product_id).first()
   if not product:
       return jsonify({'message':'Product not Found!'})
   db.session.delete(product)
   db.session.commit()
   return jsonify({ 'message':'Product has been deleted!'})


