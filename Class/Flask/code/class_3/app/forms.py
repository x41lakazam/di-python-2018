import flask_wtf
import wtforms
from wtforms import validators

class NewPostForm(flask_wtf.FlaskForm):

    username  = wtforms.StringField("Username", validators=[validators.DataRequired()])
    content   = wtforms.StringField("Content", validators=[validators.DataRequired()])
    signature = wtforms.StringField("Signature")

    submit    = wtforms.SubmitField("Submit")

class NewUserForm(flask_wtf.FlaskForm):
    username  = wtforms.StringField('Username', validators=[validators.DataRequired()])
    email     = wtforms.StringField('Email', validators=[validators.DataRequired()])
    password  = wtforms.StringField("Password", validators=[validators.DataRequired()])

    submit    = wtforms.SubmitField("Submit")