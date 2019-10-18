from flask_restful import Resource, reqparse
from flask import jsonify
from models.user import UserModel
from flask_jwt_extended import (create_access_token)

parser = reqparse.RequestParser()

parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return jsonify({'message': 'User {} already exists'.format(data['username'])})
        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

        return data


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = UserModel(
            username=data['username'],
            password=data['password']
        )

        current_users = UserModel.find_by_username(data['username'])

        if current_users:
            if UserModel.verify_hash(data['password'], current_users.password):
                return jsonify({'message':'berhasil login'})
            else:
                return jsonify({'message':'password salah'})

        return jsonify({'message': 'akun tidak ditemukan'})

class UserLogoutAccess(Resource):
    def post(self):
        return jsonify({'message': 'User Logout'})


class UserLogoutRefresh(Resource):
    def post(self):
        return jsonify({'message': 'User Logout'})


class TokenRefresh(Resource):
    def post(self):
        return jsonify({'message': 'Token Refresh'})


class AllUser(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResources(Resource):
    def get(self):
        return jsonify({'answer': 42})
