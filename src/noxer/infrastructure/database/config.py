from dataclasses import dataclass

from sqlalchemy import URL, make_url


@dataclass(frozen=True)
class PostgresConfig:
    host: str
    port: int
    database: str
    user: str
    password: str

    @property
    def url(self) -> URL:
        return make_url(
            f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}",
        )
