from flask import Flask
from flask_migrate import Migrate

from app.models import db
from app.views import blue


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.register_blueprint(blueprint=blue)
    db.init_app(app)

    migrate = Migrate(app=app, db=db)

    return app