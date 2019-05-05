import flask
from juices import app, forms, models

@app.route("/")
@app.route("/index")
def homepage():
    return flask.render_template("index.html")

@app.route("/juices/new", methods=('GET', 'POST'))
def new_juice():
    form = forms.NewJuiceForm()
    if form.validate_on_submit():
        # Retrieve the data
        name        = form.name.data
        recipe      = form.recipe.data # "onions, tomatoes, banana"
        recipe_list = [s.strip() for s in recipe.split(",")]

        # Create an object
        juice = models.Juice(name, recipe_list)
        print("Added {} to juices".format(juice))

        return flask.redirect("/")
    return flask.render_template("add_juice.html", myform=form)