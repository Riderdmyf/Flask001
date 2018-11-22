from flask_restful import Resource, marshal_with, fields, reqparse

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='Please type your email here.')
parser.add_argument('password', type=str, required=True, help='Please type your password here.')

class IconPath(fields.Raw):
    def format(self, value):
        return '/static/img/' + value

user_data = {
    'name': fields.String,
    'token': fields.String,
    'icon':IconPath(attribute='icon'),
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_data)
}

class Login(Resource):
    pass