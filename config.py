import os


class Config(object):
    VERSION = '0.0.9'
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'fallback-secret')

