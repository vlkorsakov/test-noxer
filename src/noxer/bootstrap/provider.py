from collections.abc import Iterable

from dishka import AnyOf, Scope, provide
from dishka import Provider as DishkaProvider
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from noxer.application.committer import Committer
from noxer.bootstrap.config import Config


class Provider(DishkaProvider):
    @provide(scope=Scope.APP)
    def get_engine(self, config: Config) -> Iterable[Engine]:
        engine = create_engine(url=config.postgres.url)
        yield engine
        engine.dispose(close=True)

    @provide(scope=Scope.REQUEST)
    def get_session(
        self,
        engine: Engine,
    ) -> Iterable[AnyOf[Session, Committer]]:
        with Session(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
        ) as session:
            yield session
