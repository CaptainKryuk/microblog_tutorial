import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # setting database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    POSTS_PER_PAGE = 25

    LANGUAGES = ['en', 'es']