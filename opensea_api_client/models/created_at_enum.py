from enum import Enum


class CreatedAtEnum(str, Enum):
    VALUE_0 = " "

    def __str__(self) -> str:
        return str(self.value)
