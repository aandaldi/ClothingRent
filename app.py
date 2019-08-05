# IMPORT FILE
from flask import Flask, request, render_template
from flask_restful import Api
from flask_jwt import JWT

# IMPORT EKSTERNAL LIBRARY
from resources.user import UserRegister, User, UserLists
from resources.store import StoreRegister, StoreList
from resources.product import Product
from resources.transaction import Transaction
from security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://local:local@localhost/fashion_rent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Aan' 
api = Api(app)

#INITIALISATION 
jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return "hello flask", render_template('home.html')

# ------------------- TEST AUTH LOGIN ----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html'), "hello"
    # user=request.form['username']
    # password = request.form['password']
    # authenticate(user, password)
    
    # return render_template('login.html', error=error)

# ------------------- END TEST AUTH ------------------------------
 


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
