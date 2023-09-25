import os


class Config(object):
    VERSION = '0.0.3'
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'fallback-secret')

