import flask
import flask_sqlalchemy
import flask_migrate
import flask_login

import os 

app = flask.Flask(__name__)

login_mngr = flask_login.LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(os.getcwd(), "blog.db")

app.config['SECRET_KEY'] = "my secret key"
db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from blog import routes


