import flask
from blog import app, models, forms, db

@app.route("/")
def homepage():
	return flask.render_template("index.html")

@app.route("/users")
def show_users():
    # Retrieve users
    users = models.User.query.all()

    # Render template
    return flask.render_template("users.html", users=users)

@app.route("/users/new", methods=('GET', 'POST'))
def add_user():
    userform = forms.NewUserForm()
    if userform.validate_on_submit():
        name = userform.name.data
        pwd  = userform.password.data

        user = models.User(name=name)

        handler = models.UserHandler(user)
        handler.add_pwd(pwd)

        if not handler.add_to_db():
            flask.flash("Unable to create user")
            return flask.redirect(flask.url_for('add_user'))
        else:
            flask.flash("Welcome {}!".format(user.name))
            return flask.redirect(flask.url_for('homepage'))

    return flask.render_template("newuser.html", userform=userform)


@app.route('/login', methods=('GET','POST'))
def login():

    loginform = forms.LoginForm()

    if loginform.validate_on_submit():
        username = loginform.username.data
        password = loginform.password.data

        user = models.User.query.filter_by(name=username).first()
        if user is None:
            flash("User {} doesn't exist.".format(username))
            return flask.redirect(flask.url_for('login'))

        user_handler = models.UserHandler(user)
        if user_handler.login(password):
            flask.flash("{} signed in !".format(username))
            return flask.redirect(flask.url_for('homepage'))
        else:
            flask.flash("Something went wrong")

    return flask.render_template('login.html',
                                form=loginform
                                )








