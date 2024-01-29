from http import HTTPStatus

from app.utils.response_utils import make_json_response
from .extentions import jwt


def setup_jwt(app):
    jwt.init_app(app)


@jwt.unauthorized_loader
def unauthorized_response(error):
    return make_json_response({"error": {"status_code": HTTPStatus.UNAUTHORIZED,
                                         "message": HTTPStatus.UNAUTHORIZED.description,
                                         "error": HTTPStatus.UNAUTHORIZED.phrase}},
                              HTTPStatus.UNAUTHORIZED)


@jwt.invalid_token_loader
def invalid_token_callback(error="Invalid Token"):
    return make_json_response({"error": {"status_code": HTTPStatus.UNAUTHORIZED,
                                         "message": HTTPStatus.UNAUTHORIZED.description,
                                         "error": HTTPStatus.UNAUTHORIZED.phrase}},
                              HTTPStatus.UNAUTHORIZED)
