from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import sys
import pymysql

app = Flask(__name__)

try:
    db_path = "mysql+pymysql://" + os.environ.get("DATABASE_USERNAME") + ":" + os.environ.get("DATABASE_PASSWORD") + "@" + os.environ.get("DATABASE_HOSTNAME") + ":" + os.environ.get("DATABASE_PORT") + "/" + os.environ.get("DATABASE_DATABASE")
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
except TypeError:
    sys.exit(1)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from report.Blueprints.routes import main_page
from report.Blueprints.error_handler import app_error

app.register_blueprint(main_page)
app.register_blueprint(app_error)