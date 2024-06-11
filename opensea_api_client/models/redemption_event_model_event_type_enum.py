from enum import Enum


class RedemptionEventModelEventTypeEnum(str, Enum):
    REDEMPTION = "redemption"

    def __str__(self) -> str:
        return str(self.value)
