from flask_restful import Resource, reqparse
from models.transaction import TransactionModel

class Transaction(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_created')
    parser.add_argument('created_by')
    parser.add_argument('date_modified')
    parser.add_argument('modified_by')
    parser.add_argument('product_id')
    parser.add_argument('owner_id')
    parser.add_argument('start_date')
    parser.add_argument('end_date')
    parser.add_argument('total_price')

    # POST
    def post(self, id):
        data = Transaction.parser.parse_args()
        transaction = TransactionModel.find_by_name(id)

        if transaction:
            return{"message":"Transaction already axists"}
        
        transaction = TransactionModel(**data)
        print(transaction)
        transaction.save_to_db()
        
        return {"message": "data has been saved"}
