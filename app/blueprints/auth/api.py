from flask import Blueprint
from flask_restful import Api
from app.blueprints.auth.service import Register, Login, Logout, Profile

auth_bp = Blueprint('auth', __name__)
auth_api = Api(auth_bp)

auth_api.add_resource(Register, '/register')
auth_api.add_resource(Login, '/login')
auth_api.add_resource(Logout, '/logout')
auth_api.add_resource(Profile, '/profile')
