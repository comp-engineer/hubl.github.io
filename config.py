import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/your_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
