# IMPORT FILE
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.user import UserRegister


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
    print("hello flask")
    db.create_all()
    print("hello gaes")


api.add_resource(UserRegister,'/register')



if __name__=="__main__":
    from db import db
    print("1")
    db.init_app(app)
    print("run")
    app.run(port=5000, debug=True)
