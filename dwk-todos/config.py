import os

# POSTGRES_USER = os.environ.get('POSTGRES_USER')
# POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
# DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:5432/books'


class BaseConfig:
    """Base configuration"""

    DEBUG = False
    TESTING = False
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




class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    # TODO: remove hardcode, k8s secret
    SECRET_KEY = "((AUGSd(ASdgj9asdf9ASD;n;lkdsvna;lk"
    # SQLALCHEMY_DATABASE_URI = DATABASE_URL


class ProductionConfig(BaseConfig):
    """Production configuration"""

    # SQLALCHEMY_DATABASE_URI = DATABASE_URL
