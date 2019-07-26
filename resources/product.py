from flask_restful import Resource, reqparse
from models.product import ProductModel

class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'size',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'color',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'price',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'store_id',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument('type')
    parser.add_argument('details')
    parser.add_argument('date_created')
    parser.add_argument('created_by')
    parser.add_argument('date_modified')
    parser.add_argument('modified_by')

    # POST
    def post(self,name):
        data = Product.parser.parse_args()
        product = ProductModel.find_by_name(name)

        if product:
            return {"message":"product with name '{}' already axists".format(name)}
        product = ProductModel(**data)
        print(product.json())
        product.save_to_db()
        
        return {"message":"Product has been saved"}, 200

    # GET
    def get(self, name):
        product = ProductModel.find_by_name(name)
        print(name)
        if product:
            return {"product": product.json()}, 201
        return {"message":"Product Not Found"}, 404

    # PUT
    def put(self, name):
        data = Product.parser.parse_args()
        print(data)
        product = ProductModel.find_by_name(name)
        print(name)
        if product:
            print(product.json())
            product.name = data['name']
            product.type = data['type']
            product.color = data['color']
            product.size = data['size']
            product.details = data['details']
            product.price = data['price']
            product.store_id = data['store_id']

            return {'message':"data has been update","product":product.json()}, 200

        return {"message":"Product Not Found"}, 404

    # DELETE
    def delete(self, name):
        product = ProductModel.find_by_name(name)

        if product:
            print(product.json())
            product.delete_from_db()

            return {"message":"Product with name '{}' has been deleted".format(name)}, 200

        return {"message":"Product with name '{}' has been deleted".format(name)}, 200

