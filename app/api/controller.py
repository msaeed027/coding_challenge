from flask import Blueprint, request
import json
from ..services.combination import Combination

api = Blueprint('api', __name__)


@api.route("/combine", methods=["POST"])
def combine():
    combination_type = request.args.get('combination_type')

    lists = request.json

    if not isinstance(lists, list):
        return ['error']
    if not len(lists) and len(lists[0]):
        return ['error']

    res = []

    if combination_type is not None:
        if combination_type == 'custom':
            res = Combination.custom_combine(lists)
        elif combination_type == 'observable':
            res = Combination.rx_combine(lists)

    if not res:  # built-in python method
        res = Combination.py_combine(lists)

    return json.dumps(res)
