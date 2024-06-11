from enum import Enum


class OrderTypeEnum(str, Enum):
    BASIC = "basic"
    CRITERIA = "criteria"
    DUTCH = "dutch"
    ENGLISH = "english"

    def __str__(self) -> str:
        return str(self.value)
