from flask import Blueprint, render_template, abort,request, jsonify


app_error = Blueprint('error-handler',__name__)

@app_error.app_errorhandler(404)
def handle_404_error(e):
    return jsonify({'error':'Page not found'}),404

@app_error.app_errorhandler(405)
def handle_405_error(e):
    return jsonify({'error':'Method not allowed'}),404