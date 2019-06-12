from blog import db, models, login_mngr
import datetime

import flask_login
from werkzeug import security as sec

@login_mngr.user_loader
def load_user(id):
    id = int(id)
    user = User.query.get(id)
    return user

class User(flask_login.UserMixin, db.Model):

    id              = db.Column(db.Integer(), primary_key=True)
    name            = db.Column(db.String(32))
    password_hash   = db.Column(db.String(256))

    posts = db.relationship('Post', backref="author")

    def __repr__(self):
        return "<User {}>".format(self.name)

class Post(db.Model):

	id      = db.Column(db.Integer(), primary_key=True)

	title   = db.Column(db.String(32))
	content = db.Column(db.Text())
	date	= db.Column(db.DateTime(), default=datetime.datetime.now())

	author_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Post {}>".format(self.title)


class UserHandler:

    def __init__(self, user_obj):
        self.user_obj = user_obj

    def add_to_db(self):

        users = models.User.query.filter_by(name=self.user_obj.name).first()
        if users is None:
            db.session.add(self.user_obj)
            db.session.commit()
            return True
        else:
            print("User {} already exist".format(self.user_obj.name))
            return False

    def add_pwd(self, pwd):
        hash = sec.generate_password_hash(pwd)
        self.user_obj.password_hash = hash

    def check_pwd(self, pwd):
        return sec.check_password_hash(self.user_obj.password_hash, pwd)

    def login(self, pwd, remember=False):

        check = self.check_pwd(pwd)
        if not check:
            return False

        flask_login.login_user(self.user_obj,remember=remember)
        return True






















