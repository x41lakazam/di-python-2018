import flask_wtf
import wtforms
from wtforms import validators as val

class AddCoffeeForm(flask_wtf.FlaskForm):

    name     = wtforms.StringField(label="name",
                               validators=(val.DataRequired(),))

    strength = wtforms.SelectField(label="Strength",
                                   choices=(list(zip(range(11), range(11)))),
                                   coerce=int,
                                  )
    price    = wtforms.IntegerField(label="Price",
                                   validators=(val.DataRequired(),))

    
    submit   = wtforms.SubmitField(label="Add your coffee !")
