from enum import StrEnum
from flask import jsonify, make_response


class ResponseMessage(StrEnum):
    INVALID_REQUEST_JSON_BODY = "Missing JSON in request"
    INVALID_AUTH_REQUEST = "Provided authentication data is invalid"

    # User
    USER_NOT_FOUND = "User not found"
    USER_CREATED = "User created successfully"

    # Auth
    LOGGED_OUT = "Logged out"
    SUCCESSFULLY_LOGGED_OUT = "Successfully logged out"
    LOGGED_IN = "Logged in"
    SUCCESSFULLY_LOGGED_IN = "Successfully logged in"
    NOT_LOGGED_IN = "You are not logged in!"

    # Common
    SOMETHING_WENT_WRONG = "Something went wrong"


def make_json_response(data, status, headers=None):
    if data is None:
        data = {}
    response = {"success": True, "type": status.name, "data": data}
    if not headers:
        headers = {"content-type": "application/json"}
    return make_response(jsonify(response), status.value, headers)
