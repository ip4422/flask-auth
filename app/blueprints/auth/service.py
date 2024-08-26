from http import HTTPStatus
from flask import request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token,
    unset_jwt_cookies
)
from app.utils.response_utils import make_json_response
from app.blueprints.user.model.users import User, user_list


class Register(Resource):
    def post(self):
        if not request.is_json:
            return make_json_response({'message': 'Missing JSON in request'}, HTTPStatus.BAD_REQUEST)

        data = request.get_json()
        required_data = {"password", "username", "email"}
        if not all(key in data for key in required_data):
            return make_json_response({'message': 'Missing data in request'}, HTTPStatus.BAD_REQUEST)

        hashed_password = data['password']
        hashed_password = generate_password_hash(
            data['password'], method='pbkdf2')
        new_user = User(public_id=str(
            uuid.uuid4()), username=data['username'], email=data['email'], password=hashed_password)
        new_user.save()
        return make_json_response({'message': 'User registered successfully!'}, HTTPStatus.CREATED)


class Login(Resource):
    def post(self):
        if not request.is_json:
            return make_json_response({'message': 'Missing JSON in request'}, HTTPStatus.BAD_REQUEST)

        data = request.get_json()
        required_data = {"password", "email"}
        if not all(key in data for key in required_data):
            return make_json_response({'message': 'Missing data in request'}, HTTPStatus.BAD_REQUEST)

        user = User.get_by_email(data['email'])
        if not user:
            return make_json_response({'message': 'User not found!'}, HTTPStatus.NOT_FOUND)
        if user.check_password(data['password']):
            access_token = create_access_token(
                identity=user.public_id, fresh=True)
            refresh_token = create_refresh_token(identity=user.public_id)
            return make_json_response({'access_token': access_token, 'refresh_token': refresh_token}, HTTPStatus.OK)
        return make_json_response({'message': 'Something wrong!'}, HTTPStatus.UNAUTHORIZED)


class Logout(Resource):
    @jwt_required()
    def delete(self):
        resp = jsonify({"msg": "Successfully logged out"})
        unset_jwt_cookies(resp)
        return make_json_response({'message': 'Logged out'}, HTTPStatus.OK)


class Profile(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        if not current_user:
            return make_json_response({'message': 'You are not logged in!'}, HTTPStatus.UNAUTHORIZED)
        user = next(
            (user for user in user_list if user.public_id == current_user), None)
        if not user:
            make_json_response(
                {'message': 'User not found!'}, HTTPStatus.NOT_FOUND)
        user_data = {
            'public_id': user.public_id,
            'username': user.username,
            'email': user.email
        }
        return make_json_response({'user': user_data}, HTTPStatus.OK)
