import flask_mail
from blog import mail_mngr

def send_email(subject, text_body, sender, receivers, html_body=None):

    # Create a message
    msg = flask_mail.Message(subject=subject, sender=sender,
                             recipients=receivers)
    msg.body = text_body
    if html_body:
        msg.html = html_body

    mail_mngr.send(msg)
