from typing import Protocol


class Committer(Protocol):
    def commit(self) -> None:
        raise NotImplementedError
