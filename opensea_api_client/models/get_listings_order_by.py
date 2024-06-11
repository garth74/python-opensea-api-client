from enum import Enum


class GetListingsOrderBy(str, Enum):
    CREATED_DATE = "created_date"
    ETH_PRICE = "eth_price"

    def __str__(self) -> str:
        return str(self.value)
