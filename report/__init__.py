from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from report.config import ProductionConfig, TestingConfig
from sentry_sdk.integrations.flask import FlaskIntegration
import os, psycopg2, sentry_sdk

SENTRY_KEY = os.environ.get("SENTRY_KEY")
SENTRY_ORGANIZATION = os.environ.get("SENTRY_ORGANIZATION")
SENTRY_PROJECT = os.environ.get("SENTRY_PROJECT")
sentry_sdk.init(
    dsn=f"https://{SENTRY_KEY}@{SENTRY_ORGANIZATION}.ingest.sentry.io/{SENTRY_PROJECT}",
    integrations=[FlaskIntegration()]
)

db = SQLAlchemy()
api = Api()

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

def create_app():
    app = Flask(__name__)

    conf = os.environ.get("conf_mode")
    if conf == "deploy":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(TestingConfig)

    from report.error.error_handler import app_error
    app.register_blueprint(app_error)

    db.init_app(app)
    @app.before_first_request
    def init_tables():
        db.create_all()

    api.init_app(app)

    return app