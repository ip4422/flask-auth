from enum import StrEnum
from flask import jsonify, make_response
from i18n import _


class ResponseMessage(StrEnum):
    # Errors
    INVALID_REQUEST_JSON_BODY = _("Missing JSON in request")
    INVALID_AUTH_REQUEST = _("Provided authentication data is invalid")

    # User
    USER_NOT_FOUND = _("User not found")
    USER_CREATED = _("User created successfully")

    # Auth
    LOGGED_OUT = _("Logged out")
    SUCCESSFULLY_LOGGED_OUT = _("Successfully logged out")
    LOGGED_IN = _("Logged in")
    SUCCESSFULLY_LOGGED_IN = _("Successfully logged in")
    NOT_LOGGED_IN = _("You are not logged in!")

    # Common
    SOMETHING_WENT_WRONG = _("Something went wrong")


def make_json_response(data, status, headers=None):
    if data is None:
        data = {}
    response = {"success": True, "type": status.name, "data": data}
    if not headers:
        headers = {"content-type": "application/json"}
    return make_response(jsonify(response), status.value, headers)
