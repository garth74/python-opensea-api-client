from enum import Enum


class ListEventsByAccountEventTypeItem(str, Enum):
    ALL = "all"
    CANCEL = "cancel"
    ORDER = "order"
    REDEMPTION = "redemption"
    SALE = "sale"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
