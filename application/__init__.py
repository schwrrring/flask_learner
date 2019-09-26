from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
# https://flask-migrate.readthedocs.io/en/latest/
migrate = Migrate()


def create_app(config_type):
    app = Flask(__name__)

    app.config.from_object("config." + str(config_type))
    db.init_app(app)

    with app.app_context():

        from application.models import User, Meldung
        from application.routes import add_user, get_user
    migrate.init_app(app, db)

    return app