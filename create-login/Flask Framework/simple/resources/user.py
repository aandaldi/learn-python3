from flask_restful import Resource, reqparse
from flask import jsonify
from models.user import UserModel
from models.revokedToken import RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

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
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
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
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return jsonify({'message':'berhasil login',
                    'access_token': access_token,
                    'refresh_token': refresh_token})
            else:
                return jsonify({'message':'password salah'})

        return jsonify({'message': 'akun tidak ditemukan'})

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        print("1")
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            print("2")
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user=get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify({'access_token': access_token})


class AllUser(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResources(Resource):
    @jwt_required
    def get(self):
        return jsonify({'answer': 42})
