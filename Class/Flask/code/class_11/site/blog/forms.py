import flask_wtf
import wtforms
from wtforms import validators

class NewUserForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Username",validators=[validators.DataRequired()])
    password = wtforms.PasswordField("Password",
                                     validators=[validators.DataRequired()])
    submit = wtforms.SubmitField("Sign up")

class LoginForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username",
                                   validators=[validators.DataRequired()])
    password = wtforms.PasswordField("Password", 
                                    validators=[validators.DataRequired()])

    submit = wtforms.SubmitField("Sign in")

class NewPostForm(flask_wtf.FlaskForm):
    title   = wtforms.StringField("Title", validators=[validators.DataRequired()])
    content = wtforms.TextAreaField("Post", validators=[validators.DataRequired()])
    submit  = wtforms.SubmitField("Add Post")
