import flask
from app import app, forms, models, db


@app.route("/posts/new", methods=['GET', 'POST'])
def new_post():
    form = forms.NewPostForm()
    if form.validate_on_submit():
        flask.flash("{} posted: {}".format(form.username.data, form.content.data))
        return flask.redirect(flask.url_for('new_post'))
    return flask.render_template('newpost.html', form=form)

@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
    form = forms.NewUserForm()
    if form.validate_on_submit():
        user = models.User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flask.flash("{} logged in".format(user))
        return flask.redirect(flask.url_for('new_user'))
    return flask.render_template("newuser.html", form=form)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')