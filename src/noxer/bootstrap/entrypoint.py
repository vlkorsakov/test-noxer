from dishka import make_container
from flask import Flask

from noxer.bootstrap.config import Config, load_config
from noxer.bootstrap.provider import Provider
from noxer.presentation.routes.setup import setup_blueprints


def main() -> None:
    config = load_config()
    container = make_container(Provider(), context={Config: config})

    application = Flask(__name__)
    setup_blueprints(application)

    try:
        application.run(
            host=config.app.host,
            port=config.app.port,
        )
    finally:
        container.close()
