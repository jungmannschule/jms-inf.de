import os


class Config(object):
    VERSION = '0.1.8'
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'fallback-secret')
    UPLOAD_FOLDER = 'uploads'
