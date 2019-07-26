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

    # POST
    def post(self, name):
        data = StoreRegister.parser.parse_args()

        store = StoreModel.find_by_name(name)
        if store:
            return {"message":"The Store already axist"}, 400

        store = StoreModel(**data)
        print(store)
        
        store.save_to_db()
        return {"message" : "Store created successfully."}, 201
    
    # GET
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"Store not Found"}

    # PUT
    def put(self, name):
        store = StoreModel.find_by_name(name)
        data = StoreRegister.parser.parse_args()

        if store:
            store.name = data['name']
            store.address = data['address']
            store.owner_name = data['owner_name']
            store.phone = data['phone']

            print ("data berhasil di update")
        else:
            store = StoreModel(**data)
            print ("data baru berhasil di save")

        store.save_to_db()
        return {"message":"successfully"}

    # DELETE 
    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {"message":"Store has been delete"}
        return {"message":"Store Not Found"}, 404

class StoreList(Resource):
    def get(self):
        return {"store":[x.json() for x in StoreModel.query.all()]}
