from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from report.config import AppConfig

from report.resources.create_tickte import CreateTickte
from report.resources.delete_ticked import DeleteTicked
from report.resources.edit_ticked import EditTicked
from report.resources.list_ticked import ListTicked
from report.resources.solve_ticked import SolveTicked

import os
import sys

app = Flask(__name__)
app.config_class(AppConfig)

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

from report.error.error_handler import app_error
app.register_blueprint(app_error)

api.add_resource(CreateTickte, "/ticket")
api.add_resource(DeleteTicked, "/ticket/<int:ticket_id>")
api.add_resource(EditTicked, "/ticket/<int:ticket_id>/edit")
api.add_resource(ListTicked, "/ticket/list")
api.add_resource(SolveTicked, "/ticket/<int:ticket_id>/answer")