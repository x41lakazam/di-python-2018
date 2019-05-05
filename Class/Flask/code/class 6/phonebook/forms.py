import wtforms 
import flask_wtf

def AddContactForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("name")
    phone = wtforms.StringField("Phone:")
    submit = wtforms.SubmitField("Add contact")
