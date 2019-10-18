from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager


from resources import user


app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)



# Setting DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://local:local@localhost/user_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/",methods=['GET', 'POST'])
def index():
    """pass"""
    return jsonify({'message':'Hello World'})


api.add_resource(user.UserRegistration, '/registration')
api.add_resource(user.UserLogin, '/login')
api.add_resource(user.UserLogoutAccess, '/logout/access')
api.add_resource(user.UserLogoutRefresh, '/logout/refresh')
api.add_resource(user.TokenRefresh, '/token/refresh')
api.add_resource(user.AllUser, '/users')
api.add_resource(user.SecretResources, '/secret')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)