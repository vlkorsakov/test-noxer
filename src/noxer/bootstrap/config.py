import os
from dataclasses import dataclass

from noxer.infrastructure.database.config import PostgresConfig


@dataclass(frozen=True)
class AppConfig:
    host: str
    port: int


@dataclass(frozen=True)
class Config:
    app: AppConfig
    postgres: PostgresConfig


def load_config() -> Config:
    return Config(
        app=AppConfig(
            host=os.environ["NOXER__APP__HOST"],
            port=int(os.environ["NOXER__APP__PORT"]),
        ),
        postgres=PostgresConfig(
            host=os.environ["NOXER__POSTGRES__HOST"],
            port=int(os.environ["NOXER__POSTGRES__PORT"]),
            database=os.environ["NOXER__POSTGRES__DATABASE"],
            user=os.environ["NOXER__POSTGRES__USER"],
            password=os.environ["NOXER__POSTGRES__PASSWORD"],
        ),
    )
