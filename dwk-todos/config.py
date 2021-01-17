import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

SQLITE_DB_PATH = "sqlite:///" + os.path.join(basedir, "app.db")
DATABASE_URL = "postgres://postgres:example@postgres-svc.dwk-todos:5432/postgres"


class BaseConfig:
    """Base configuration"""

    # DEBUG = False
    # TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or SQLITE_DB_PATH
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app):
        pass
        # log to stderr
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)


# TODO: figure out how to choose config based on env variable
# class DevelopmentConfig(BaseConfig):
#     """Development configuration"""


# class ProductionConfig(BaseConfig):
#     """Production configuration"""
