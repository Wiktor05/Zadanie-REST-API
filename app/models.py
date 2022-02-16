from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)

    def __init__(self, nickname, email):
        self.nickname = nickname
        self.email = email

