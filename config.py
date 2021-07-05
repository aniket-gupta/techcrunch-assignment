"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_ENV = environ.get('DEPLOY_ENV', 'production')
    DEBUG = False if FLASK_ENV == 'production' else True
    TESTING = False if FLASK_ENV == 'production' else True
    DATABASE_URI = environ.get('DATABASE_CONNECTION_URI', 'postgresql://postgres:@localhost:5432/techcrunch')
    CREATE_TABLES = bool(environ.get('CREATE_TABLES', "true"))
    NUM_ARTICLES = int(environ.get('NUM_ARTICLES', "100"))
    CELERY_BROKER = environ.get('CELERY_BROKER', 'redis://localhost:6379')
    CELERY_BACKEND = environ.get('CELERY_BACKEND', 'redis://localhost:6379')
