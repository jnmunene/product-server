from flask import Flask,jsonify, request
import json

# create the flask application
app =Flask("Product Server")

# product list
products = [
    {'id':143,'name':'Notebook','price':140},
    {'id':144,'name':'Pen','price':20}
]

# Example request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Example request - http://localhost:5000/products/140 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"]==id][0]
    return jsonify(product)

# Example request - http://localhost:5000/products - with POST method
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json)
    return '',201

# Example request - http://localhost:5000/products/144 - with PUT method
@app.route('/products/<id>',methods=['PUT'])
def update_product(id):
    id = int(id)
    updated_product=json.loads(request.data)
    product=[x for x in products if x["id"]==id][0]
    for key, value in updated_product.items():
        product[key]=value
        return '',204
    
# Example request - http://localhost:5000/products/20
@app.route('/products/<id>',methods=['DELETE'])
def delete_product(id):
    id = int(id)
    product=[x for x in products if x["id"]==id][0]
    products.remove(product)
    return '',204

