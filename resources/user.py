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

    # POST
    def post(self):
        data = UserRegister.parser.parse_args()

        print("ini data")
        print(data)
        user = UserModel(**data)
        print("usernya adalah")
        print (user)
        user.save_to_db()

        return {"message" : "User created successfully."}, 201
