import logging
import os
import sys
from logging.config import dictConfig

import config
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_class=config.DevelopmentConfig):
    # dictConfig({
    #     'version': 1,
    #     'formatters': {'default': {
    #         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #     }},
    #     'handlers': {'wsgi': {
    #         'class': 'logging.StreamHandler',
    #         'stream': 'ext://sys.stdout',
    #         'formatter': 'default'
    #     }},
    #     'root': {
    #         'level': 'INFO',
    #         'handlers': ['wsgi']
    #     }
    # })
    app = Flask(__name__)

    app.config.from_object(config_class)
    config_class.init_app(app)

    bootstrap.init_app(app)

    with app.app_context():
        from . import main

    return app