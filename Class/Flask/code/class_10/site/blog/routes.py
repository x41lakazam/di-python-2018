import flask
from blog import app

@app.route("/")
def homepage():
	return flask.render_template("index.html")
	

