from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from report.config import AppConfig

import os
import sys

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = AppConfig.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = AppConfig.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

from report.error.error_handler import app_error
app.register_blueprint(app_error)

from report.resources.create_ticked import CreateTickte
from report.resources.delete_ticked import DeleteTicked
from report.resources.edit_ticked import EditTicked
from report.resources.list_ticked import ListTicked
from report.resources.solve_ticked import SolveTicked

api.add_resource(CreateTickte, "/ticket")
api.add_resource(DeleteTicked, "/ticket/<int:ticket_id>")
api.add_resource(EditTicked, "/ticket/<int:ticket_id>/edit")
api.add_resource(ListTicked, "/ticket/list")
api.add_resource(SolveTicked, "/ticket/<int:ticket_id>/answer")