import flask
import flask_login
from blog import app, models, forms, db

@app.route("/")
def homepage():
	return flask.render_template("index.html")

@app.route("/user/<int:user_id>")
def userpage(user_id):
    user_obj = models.User.query.filter_by(id=user_id).first()

    return flask.render_template('userpage.html',
                                usr=user_obj)

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
            flask.flash("{} logged in !".format(username))
            print('current_user:',flask_login.current_user)
            return flask.redirect(flask.url_for('homepage'))
        else:
            flask.flash("Something went wrong")

    return flask.render_template('login.html',
                                form=loginform
                                )

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('homepage'))

@app.route('/secret_page')
@flask_login.login_required
def secret():
    return flask.render_template('secret.html')

@app.errorhandler(401)
def unauthorized(e):
    print(str(e))
    return flask.render_template('401.html')

@app.route("/new_post", methods=('GET', 'POST'))
def newpost():
    if not flask_login.current_user.is_authenticated:
        flask.flash("You need to be logged in to post something.")
        return flask.redirect(flask.url_for('login'))

    postform = forms.NewPostForm()

    if postform.validate_on_submit():
        print("Debug")
        title   = postform.title.data
        content = postform.content.data
        post    = models.Post(title=title, content=content)

        current_user = flask_login.current_user
        user_id = current_user.id

        post_handler = models.PostHandler(post, user_id)
        post_handler.add_to_db()

        flask.flash("Your post for the blog has been added!")
        return flask.redirect(flask.url_for('homepage'))

    return flask.render_template("newpost.html", postform=postform)













