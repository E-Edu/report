from flask import Blueprint, jsonify
from report.response import response, Status

home = Blueprint("home", __name__)

home.route("/")
def index():
    return response(200, Status.c_200, "/", "Report MS is online")