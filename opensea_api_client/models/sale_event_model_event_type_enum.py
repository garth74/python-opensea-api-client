from enum import Enum


class SaleEventModelEventTypeEnum(str, Enum):
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
