from flask_restful import Resource, reqparse
from models.store import StoreModel

class StoreRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'address',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'owner_name',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )
    parser.add_argument(
        'phone',
        type =str,
        required=True,
        help = "this field cannot be blank",
    )

    parser.add_argument('date_created')
    parser.add_argument('created_by')
    parser.add_argument('date_modified')
    parser.add_argument('modified_by')

    def post(self):
        data = StoreRegister.parser.parse_args()

        store = StoreModel(**data)
        print(store)
        
        store.save_to_db()
        return {"message" : "Store created successfully."}, 201
