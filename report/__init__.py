from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from report.config import ProductionConfig, TestingConfig
from sentry_sdk.integrations.flask import FlaskIntegration
import os, psycopg2, sentry_sdk

SENTRY_KEY = os.environ.get("SENTRY_KEY")
SENTRY_ORGANIZATION = os.environ.get("SENTRY_ORGANIZATION")
SENTRY_PROJECT = os.environ.get("SENTRY_PROJECT")
ALL_SENTRY_VALUES_SET = os.environ.get("ALL_SENTRY_VALUES_SET")
if ALL_SENTRY_VALUES_SET == "added":
    sentry_sdk.init(
        dsn=f"https://{SENTRY_KEY}@{SENTRY_ORGANIZATION}.ingest.sentry.io/{SENTRY_PROJECT}",
        integrations=[FlaskIntegration()]
    )

db = SQLAlchemy()
api = Api()

from report.resources.ticket.create_ticket import CreateTicket
from report.resources.ticket.delete_ticket import DeleteTicket
from report.resources.ticket.edit_ticket import EditTicket
from report.resources.ticket.list_ticket import ListTicket
from report.resources.ticket.solve_ticket import SolveTicket
api.add_resource(CreateTicket, "/ticket")
api.add_resource(DeleteTicket, "/ticket/<ticket_id>")
api.add_resource(EditTicket, "/ticket/<ticket_id>/edit")
api.add_resource(ListTicket, "/ticket/list")
api.add_resource(SolveTicket, "/ticket/<ticket_id>/answer")

from report.resources.support.create_support_ticket import CreateSupportTicket
from report.resources.support.delete_support_ticket import DeleteSupportTicket
from report.resources.support.list_support_ticket import ListSupportTicket
from report.resources.support.edit_support_ticket import EditSupportTicket
api.add_resource(CreateSupportTicket, "/support")
api.add_resource(DeleteSupportTicket, "/support/<ticket_id>")
api.add_resource(ListSupportTicket, "/support/list")
api.add_resource(EditSupportTicket, "/support/<ticket_id>/edit")

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
        #db.drop_all()
        db.create_all()

    api.init_app(app)

    return app