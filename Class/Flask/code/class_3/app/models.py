from app import db
from datetime import datetime
from werkzeug import security

class User(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(64), index=True, unique=True)
    email       = db.Column(db.String(128), unique=True)
    passwd_hash = db.Column(db.String(128))

    posts       = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, passwd):
        hashed = security.generate_password_hash(passwd)
        self.passwd_hash = hashed
        return hashed

    def check_password(self, passwd):
        return security.check_password_hash(self.passwd_hash, passwd)

class Post(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(64))
    content     = db.Column(db.String(254))
    date        = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Post {}>".format(self.title)