from flask import Flask, g


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)

    @app.before_request
    def inject_g():
        g.version = app.config['VERSION']

    return app

# def init_login(app):
    # login = LoginManager(app)
    # login.login_view = 'main.login'
    # login.login_message = 'Bitte einloggen.'

    # @login.user_loader
    # def load_user(user_id):
        # pass


def register_blueprints(app):
    from src.routes.main import bp as bp_main
    app.register_blueprint(bp_main)
