from enum import Enum


class TransferEventModelEventTypeEnum(str, Enum):
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
