from coffee import db

class Coffee(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(32))
    strength    = db.Column(db.Integer)
    price       = db.Column(db.Float)


