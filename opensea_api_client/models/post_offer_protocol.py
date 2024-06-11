from enum import Enum


class PostOfferProtocol(str, Enum):
    SEAPORT = "seaport"

    def __str__(self) -> str:
        return str(self.value)
