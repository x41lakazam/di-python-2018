import flask_mail
import flask
from blog import mail_mngr, app, models

def send_email(subject, text_body, sender, receivers, html_body=None):

    # Create a message
    msg = flask_mail.Message(subject=subject, sender=sender,
                             recipients=receivers)
    msg.body = text_body
    if html_body:
        msg.html = html_body

    mail_mngr.send(msg)
    print("Sent mail to {}".format(receivers))

def send_pwdreset_mail_to_user(user):
    # Get token
    handler = models.UserHandler(user)
    token = handler.get_reset_password_token()

    send_email(
        "Reset password",
        sender=app.config['ADMINS'][0],
        receivers=[user.email],
        text_body=flask.render_template('reset_password_mail.txt', user=user,
                                        token=token)
    )



