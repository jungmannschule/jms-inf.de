import os


class Config(object):
    VERSION = '0.0.8'
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'fallback-secret')

