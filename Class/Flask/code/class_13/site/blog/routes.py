import flask
import flask_login
from blog import app, models, forms, db, email

@app.route("/")
def homepage():

    current_usr = flask_login.current_user
    if current_usr.is_authenticated:
        return userpage(user_id=current_usr.id)

    return flask.render_template("index.html")

@app.route("/user/<int:user_id>")
def userpage(user_id):
    user_obj = models.User.query.filter_by(id=user_id).first()
    if not user_obj:
        return custom_error("This user doesn't exist")

    followers_n = len(list(user_obj.followers))
    following_n = len(list(user_obj.followed))

    return flask.render_template('userpage.html', followers_n = followers_n ,  following_n= following_n, usr = user_obj)

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
            flask.flash("User {} doesn't exist.".format(username))
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

#management urls

@app.route('/follow/<int:user_id>', methods=["GET", "POST"])
def follow(user_id):
    callback = flask.request.args.get('callback')
    current_user = flask_login.current_user
    if current_user.is_anonymous:
        return False
    handler = models.UserHandler(current_user)
    handler.follow(user_id)
    return flask.redirect(callback)

@app.route('/unfollow/<int:user_id>', methods=["GET", "POST"])
def unfollow(user_id):
    callback = flask.request.args.get('callback')
    current_user = flask_login.current_user
    if current_user.is_anonymous:
        return False
    handler = models.UserHandler(current_user)
    handler.unfollow(user_id)
    return flask.redirect(callback)

@app.route('/user/<int:user_id>/followers')
def user_followers(user_id):
    user_obj = models.User.query.filter_by(id = user_id).first()
    followers_list = list(user_obj.followers)

    return render_user_list(followers_list, "{} followers:".format(user_obj.name))

@app.route('/user/<int:user_id>/followings')
def user_followings(user_id):
    user_obj = models.User.query.filter_by(id = user_id).first()
    following_list = list(user_obj.followed)

    return render_user_list(following_list, "{} followings:".format(user_obj.name))

@app.route('/reset_password_request', methods=('GET','POST'))
def reset_password_request():
    pwd_req_form = forms.ResetPasswordRequestForm()
    if pwd_req_form.validate_on_submit():
        ### FAKE ###
        user = models.User.query.all()[0]
        ### END OF FAKE ###
        if not user:
            flask.flash('Wrong mail')
            return flask.redirect(flask.url_for('reset_password_request'))

        # Send a mail to the user
        send_pwdreset_mail_to_user(user)

    return flask.render_template(
        "reset_password_request.html", 
         form=pwd_req_form
    )

@app.route('/reset_password/<int:user_id>', methods=('GET','POST'))
def reset_user_password(user_id):
    reset_pwd_form = forms.ResetPassword()
    if reset_pwd_form.validate_on_submit():
        pwd = reset_pwd_form.password.data
        user = models.User.query.filter_by(id=user_id).first()
        if not user:
            flask.redirect(flask.url_for('homepage'))

        handler = models.UserHandler(user)
        handler.add_pwd(pwd)
        flask.flash("Changed password of {}".format(user.name))
    return flask.render_template('reset_password.html', form=reset_pwd_form)

# Render functions

def render_user_list(user_list, title):
    return flask.render_template("userlist.html", user_list=user_list, title=title)

# Server functions

def send_pwdreset_mail_to_user(user):
    email.send_email(
        "Reset password",
        sender=app.config['ADMINS'][0],
        receivers=["klein.fannie@gmail.com"], #receivers=[user.mail]
        text_body="-- Reset your password --"
    )


# Errors

@app.errorhandler(401)
def unauthorized(e):
    print(str(e))
    return flask.render_template('401.html')

def custom_error(error_msg):
    return flask.render_template('custom_err.html',
                                err_msg=error_msg
                                )

@app.route('/test')
def test_page():
    return custom_error("Sorry, page not found")








