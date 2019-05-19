import flask_wtf
import wtforms

class NewJuiceForm(flask_wtf.FlaskForm):

    name   = wtforms.StringField(label="Juice name:")
    recipe = wtforms.StringField(label="Juice ingredients:", description="Separate ingedients with a coma ','")

    submit = wtforms.SubmitField(label="Add juice")

class NewStoreForm(flask_wtf.FlaskForm):

    name = wtforms.StringField(label="Store name:")
    location = wtforms.StringField(label="City:")
    open_hour = wtforms.IntegerField(label="Open from:")
    close_hour = wtforms.IntegerField(label="to:")

    submit = wtforms.SubmitField(label="Add store")
