import logging
import os

from flask import Flask
from flask_bootstrap import Bootstrap

import config


bootstrap = Bootstrap()


def create_app(config_class=config.BaseConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)
    config_class.init_app(app)

    bootstrap.init_app(app)

    with app.app_context():
        from . import main

    return app
