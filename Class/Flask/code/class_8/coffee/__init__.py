import flask
import flask_sqlalchemy
import flask_migrate
from coffee import config
import os

app = flask.Flask(__name__)
app.config.from_object(config.Config)

# Declare database and migrate objects
db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from coffee import routes, models



