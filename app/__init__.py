from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config.from_object(Config)

# elasticsearch
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Login function
login = LoginManager(app)
login.login_view = 'login' # 'login' - function name

Bootstrap(app)
Moment(app)
babel = Babel(app)

from app import routes