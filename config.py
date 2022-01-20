"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class MyConfig:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    LOG_FILE = path.join(path.dirname(path.realpath(__file__)), environ.get('LOG_FILE'))

class ProdConfig(MyConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    CAMPAIGNS_API_URI = environ.get('PROD_CAMPAIGNS_URI')


class DevConfig(MyConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    CAMPAIGNS_API_URI = environ.get('DEV_CAMPAIGNS_URI')
