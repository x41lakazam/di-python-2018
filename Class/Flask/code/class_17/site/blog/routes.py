import flask
import os
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

    return flask.render_template('userpage.html',
                                 followers_n = followers_n ,
                                 following_n= following_n,
                                 usr = user_obj
                                )

@app.route("/users", methods=("GET","POST"))
def show_users():
    # Retrieve users
    users = models.User.query

    page_nb = flask.request.args.get('page_nb', 1, type=int)

    elems_per_page  = 20
    page            = users.paginate(page_nb, elems_per_page, False)

    ##############################################
    # Pagination object has 4 attributes
    # next_num: the next index
    # prev_num: the prev index 
    # has_next: True if the page has a next url
    # has_prev: True if the page has a next url
    #############################################

    # Build the next url
    if page.has_next:
        next_url = flask.url_for('show_users', page_nb=page.next_num)
    else:
        next_url = None

    if page.has_prev:
        prev_url = flask.url_for('show_users', page_nb=page.prev_num)
    else:
        prev_url = None

    pag_users = page.items

    # Render template
    return flask.render_template("users.html", 
                                 users=pag_users,
                                 next_url=next_url,
                                 prev_url=prev_url
                                ) 
@app.route("/users/new", methods=('GET', 'POST'))
def add_user():
    userform = forms.NewUserForm()
    if userform.validate_on_submit():
        name = userform.name.data
        email = userform.email.data
        pwd  = userform.password.data

        user = models.User(name=name, email=email)

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

@app.route("/change_pic", methods=('GET','POST'))
def change_pp():
    if flask.request.method.lower() == 'post':
        if 'profile_pic' not in flask.request.files:
            return flask.render_template('change_pp.html')
        file = flask.request.files['profile_pic']
        file_name = file.filename
        file_path = app.config['UPLOAD_FOLDER']
        file_save = os.path.join(file_path, file_name)
        file.save(file_save)

        file_rel_path = transform_to_relative(file_save)
        current_usr = flask_login.current_user
        models.UserHandler(current_usr).modify_pp(file_rel_path)
        print("Changed the user pp to {}".format(file_save))
        print("User {} picture is now {}".format(current_usr,
                                                 current_usr.pp_path))
    return flask.render_template('change_pp.html')

@app.route('/feed')
def feed():
    followers_posts = []
    for user in flask_login.current_user.followed:
        user_posts = user.posts
        followers_posts.extend(user_posts)
    followers_posts.sort(key=lambda post: post.date.timestamp())

    last_posts = followers_posts[:50]
    return flask.render_template("feed.html", posts=last_posts)


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
        user_email = pwd_req_form.email.data
        user_email = user_email.lower().strip()
        user = models.User.query.filter_by(email=user_email).first()

        if not user:
            flask.flash('Wrong mail')
            return flask.redirect(flask.url_for('reset_password_request'))

        # Send a mail to the user
        email.send_pwdreset_mail_to_user(user)

    return flask.render_template(
        "reset_password_request.html", 
         form=pwd_req_form
    )

@app.route('/reset_password/<token>', methods=('GET','POST'))
def reset_user_password(token):

    # Get id with token
    fake_handler = models.UserHandler('fake_user')
    user_id = fake_handler.decode_reset_password_token(token)

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

# Files functions
def file_auth(filename):
    allowed_ext = ['.txt', '.png', '.jpg', 'jpeg']
    file_ext = os.path.splitext(filename)[1]
    return file_ext in allowed_ext

def transform_to_relative(path):
    prefix = os.path.abspath(os.path.dirname(__file__))
    rel_path = '/'+os.path.relpath(path, prefix)
    return rel_path

# Render functions
def render_user_list(user_list, title):
    return flask.render_template("userlist.html", user_list=user_list, title=title)

# Errors
@app.errorhandler(401)
def unauthorized(e):
    print(str(e))
    return flask.render_template('401.html')

def custom_error(error_msg):
    return flask.render_template('custom_err.html',
                                err_msg=error_msg
                                )

@app.route('/test', methods=('GET', 'POST'))
def test_page():
    if flask.request.method == 'POST':
        if 'file' not in flask.request.files:
            return flask.redirect(flask.url_for('test_page'))

        file = flask.request.files['file']
        file_name = file.filename
        filepath  = app.config['UPLOAD_FOLDER']
        file_full_path = os.path.join(filepath, file_name)

        file.save(file_full_path)

    return flask.render_template("upload.html")


# Api functions
@app.route('/api/userlist')
def api_list_users():
    users = models.User.query.all()
    # usernames = [user.name for user in users]
    usernames = []
    for user in users:
        usernames.append(user.name)

    return flask.jsonify(usernames)







