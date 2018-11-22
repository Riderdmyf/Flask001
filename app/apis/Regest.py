import hashlib
import time
import uuid

from flask_restful import Resource, marshal_with, fields, reqparse

from app.ext import db
from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Please tell me your name.')
parser.add_argument('password', type=str, required=True, help='Please type your password.')
parser.add_argument('email', type=str, required=True, help='Please tell me your email.')

'''
{
    'msg':'regest successfully',
    'status':'200',
    'time':'0123456',
    'err':'',
    'data':{
        'name':'username',
        'token':'.......',
        'icon':'../../...jpg',
    }
}
'''

user_data = {
    'name': fields.String,
    'token': fields.String,
    'icon': fields.String,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'time': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_data)
}


class UserRegest(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()

        user = User()
        user.name = parse.get('name')
        user.password = parse.get('password')
        user.email = parse.get('email')
        user.token = get_token()

        responseData = {}

        users = User.query.filter(User.email == user.email)
        if users.count > 0:
            responseData['status'] = 406
            responseData['msg'] = 'regest failed'
            responseData['err'] = 'the email has been used.'
            return responseData
        else:
            db.session.add(user)
            db.session.commit()

            responseData['status'] = 200
            responseData['msg'] = 'regest success'
            responseData['data'] = user

            return responseData

def get_token():
    hash = hashlib.sha512()
    hash_str = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(hash_str.encode('utf-8'))
    return hash.hexdigest()