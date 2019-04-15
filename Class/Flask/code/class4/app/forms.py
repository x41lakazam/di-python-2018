import flask_wtf
import wtforms

class NewPostForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username")
    title    = wtforms.StringField("Title")
    content  = wtforms.StringField("Content")

    submit = wtforms.SubmitField("Post")