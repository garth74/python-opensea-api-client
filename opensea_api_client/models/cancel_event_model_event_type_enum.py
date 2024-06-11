from enum import Enum


class CancelEventModelEventTypeEnum(str, Enum):
    CANCEL = "cancel"

    def __str__(self) -> str:
        return str(self.value)
