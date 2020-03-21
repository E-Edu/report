from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
ma = Marshmallow(app)




from report.Blueprints.routes import main_page
from report.Blueprints.error_handler import app_error

app.register_blueprint(main_page)
app.register_blueprint(app_error)