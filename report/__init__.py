from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


from report.Blueprints.routes import main_page
from report.Blueprints.error_handler import app_error

app.register_blueprint(main_page)
app.register_blueprint(app_error)