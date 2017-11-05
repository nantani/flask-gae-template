# coding: utf-8
import os

from flask import Flask
from flask_cors import CORS


def create_app(env):  # type: (str) -> Flask
    app = Flask(__name__)

    config = {
        'development': 'config.DevelopmentConfig',
        'staging': 'config.StagingConfig',
        'production': 'config.ProductionConfig',
    }
    app.config.from_object(config[env])
    app.config.from_pyfile('config.cfg', silent=True)

    cors = CORS()
    cors.init_app(app, origins=app.config['ALLOW_ORIGINS'])

    import prediction.diagnosis
    app.register_blueprint(prediction.diagnosis.app)

    return app
