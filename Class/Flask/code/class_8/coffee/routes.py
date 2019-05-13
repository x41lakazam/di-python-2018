from coffee import app, forms, models, db
import flask

@app.route("/")
def homepage():
    coffees = models.Coffee.query.all()
    return flask.render_template('index.html', coffees=coffees)

@app.route("/coffees/new", methods=('GET','POST'))
def add_coffee():
    coffee_form = forms.AddCoffeeForm()

    if coffee_form.validate_on_submit():
        name = coffee_form.name.data
        strength = coffee_form.strength.data
        price    = coffee_form.price.data

        coffee   =  models.Coffee(name=name, strength=strength, price=price)
        db.session.add(coffee)
        db.session.commit()
        print("Added {} to coffees list".format(coffee))

        return flask.redirect(flask.url_for('homepage'))
    return flask.render_template('add_coffee.html', form=coffee_form)







