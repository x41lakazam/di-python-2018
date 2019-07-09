import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import flask_mail
import os

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

mail_mngr  = flask_mail.Mail(app)
login_mngr = flask_login.LoginManager(app)

db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from blog import routes


