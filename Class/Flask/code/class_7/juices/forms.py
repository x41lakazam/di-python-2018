import flask_wtf
import wtforms

class NewJuiceForm(flask_wtf.FlaskForm):

    name   = wtforms.StringField(label="Juice name:")
    recipe = wtforms.StringField(label="Juice ingredients:", description="Separate ingedients with a coma ','")

    submit = wtforms.SubmitField(label="Add juice")