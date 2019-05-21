import flask
from juices import app, forms, models, db

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

        # Create an object
        juice = models.Juice(name=name, recipe=recipe)
        db.session.add(juice)
        db.session.commit()

        flask.flash("Added {} to juices".format(juice.name))

        return flask.redirect(flask.url_for('new_juice'))
    return flask.render_template("add_juice.html", myform=form)

@app.route('/juices')
def all_juices():
    juices_obj = models.Juice.query.all()
    return flask.render_template("all_juices.html", juices=juices_obj)

@app.route("/juices/<juice_id>")
def juice_details(juice_id):
    juice = models.Juice.query.filter_by(id=juice_id).first()
    return flask.render_template('juice_details.html',
                         juice=juice
                         )


@app.route('/stores/new', methods=('GET','POST'))
def new_store():
    store_form = forms.NewStoreForm()

    if store_form.validate_on_submit():
        name     = store_form.name.data
        location = store_form.location.data
        open_h   = store_form.open_hour.data
        close_h  = store_form.close_hour.data

        store = models.Store(name=name,
                            city=location,
                            open_h=open_h,
                            close_h=close_h
                            )

        db.session.add(store)
        db.session.commit()

        flask.flash("Added {} to the list of stores".format(store.name))
        return flask.redirect(flask.url_for('new_store'))

    return flask.render_template('new_store.html',
                                storeform=store_form,
                                )










