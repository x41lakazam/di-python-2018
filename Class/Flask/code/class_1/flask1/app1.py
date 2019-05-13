import flask
from datetime import datetime

import fake_db as db  # SIMULATION

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

@app.route("/timeline")
def timeline():
    posts = [
        ('John', 'Beautiful day in New York!'),
        ('Micheal', 'Loved the last Star Wars !'),
        ('Sundar Pichai', 'I love python')
    ]

    return flask.render_template("timeline.html",
                                 posts=posts)


@app.route("/user/<int:id>")
def user_page(id):
    user = db.users[int(id)]
    return flask.render_template('user_page.html',
                                user=user)


app.run(port=5000, debug=True)