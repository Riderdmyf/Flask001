from flask_restful import Resource


class Trail(Resource):
    def get(self):
        return {
            'msg':'get the fuck out of here'
        }