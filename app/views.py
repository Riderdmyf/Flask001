from flask import Blueprint

blue = Blueprint('blue', __name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello'