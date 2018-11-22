from flask_restful import Api

from app.apis.trail import Trail

api = Api()

def init_api(app):
    api.init_app(app)

api.add_resource(Trail, '/api/v1/trail/')