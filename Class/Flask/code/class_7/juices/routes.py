import flask
from juices import app, forms, models

@app.route('/')
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
        flask.flash("Added {} to juices".format(juice.name))

        return flask.redirect(flask.url_for('new_juice'))
    return flask.render_template("add_juice.html", myform=form)

@app.route('/juices')
def all_juices():
    juices_obj = models.Juice.class_objs
    return flask.render_template("all_juices.html", juices=juices_obj)

@app.route('/stores/new', methods=('GET','POST'))
def new_store():
    store_form = forms.NewStoreForm()

    if store_form.validate_on_submit():
        name = store_form.name.data
        location = store_form.location.data
        open = store_form.open_hour.data
        close = store_form.close_hour.data

        opening_hours = (open, close)

        store = models.Store(name=name,
                            location=location,
                            opening_hours=opening_hours)
        flask.flash("Added {} to the list of stores".format(store.name))
        return flask.redirect(flask.url_for('new_store'))

    return flask.render_template('new_store.html',
                                storeform=store_form,
                                )










