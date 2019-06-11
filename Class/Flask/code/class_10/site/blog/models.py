from blog import db, models
import datetime

class User(db.Model):
	
	id      = db.Column(db.Integer(), primary_key=True)
	name    = db.Column(db.String(32))	
    
	posts 	= db.relationship('Post', backref="author")

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
            return False













