import flask
import flask_sqlalchemy
import flask_migrate

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'you-wont-find-me'

db_path = "sqlite:///"+r"/home/pi/Documents/work/dev_institute/Courses/1python/Class/Flask/code/class_9/juices/juices.db"
app.config['SQLALCHEMY_DATABASE_URI'] = db_path

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from juices import routes, models
