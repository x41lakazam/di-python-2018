from blog import db, models, login_mngr
import datetime

import flask_login
from werkzeug import security as sec

@login_mngr.user_loader
def load_user(id):
    id = int(id)
    user = User.query.get(id)
    return user

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer(), db.ForeignKey('user.id'))
)

class User(flask_login.UserMixin, db.Model):

    id              = db.Column(db.Integer(), primary_key=True)
    name            = db.Column(db.String(32))
    password_hash   = db.Column(db.String(256))
    last_seen       = db.Column(db.DateTime(), default=datetime.datetime.now())

    posts = db.relationship('Post', backref="author")

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
     )

    def has_posts(self):
        return len(self.posts) > 0

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
        self.update_last_seen()
        return True

    def update_last_seen(self):
        self.user_obj.last_seen = datetime.datetime.now()
        db.session.commit()

    def follow(self, id_to_follow):
        usr = User.query.filter_by(id=id_to_follow).first()
        usr.followers.append(self.user_obj)
        self.user_obj.followed.append(usr)

class PostHandler():

    def __init__(self, post_obj, user_id):
        self.post_obj = post_obj
        self.user_id  = user_id

    def add_to_db(self):
        user_obj = models.User.query.filter_by(id=self.user_id).first()

        if not user_obj:
            return False

        user_obj.posts.append(self.post_obj)
        db.session.commit()


