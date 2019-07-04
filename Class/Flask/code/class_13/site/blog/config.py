import os

DEBUG = True

# Security config

SECRET_KEY = 'my-secret-key'

# Mail config

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'bootcampdevinstitute@gmail.com'
MAIL_PASSWORD = 'aA123456!'

# DB config
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(os.getcwd(), "blog.db")

# Administration config
ADMINS = ['bootcampdevinstitute@gmail.com']
