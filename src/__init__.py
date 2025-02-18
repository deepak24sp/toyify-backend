from flask import Flask
from src.blueprints import init_blueprint
from src.db import init_db
from src.config import init_config


def create_app():
    app = Flask(__name__)

    init_config(app)
    init_db(app)
    init_blueprint(app)
    return app