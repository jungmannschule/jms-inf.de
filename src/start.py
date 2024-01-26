import os

from dotenv import load_dotenv
from flask import Flask, g
from tortoise import Tortoise, run_async


def create_app(config_object=None):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    run_async(connect_db(app))

    @app.before_request
    def inject_g():
        g.version = app.config['VERSION']

    return app


async def connect_db(app):
    if app.debug:
        connection_string = f'sqlite://sqlite.db'
    else:
        user, password, host, database = os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_NAME')
        connection_string = f'mysql://{user}:{password}@{host}/{database}'
    await Tortoise.init(
        db_url=connection_string,
        modules={'models': ['src.models']}
    )


def register_blueprints(app):
    from src.routes.main import bp as bp_main
    app.register_blueprint(bp_main)
    from src.routes.python import bp as bp_python
    app.register_blueprint(bp_python)
