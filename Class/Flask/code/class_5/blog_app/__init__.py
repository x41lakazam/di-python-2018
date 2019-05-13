import flask
import json

app = flask.Flask(__name__)
db  = json.load(open('blog_app/app_db.json', 'r'))

from blog_app import routes
