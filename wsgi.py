"""
Entry point for uwsgi.
"""
from asgiref.wsgi import WsgiToAsgi

from config import Config
from src.start import create_app

config = Config()
app = WsgiToAsgi(create_app(config))

# if __name__ == '__main__':
#
#     app.run(host='0.0.0.0', port=1024)
