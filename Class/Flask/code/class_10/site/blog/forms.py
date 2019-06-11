import flask_wtf
import wtforms

class NewUserForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Username")

    submit = wtforms.SubmitField("Sign in")

