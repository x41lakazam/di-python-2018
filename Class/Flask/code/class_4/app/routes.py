from app import app, forms
import flask

@app.route("/")
@app.route("/home")
def home():
    return flask.render_template("index.html")

@app.route("/posts/new", methods=['GET', 'POST'])
def new_post():
    post_form = forms.NewPostForm()
    if post_form.validate_on_submit():
        # Retrieve the data
        username    = post_form.username.data
        post_title  = post_form.title.data
        post_body   = post_form.content.data
        print("{} Posted: {}\n{}\n".format(username, post_title, post_body))

        return flask.redirect(flask.url_for('home'))

    return flask.render_template("newpost.html", form=post_form)
