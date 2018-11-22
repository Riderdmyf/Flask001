from flask_restful import Api

from app.apis.Regest import UserRegest

api = Api()

def init_api(app):
    api.init_app(app)

api.add_resource(UserRegest, '/api/v1/regest/')