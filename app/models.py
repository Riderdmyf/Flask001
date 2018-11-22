from app.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)
    isdelete = db.Column(db.Boolean, default=False)
    isactivate = db.Column(db.Boolean, default=False)