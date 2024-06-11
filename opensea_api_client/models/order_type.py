from enum import Enum


class OrderType(str, Enum):
    AUCTION = "auction"
    COLLECTION_OFFER = "collection_offer"
    ITEM_OFFER = "item_offer"
    LISTING = "listing"
    TRAIT_OFFER = "trait_offer"

    def __str__(self) -> str:
        return str(self.value)
