from flask import jsonify, make_response


def make_json_response(data, status, headers=None):
    if data is None:
        data = {}
    response = {"success": True, "type": status.name, "data": data}
    if not headers:
        headers = {"content-type": "application/json"}
    return make_response(jsonify(response), status.value, headers)
