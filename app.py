# IMPORT FILE
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.user import UserRegister, User, UserLists
from resources.store import StoreRegister, StoreList
from resources.product import Product
from resources.transaction import Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://local:local@localhost/fashion_rent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Aan' 
api = Api(app)

@app.route('/')
def home():
    return "hello flask"
 
@app.before_first_request
def create_tables():
    db.create_all()

# ENDPOINT
api.add_resource(UserRegister,'/users/<string:full_name>')
api.add_resource(User, '/user')
api.add_resource(StoreRegister,'/store/<string:name>')
api.add_resource(Product, '/product/<string:name>')
api.add_resource(Transaction, '/transaction/<string:id>')
api.add_resource(UserLists, '/users')
api.add_resource(StoreList,'/stores')



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
