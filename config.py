import os


class Config(object):
    VERSION = '0.1.0'
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'fallback-secret')

