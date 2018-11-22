import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(object):
    Debug = False
    Texting = False
    secret_key = 'zxcvb1243412'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'test.db')


config = {
    'develop':DevelopConfig,
    'default':DevelopConfig
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))