import os

from dotenv import load_dotenv
from flask import Flask, g
from pony.flask import Pony
from src.models import db as database


def create_app(config_object=None):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)

    connect_db(app)
    Pony(app)
    register_blueprints(app)

    @app.before_request
    def inject_g():
        g.version = app.config['VERSION']

    return app


def connect_db(app):
    if app.debug:
        database.bind(provider='sqlite', filename='../sqlite.db')
    else:
        database.bind(provider='mysql', host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD'), db=os.getenv('DB_NAME'))
    database.generate_mapping()


def register_blueprints(app):
    from src.routes.main import bp as bp_main
    app.register_blueprint(bp_main)
    from src.routes.python import bp as bp_python
    app.register_blueprint(bp_python)
    # from src.routes.web7 import bp as bp_web7
    # app.register_blueprint(bp_web7, url_prefix='/web7')
    # from src.routes.godot10 import bp as bp_godot10
    # app.register_blueprint(bp_godot10)
    from src.routes.office6 import bp as bp_office6
    app.register_blueprint(bp_office6, url_prefix='/office6')
    from src.routes.scratch7 import bp as bp_scratch7
    app.register_blueprint(bp_scratch7, url_prefix='/scratch7')
    from src.routes.project10 import bp as bp_project10
    app.register_blueprint(bp_project10, url_prefix='/project10')
    from src.routes.cybersec8 import bp as bp_cybersec8
    app.register_blueprint(bp_cybersec8, url_prefix='/cybersec8')
