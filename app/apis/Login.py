import time

from flask_restful import Resource, marshal_with, fields, reqparse

from app.models import User

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
    'data': fields.Nested(user_data, default='')
}

class Login(Resource):
    def post(self):
        parse = parser.parse_args()
        email = parse.get('email')
        password = parse.get('password')

        responseData = {
            'time':str(int(time.time()))
        }

        users = User.query.filter(User.email == email)
        if users.count() > 0:
            user = users.first()

            if user.isdelete == True:
                responseData['status'] = 401
                responseData['msg'] = 'login failed'
                responseData['err'] = 'email has been deleted.'
                return responseData

            if user.password == password:
                pass
            else:
                responseData['status'] = 401
                responseData['msg'] = 'login failed'
                responseData['err'] = 'password is not correct.'
                return responseData
        else:
            responseData['status'] = 401
            responseData['msg'] = 'login failed'
            responseData['err'] = 'email not existed'
            return responseData
