from enum import Enum


class PostListingProtocol(str, Enum):
    SEAPORT = "seaport"

    def __str__(self) -> str:
        return str(self.value)
