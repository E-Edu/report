import os
import sys


class AppConfig:
    try:
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.getenv("DATABASE_USERNAME") + ":" + os.getenv(
                "DATABASE_PASSWORD") + "@" + os.getenv("DATABASE_HOSTNAME") + ":" + os.getenv(
                "DATABASE_PORT") + "/" + os.getenv("DATABASE_DATABASE")
    except:
        print("missing environment var (db)")
        sys.exit(1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class VenVar:
    try:
        JWT_SEC = os.getenv('JWT_SECRET')
    except:
        print("missing environment var (jwt)")
        sys.exit(1)
    JWT_ALGORITHMS = algorithms=['HS512']