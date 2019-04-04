import flask
from datetime import datetime

app = flask.Flask(__name__)

@app.route("/")
@app.route('/index')
def index():

    return flask.render_template("index.html",
                                 title="Eyal's site",
                                 author_name="Eyal")

@app.route('/what-time-is-it')
def get_time():
    now = datetime.now()
    return "Date and hour: "+str(now)

@app.route("/get_hello")
def say_hello():
    return flask.render_template("say_hello_template.html",
                                 name="Henry")

app.run(port=5000, debug=True)