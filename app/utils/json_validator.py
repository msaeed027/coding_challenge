from functools import wraps
from flask import jsonify, request, make_response
from werkzeug.exceptions import BadRequest


def validate_json(func):
    @wraps(func)
    def wrapper(*args, **kw):
        try:
            request.json
        except BadRequest:
            return make_response(jsonify(error='Payload must be a valid json.'), 400)

        return func(*args, **kw)

    return wrapper
