from enum import Enum


class RarityStrategyId(str, Enum):
    OPENRARITY = "openrarity"

    def __str__(self) -> str:
        return str(self.value)
