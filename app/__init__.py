from flask import Flask
from app.config import Config
from app.models.energy_models import db
from app.views.energy_view import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/api')

    return app
