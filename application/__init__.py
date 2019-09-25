from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addsi.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'users':        'sqlite:///users.db',
        'news':        'sqlite:///news.db',
    }

    db.init_app(app)

    with app.app_context():
        from application.models import User
        from application.routes import add_user, get_user

    migrate.init_app(app, db)

    return app