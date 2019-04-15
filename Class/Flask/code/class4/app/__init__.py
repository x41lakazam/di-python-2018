import flask

app = flask.Flask(__name__)

# Defining app config
app.config['SECRET_KEY'] = "p4$$w0rd!"

# Import the routes
from app import routes