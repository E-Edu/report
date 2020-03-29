import os
import sys

class AppConfig:
    try:
        db_path = "mysql+pymysql://" + os.environ.get("DATABASE_USERNAME") + ":" + os.environ.get(
            "DATABASE_PASSWORD") + "@" + os.environ.get("DATABASE_HOSTNAME") + ":" + os.environ.get(
            "DATABASE_PORT") + "/" + os.environ.get("DATABASE_DATABASE")

    except TypeError as e:
        print(e)
        print("No Environ Var found")
        sys.exit(1)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class VenVar:
    JWT_SEC = os.environ.get('JWT_SECRET')
    JWT_ALGORITHMS = algorithms=['HS256']