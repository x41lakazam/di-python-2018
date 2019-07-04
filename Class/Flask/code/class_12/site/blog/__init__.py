import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import flask_mail
import os

app = flask.Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'bootcampdevinstitute@gmail.com',
    MAIL_PASSWORD = 'aA123456!',
))

mail_mngr  = flask_mail.Mail(app)
login_mngr = flask_login.LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(os.getcwd(), "blog.db")

app.config['SECRET_KEY'] = "my secret key"
db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from blog import routes


