import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'you-wont-find-me'

from juices import routes