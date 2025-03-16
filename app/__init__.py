from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .main import blue_main as main_blueprint

from config import DevelopmentConfig

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    bootstrap.init_app(app)
    db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app


from . import models
from . import main
