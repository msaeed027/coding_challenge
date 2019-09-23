from flask import Blueprint, request, make_response, jsonify
import json
from ..services.combination import Combination
from ..infrastructure.json_validator import validate_json

api = Blueprint('api', __name__)


@api.route("/combine", methods=["POST"])
@validate_json
def combine():
    combination_type = request.args.get('combination_type')

    lists = request.json

    if not isinstance(lists, list) or not lists:
        error = 'Request should contains list of lists (at least one list represents the products).'
        return make_response(jsonify(error=error), 400)
    elif not lists[0]:
        error = 'Request should contains list of lists which first list should include at least one product.'
        return make_response(jsonify(error=error), 400)

    res = None

    if combination_type is not None:
        if combination_type == 'custom':
            res = Combination.custom_combine(lists)
        elif combination_type == 'rx':
            try:
                res = Combination.rx_combine(lists)
            except Exception:
                error = 'Something went wrong. please use another combination type.'
                return make_response(jsonify(error=error), 500)

    if not res:  # built-in python method
        res = Combination.py_combine(lists)

    return json.dumps(res)
