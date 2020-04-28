from flask import Blueprint, jsonify, request
from report.response import response, Status

app_error = Blueprint('error-handler', __name__)


@app_error.app_errorhandler(404)
def handle_404_error(e):
    return jsonify(response(404, Status.c_404, request.path))


@app_error.app_errorhandler(405)
def handle_405_error(e):
    return jsonify(response(405, Status.c_405, request.path))
