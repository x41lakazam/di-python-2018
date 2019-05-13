from blog_app import app, db
import flask

@app.route('/')
@app.route('/home')
def homepage():
    return flask.render_template('home.html')

@app.route("/users/<int:user_id>")
def userpage(user_id):
    users = db['users']

    if not 0 <= user_id < len(users):
        return notfound("User doesn't exist")

    current_user = users[user_id]

    return flask.render_template('userpage.html', user=current_user)

@app.route("/users")
def listusers():
    list_of_users = db['users']
    return flask.render_template('listusers.html', users=list_of_users)

def notfound(msg=None):
    return flask.render_template('custom404.html', message=msg)
