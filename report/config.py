import os
import sys


class AppConfig:
    try:
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.environ.get("DATABASE_USERNAME") + ":" + os.environ.get(
                "DATABASE_PASSWORD") + "@" + os.environ.get("DATABASE_HOSTNAME") + ":" + os.environ.get(
                "DATABASE_PORT") + "/" + os.environ.get("DATABASE_DATABASE")
    except:
        print(os.environ)
        print("missing environment var (db)")
        sys.exit(1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class VenVar:
    try:
        JWT_SEC = os.environ.get('JWT_SECRET')
    except:
        print(os.environ)
        print("missing environment var (jwt)")
        sys.exit(1)
    JWT_ALGORITHMS = algorithms=['HS512']