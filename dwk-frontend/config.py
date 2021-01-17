import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class BaseConfig:
    """Base configuration"""

    SECRET_KEY = os.environ.get("SECRET_KEY")

    @classmethod
    def init_app(cls, app):
        # log to stderr
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)


# class DevelopmentConfig(BaseConfig):
#     """Development configuration"""


# class ProductionConfig(BaseConfig):
#     """Production configuration"""
