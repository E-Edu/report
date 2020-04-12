import os


class AppConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.environ.get("DATABASE_USERNAME", "root") + ":" + os.environ.get(
            "DATABASE_PASSWORD", "") + "@" + os.environ.get("DATABASE_HOSTNAME", "localhost") + ":" + os.environ.get(
            "DATABASE_PORT", "3306") + "/" + os.environ.get("DATABASE_DATABASE", "report")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class VenVar:
    JWT_SEC = os.environ.get('JWT_SECRET', "save")
    JWT_ALGORITHMS = algorithms=['HS512']