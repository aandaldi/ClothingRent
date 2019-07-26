from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument(
        'full_name',
        type =str,
        required=True,
        help = "this field cannot be blank",
    ) 

    parser.add_argument('date_created')
    parser.add_argument('created_by')
    parser.add_argument('date_modified')
    parser.add_argument('modified_by')


    parser.add_argument(
        'gender',
        type =str,
        required=True,
        help = "this field cannot be blank"
    )
    
    parser.add_argument(
        'phone',
        type =str,
        required=True,
        help = "this field cannot be blank"
    )

    parser.add_argument(
        'address',
        type =str,
        required=True,
        help = "this field cannot be blank"
    )

    parser.add_argument(
        'email',
        type =str,
        required=True,
        help = "this field cannot be blank"
    )

    parser.add_argument(
        'password',
        type =str,
        required=True,
        help = "this field cannot be blank"
    )
    
    # GET
    def get(self, full_name):
        user = UserModel.find_by_name(full_name)

        if user:
            return user.json()
        return {'message': 'User Not Found'}, 404

    # PUT
    def put(self, full_name):
        data = UserRegister.parser.parse_args()
        print(data)
        user = UserModel.find_by_name(full_name)
        
        if user is None:
            print("data tidak di temukan")
            user = UserModel(**data)
            print(user.json())

            print("data berhasil di ditambahkan")
            
        else:
            print("data di temukan")

            user.full_name = data['full_name']
            user.gender    = data['gender']
            user.phone     = data['phone']
            user.address   = data['address']
            user.email     = data['email']

            print(user.json())


            print("data berhasil diupdate")

        user.save_to_db()
        return {"message":"data has been saved"}

    # DELETE
    def delete(self, full_name):
        user = UserModel.find_by_name(full_name)

        if user:
            print("ditemukan")
            user.delete_from_db()
            return {"message": "Users delete"}
        print("ngga ada")
        return {"message": "User Not Deleted"}


class User(Resource):
    # POST
    def post(self):
        data = UserRegister.parser.parse_args()
        full_name = data['full_name']
        user = UserModel(**data)
        print(full_name)
        # print ('data User adalah : ', user)
        if UserModel.find_by_name(full_name):
            print("A User with name '{}' already axists.".format(full_name))
            return {"message":"User Already axists"}, 400                
        user.save_to_db()
        return {"message" : "User created successfully."}, 201

class UserLists(Resource):
    def get(self):
        return {'users':[x.json() for x in UserModel.query.all()]}