import flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)
db  = SQLAlchemy(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'youllneverguess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///'+os.path.join(basedir, 'app.db')

from app import routes