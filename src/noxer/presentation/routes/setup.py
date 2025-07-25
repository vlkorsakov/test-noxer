from flask import Flask

from noxer.presentation.routes import root


def setup_blueprints(application: Flask) -> None:
    application.register_blueprint(root.blueprint)
