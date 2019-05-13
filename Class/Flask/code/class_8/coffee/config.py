import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    SECRET_KEY = 'this-is-my-password'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,
                                                        'coffee.db')
