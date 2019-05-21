from juices import db

class Juice(db.Model):

    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(64), unique=True)
    recipe = db.Column(db.String(254))

    def __repr__(self):
        return "<Juice {}>".format(self.name)

class Store(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64), unique=True)
    city    = db.Column(db.String(64))
    open_h  = db.Column(db.Integer)
    close_h = db.Column(db.Integer)

    def __repr__(self):
        return "<Store {}>".format(self.name)

